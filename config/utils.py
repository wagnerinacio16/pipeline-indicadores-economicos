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