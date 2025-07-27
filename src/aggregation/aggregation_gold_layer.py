from config.utils import *

for nome_indicador, parametros in INDICADORES.items():

    indicador = ler_dados_indicadores_silver(nome_indicador=nome_indicador)
    
    if validar_schema(dados=indicador, nome_indicador=nome_indicador) is True:

        salvar_dados_indicadores_gold(dados=indicador, nome_indicador=nome_indicador)
    