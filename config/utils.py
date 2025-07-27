"""
Funções utilitárias utilizadas no projeto para ingestão, leitura e salvamento de dados.
"""



from config.schemas import *

#libs
import json
import requests
import pandas as pd
import pandera.pandas as pa
from loguru import logger


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
        resposta = requests.get(indicador['URL'],timeout=60)
        resposta.raise_for_status()  
        logger.success(f"Requisição para {indicador['NOME']} - Status: {resposta.status_code}")
        return resposta.json()
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"Erro HTTP ao acessar a URL: {indicador['URL']} - {http_err}")
        raise http_err


def salvar_dados_api(dados: dict, nome_indicador: str) -> None:
    """
    Salva os dados brutos da API na camada bronze com nome padronizado.

    Args:
        dados (dict): Dados retornados da API.
        nome_indicador (str): Nome para salvar os metadados do indicador.

    Returns:
        None
    """
    try:
        # pyrefly: ignore  # unknown-name
        nome_arquivo: str = f"{nome_indicador.lower()}_{dt.datetime.today().strftime('%Y%m%d')}.json"
        # pyrefly: ignore  # unknown-name
        caminho_arquivo = os.path.join(PATHS["BRONZE_LAYER"],nome_arquivo)
        #print(caminho_arquivo)

        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, fp=f, ensure_ascii=False, indent=4)

        logger.info(f"Indicacdor {nome_indicador} salvo no arquivo: {nome_arquivo}")

    except Exception as e:
        logger.error(f"Erro ao salvar os dados na camada bronze: {str(e)}")
        raise e
    

# pyrefly: ignore  # unknown-name
def ler_dados_indicadores(nome_indicador: str, nome_fonte: str, path: str = PATHS['BRONZE_LAYER'], data: str = DATA_FINAL) -> pd.DataFrame | None:

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
        data_str: str = pd.to_datetime(data, format="%d/%m/%Y").strftime("%Y%m%d")
        nome_arquivo: str = f"{nome_indicador}_{data_str}.json"
        # pyrefly: ignore  # unknown-name
        path_arquivo = os.path.join(path, nome_arquivo)

        logger.info(f"Lendo arquivo: {path_arquivo}")

        if nome_fonte.upper() == 'BACEN':
            df: pd.DataFrame = pd.read_json(path_arquivo)
            df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')

        elif nome_fonte.upper() == 'IBGE':
            with open(path_arquivo, "r", encoding="utf-8") as f:
                dados: Any = json.load(f)
                serie = dados[0]['resultados'][0]['series'][0]['serie']
                # pyrefly: ignore  # bad-argument-type
                df = pd.DataFrame(serie.items(), columns=['data', 'valor'])
                df['data'] = pd.to_datetime(df['data'].astype(str), format="%Y%m").dt.strftime('%d/%m/%Y')
        else:
            logger.warning(f"Fonte desconhecida: {nome_fonte}")
            return None

        df.rename(columns={'valor': nome_indicador}, inplace=True)
       
        return df

    except FileNotFoundError:
        logger.warning(f"Arquivo não encontrado: {nome_arquivo}")
    except Exception as e:
        logger.error(f"Erro ao ler {nome_indicador} - {data_str}: {e}", exc_info=True)

    return None


def salvar_dados_indicadores(dados: pd.DataFrame, nome_indicador: str) -> None:
    
    """
    Salva os dados transformados do indicador na camada Silver em formato Parquet.

    Args:
        dados (pd.DataFrame): Dados transformados do indicador.
        nome_indicador (str): Nome do indicador econômico (ex: 'IPCA', 'SELIC_META').

    Returns:
        None
    """
    try:
        nome_arquivo: str = f"{nome_indicador.lower()}.parquet"
        # pyrefly: ignore  # unknown-name
        caminho_arquivo = os.path.join(PATHS["SILVER_LAYER"], nome_arquivo)

        dados.to_parquet(caminho_arquivo)

        logger.success(f"Indicador '{nome_indicador}' salvo com sucesso em: {caminho_arquivo}")

    except Exception as e:
        logger.error(f"Erro ao salvar os dados do indicador '{nome_indicador}' na camada Silver: {str(e)}", exc_info=True)


def exportar_schemas_para_yaml() -> None:
    
    """
    Exporta todos os schemas definidos no dicionário SCHEMAS
    para arquivos YAML na pasta definida em PATHS['SCHEMAS'].
    
    Returns:
        None
    """
    for nome, schema in SCHEMAS.items():
        path_schema = os.path.joiin(PATHS['SCHEMAS'],f"{nome}.yaml")
        try:
            with open(path_schema, "w", encoding="utf-8") as f:
                f.write(schema.to_yaml())
            logger.success(f"Schema '{nome}' exportado para: {path_schema}")
        except Exception as e:
            logger.error(f"Erro ao exportar schema '{nome}': {e}")