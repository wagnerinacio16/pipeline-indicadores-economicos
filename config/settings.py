import datetime as dt
import os
import pathlib


DATA_ROOT = str(pathlib.Path('data').resolve())



PATHS = {
    #Camaddas do medahão
    "BRONZE_LAYER": os.path.join(DATA_ROOT, "bronze"),
    "SILVER_LAYER": os.path.join(DATA_ROOT, "silver"),
    "GOLD_LAYER": os.path.join(DATA_ROOT, "gold"),
    #Camadas de metricas e logs
    "LOGS": os.path.join(DATA_ROOT, "logs"),
    "METRICS": os.path.join(DATA_ROOT, "metrics"),

}


