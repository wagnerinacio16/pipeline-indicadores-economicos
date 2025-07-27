from config.utils import *

for nome_inidicador, parametros in INDICADORES.items():
    
    dados = ler_dados_api(parametros)
    salvar_dados_api_bronze(dados, nome_inidicador)
