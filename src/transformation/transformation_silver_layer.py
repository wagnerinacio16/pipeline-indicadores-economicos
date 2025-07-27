from config.utils import *

#Ingestão dos dados na camada silver
for nome_indicador, parametros in INDICADORES.items():
    
    fonte = parametros.get('FONTE')

    dados = ler_dados_indicadores_bronze(nome_indicador=nome_indicador, nome_fonte=fonte)

    if dados is not None:
        salvar_dados_indicadores_silver(dados=dados, nome_indicador=nome_indicador)
    else:
        logger.warning(f"Dados do indicador '{nome_indicador}' não foram carregados.")
