import datetime as dt
import os
import pathlib


# Diretório raiz do projeto (um nível acima da pasta 'config')
PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]

# Pasta de dados (camadas do Lake)
DATA_ROOT = PROJECT_ROOT / "data"


PATHS = {
    #Camaddas do medahão
    "BRONZE_LAYER": os.path.join(DATA_ROOT, "bronze"),
    "SILVER_LAYER": os.path.join(DATA_ROOT, "silver"),
    "GOLD_LAYER": os.path.join(DATA_ROOT, "gold"),
    #Camadas de metricas e logs
    "LOGS": os.path.join(DATA_ROOT, "logs"),
    "METRICS": os.path.join(DATA_ROOT, "metrics"),

}


