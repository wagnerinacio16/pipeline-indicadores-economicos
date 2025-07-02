
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.append(project_root)

from config.utils import *


for nome_inidicador, parametros in INDICADORES.items():
    dados = obter_dados_api(parametros)
    salvar_dados_api(dados, nome_inidicador)
