# pyrefly: ignore  # import-error
from config.utils import *


#Ingestão dos dados na camada silver
# pyrefly: ignore  # unknown-name
for nome_indicador, parametros in INDICADORES.items():
    fonte = parametros.get('FONTE')

    # pyrefly: ignore  # unknown-name
    dados = ler_dados_indicadores(nome_indicador=nome_indicador, nome_fonte=fonte)

    if dados is not None:
        # pyrefly: ignore  # unknown-name
        salvar_dados_indicadores(dados=dados, nome_indicador=nome_indicador)
    else:
        # pyrefly: ignore  # unknown-name
        logger.warning(f"Dados do indicador '{nome_indicador}' não foram carregados.")
