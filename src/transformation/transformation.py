from config.utils import *


#Ingestão dos dados de cotação na camadda silver
for nome_moeda, parametros in list(INDICADORES.items())[-7:]:
   dados_cotacao = ler_dados_cotacao(moeda=nome_moeda)
   salvar_dados_cotacao(dados=dados_cotacao,moeda=nome_moeda)