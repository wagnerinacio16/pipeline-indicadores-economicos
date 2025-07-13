from config.utils import *


for nome_inidicador, parametros in INDICADORES.items():
    dados = obter_dados_api(parametros)
    salvar_dados_api(dados, nome_inidicador)
