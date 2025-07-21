from typing import LiteralString
from pathlib import Path
import datetime as dt
import os
import pathlib

# Diretório raiz do projeto (um nível acima da pasta 'config')
PROJECT_ROOT: Path = pathlib.Path(__file__).resolve().parents[1]


PATHS: dict[str, str] = {
    #Camaddas do medahão
    "BRONZE_LAYER": os.path.join(PROJECT_ROOT, "data/bronze"),
    "SILVER_LAYER": os.path.join(PROJECT_ROOT, "data/silver"),
    "GOLD_LAYER": os.path.join(PROJECT_ROOT, "data/gold"),
    #Camadas de metricas e logs
    "LOGS": os.path.join(PROJECT_ROOT, "data/logs"),
    "METRICS": os.path.join(PROJECT_ROOT, "data/metrics")
}


