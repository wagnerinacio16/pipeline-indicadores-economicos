# pyrefly: ignore  # import-error
from config.utils import *


# pyrefly: ignore  # unknown-name
for nome_inidicador, parametros in INDICADORES.items():
    # pyrefly: ignore  # unknown-name
    dados = obter_dados_api(parametros)
    # pyrefly: ignore  # unknown-name
    salvar_dados_api(dados, nome_inidicador)
