"""
Configurações globais do pipeline, incluindo diretórios, caminhos de dados e bibliotecas compartilhadas.
"""

import os
import pathlib
from pathlib import Path

# Diretório raiz do projeto (um nível acima da pasta 'config')
PROJECT_ROOT: Path = pathlib.Path(__file__).resolve().parents[1]


PATHS: dict[str, str] = {
    #Camaddas do medahão
    "BRONZE_LAYER": os.path.join(PROJECT_ROOT, "data/bronze"),
    "SILVER_LAYER": os.path.join(PROJECT_ROOT, "data/silver"),
    "GOLD_LAYER": os.path.join(PROJECT_ROOT, "data/gold"),
    #Camadas de metricas, schemas e logs
    "LOGS": os.path.join(PROJECT_ROOT, "data/logs"),
    "METRICS": os.path.join(PROJECT_ROOT, "data/metrics"),
    "SCHEMAS": os.path.join(PROJECT_ROOT,"data/metrics/schemas")
}


for path in PATHS.values():
    os.makedirs(path, exist_ok=True)