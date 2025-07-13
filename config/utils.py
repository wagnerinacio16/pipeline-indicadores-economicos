from config.constants import *


#libs
import json
import requests
import pandas as pd
from loguru import logger


#Definindo funções do projeto


def obter_dados_api(indicador:dict):
    """
    Realiza uma requisição GET a uma API pública e retorna os dados em formato JSON.

    Args:
        url (str): URL completa do endpoint da API.

    Returns:
        dict ou list: Resposta da API convertida em uma lista de dicionários (json).

    Raises:
        Exception: Caso ocorra erro de conexão ou resposta inválida.
    """
    try:
        logger.info(f"Realizando requisição da API: {indicador['NOME']}")
        resposta = requests.get(indicador['URL'])
        resposta.raise_for_status()  
        logger.success(f"Requisição para {indicador['NOME']} realizada com sucesso - Status: {resposta.status_code}")
        return resposta.json()
        

    except requests.exceptions.RequestException as erro:
        logger.error(f"Falha ao acessar a URL: {indicador['URL']}")
        raise erro


def salvar_dados_api(dados: dict, nome_indicador: str):
    """
    Salva os dados brutos da API na camada bronze com nome padronizado.

    Args:
        dados (dict): Dados retornados da API.
        nome_indicador (str): Nome para salvar os metadados do indicador.

    Returns:
        None
    """
    try:
        nome_arquivo = f"{nome_indicador.lower()}_{dt.datetime.today().strftime('%Y%m%d')}.json"
        caminho_arquivo = os.path.join(PATHS["BRONZE_LAYER"],nome_arquivo)
        #print(caminho_arquivo)

        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, fp=f, ensure_ascii=False, indent=4)

        logger.info(f"Indicacdor {nome_indicador} salvos no arquivo: {nome_arquivo}")

    except Exception as e:
        logger.error(f"Erro ao salvar os dados na camada bronze: {str(e)}")
        raise e
    

def ler_dados_cotacao(moeda: str, path: str = PATHS['BRONZE_LAYER'], data: str = DATA_FINAL):
    """
    Lê um arquivo JSON de cotação e retorna um DataFrame.

    Args:
        path (str): Caminho da pasta onde está o JSON.
        moeda (str): Nome da moeda (ex: 'USD_BRL').
        data (datetime, opcional): Data desejada. Default: DATA_FINAL.

    Returns:
        [pd.DataFrame]: DataFrame formatado ou None se houver erro.
    """

    try:
        moeda = moeda.lower()
        data_str = pd.to_datetime(data, format="%d/%m/%Y").strftime("%Y%m%d")
        nome_arquivo = f"{moeda}_{data_str}.json"
        path_arquivo = os.path.join(path, nome_arquivo)

        logger.info(f"Lendo arquivo: {path_arquivo}")

        df = pd.read_json(path_arquivo)

       
        df.rename(columns={'valor': moeda}, inplace=True)
        df = df.astype({'data': 'datetime64', moeda.lower(): 'float64'}, errors='ignore')

      
        return df

    except FileNotFoundError:
        logger.warning(f"Arquivo não encontrado: {nome_arquivo}")
    except Exception as e:
        logger.error(f"Erro ao ler {moeda} - {data_str}: {e}", exc_info=True)

    return None


def salvar_dados_cotacao(dados: pd.DataFrame, moeda: str):
    """
    Salva os dados brutos da API na camada silver.

    Args:
        dados (DataFrame): Dados retornados da API.
        nome_cotacao (str): Nome da moeda de cotação.

    Returns:
        None
    """
    try:
        nome_arquivo = f"{moeda.lower()}.parquet"
        caminho_arquivo = os.path.join(PATHS["SILVER_LAYER"],nome_arquivo)
        print(caminho_arquivo)
        dados.to_parquet(caminho_arquivo)

        
        logger.info(f"Indicacdor {moeda} salvo no arquivo: {nome_arquivo}")

    except Exception as e:
        logger.error(f"Erro ao salvar os dados na camada silver: {str(e)}")
        raise e