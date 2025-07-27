# pipeline-indicadores-economicos

Este projeto tem como objetivo construir um pipeline de dados baseado na arquitetura de **medalhão (bronze, silver e gold)** para ingestão, transformação, padronização e validação de indicadores econômicos públicos disponibilizados por fontes como **BACEN** e **IBGE**.

---

## Funcionalidades
- Ingestão de dados via APIs públicas do BACEN e IBGE
- Camada Bronze com persistência dos dados crus em JSON
- Camada Silver com dados padronizados, convertidos e validados
- Camada Gold com modelagens finais e datasets prontos
- Validação de dados com Pandera
- Geração de catálogos de dados em YAML

---

## Estrutura do Projeto

```bash
economic-indicators-pipeline/
│
├── config/                                 # Configurações reutilizáveis do projeto
│   ├── constants.py                        # Constantes globais (ex: nomes de indicadores, granularidades)
│   ├── schemas.py                          # Schemas do Pandera para validação dos dados
│   ├── settings.py                         # Caminhos, datas, variáveis de ambiente
│   └── utils.py                            # Funções utilitárias (ex: salvar JSON, formatar datas, logging)
│
├── data/                                   # Diretório de armazenamento dos dados em diferentes camadas
│   ├── bronze/                             # Dados brutos extraídos (sem transformação)
│   ├── silver/                             # Dados tratados (tipos, datas, colunas renomeadas)
│   ├── gold/                               # Dados prontos para análise e consumo
│   └── metrics/                            # Metainformações e validações
│       └── schemas/                        # Schemas YAML exportados (catálogo de dados)
│
├── notebooks/                              # Notebooks de exploração, testes e protótipos
│   └── exploration.ipynb                   # Notebook de exploração de dados e testes locais
│
├── src/                                    # Código-fonte do pipeline
│   ├── ingestion/                          # Módulo responsável pela ingestão de dados externos
│   │   └── bronze_ingestion.py             # Script para coletar e salvar dados na camada bronze
│   ├── transformation/                     # Módulo de transformação dos dados para a camada silver
│   │   └── silver_transformation.py        # Tratamento, renomeações e normalização dos dados
│   └── aggregation/                        # Módulo de agregações e geração da camada gold
│       └── gold_aggregation.py             # Criação de indicadores finais e tabelas analíticas
│
├── requirements.txt                        # Lista de bibliotecas necessárias para executar o projeto
├── main.py                                 # Ponto de entrada do pipeline (executa ingestão, transformação e agregcação)
├── main.py                                 # Ponto de entrada do pipeline (executa ingestão, transformação, agregação)
└── README.md                               # Documentação do projeto com instruções de uso e visão geral

```
---

## Tecnologias
- Python 3.12
- Pandas
- Pandera
- Requests
- YAML
- Loguru
- Jupyter Notebook

---

## Camadas do Projeto
- **Bronze**: Dados brutos da API salvos localmente.
- **Silver**: Dados tratados, padronizados, com colunas renomeadas e datas ajustadas.
- **Gold**: Dados agregados, prontos para análise.

---

## Validação de Dados
A camada `metrics/` contém os esquemas implementado com Panderas:
- Tipos de dados
- Descrições das colunas
- Metadata da tabela
- Serialização com `.yaml`

---

## Como Excecutar

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/economic-indicators-pipeline.git
cd economic-indicators-pipeline

# Instale as dependências 
pip install -r requirements.txt

# Execute o pipeline
python main.py
```
---
