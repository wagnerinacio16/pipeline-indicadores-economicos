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

        logger.info(f"Indicacdor {nome_indicador} salvo no arquivo: {nome_arquivo}")

    except Exception as e:
        logger.error(f"Erro ao salvar os dados na camada bronze: {str(e)}")
        raise e
    

def ler_dados_indicadores(nome_indicador: str, nome_fonte: str, path: str = PATHS['BRONZE_LAYER'], data: str = DATA_FINAL):
    """
    Lê um arquivo JSON da camada bronze e retorna um DataFrame padronizado.

    Args:
        nome_indicador (str): Nome do indicador (ex: 'IPCA').
        nome_fonte (str): Fonte dos dados (ex: 'BACEN' ou 'IBGE').
        path (str): Caminho da pasta onde está o JSON.
        data (str): Data desejada no formato 'dd/mm/yyyy'. Default: DATA_FINAL.

    Returns:
        pd.DataFrame: DataFrame formatado ou None se houver erro.
    """
    try:
        nome_indicador = nome_indicador.lower()
        data_str = pd.to_datetime(data, format="%d/%m/%Y").strftime("%Y%m%d")
        nome_arquivo = f"{nome_indicador}_{data_str}.json"
        path_arquivo = os.path.join(path, nome_arquivo)

        logger.info(f"Lendo arquivo: {path_arquivo}")

        granularidade = INDICADORES[nome_indicador]['GRANULARIDADE']

        if nome_fonte.upper() == 'BACEN':
            df = pd.read_json(path_arquivo)

        elif nome_fonte.upper() == 'IBGE':
            with open(path_arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
                serie = dados[0]['resultados'][0]['series'][0]['serie']
                df = pd.DataFrame(serie.items(), columns=['data', 'valor'])

        else:
            logger.warning(f"Fonte desconhecida: {nome_fonte}")
            return None

        df.rename(columns={'valor': nome_indicador}, inplace=True)

        if granularidade == "mensal":
            df['data'] = pd.to_datetime(df['data'].astype(str), format="%Y%m")
        elif granularidade == "diaria":
            df['data'] = pd.to_datetime(df['data'], errors='coerce')

        return df

    except FileNotFoundError:
        logger.warning(f"Arquivo não encontrado: {nome_arquivo}")
    except Exception as e:
        logger.error(f"Erro ao ler {nome_indicador} - {data_str}: {e}", exc_info=True)

    return None


def salvar_dados_indicadores(dados: pd.DataFrame, nome_indicador: str):
    """
    Salva os dados transformados do indicador na camada Silver em formato Parquet.

    Args:
        dados (pd.DataFrame): Dados transformados do indicador.
        nome_indicador (str): Nome do indicador econômico (ex: 'IPCA', 'SELIC_META').

    Returns:
        None
    """
    try:
        nome_arquivo = f"{nome_indicador.lower()}.parquet"
        caminho_arquivo = os.path.join(PATHS["SILVER_LAYER"], nome_arquivo)

        dados.to_parquet(caminho_arquivo)

        logger.success(f"Indicador '{nome_indicador}' salvo com sucesso em: {caminho_arquivo}")

    except Exception as e:
        logger.error(f"Erro ao salvar os dados do indicador '{nome_indicador}' na camada Silver: {str(e)}", exc_info=True)