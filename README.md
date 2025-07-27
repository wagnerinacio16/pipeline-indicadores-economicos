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
├── notebooks/              # Notebooks exploratórios e scripts de testes
├── src/                    # Código fonte do pipeline
│   ├── ingestion/          # Ingestão de dados (APIs públicas)
│   ├── transformation/     # Limpeza, padronização e enriquecimento (camada Silver)
│   └── gold/               # Modelagem e estrutura final de consumo (camada Gold)
│
├── config/                 # Configurações gerais (paths, constantes, schemas)
├── data/                   # Dados divididos por camadas
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── metrics/                # Schemas de validação e metadados com Pandera
├── requirements.txt        # Bibliotecas necessárias
├── .gitignore              # Arquivos a serem ignorados pelo Git
└── README.md               # Documentação do projeto

```

## Tecnologias
- Python 3.12
- Pandas
- Pandera
- Requests
- YAML
- Loguru
- Jupyter Notebook

## Camadas do Projeto
- **Bronze**: Dados brutos da API salvos localmente.
- **Silver**: Dados tratados, padronizados, com colunas renomeadas e datas ajustadas.
- **Gold**: Dados agregados, prontos para análise.

## Validação de Dados
A camada `metrics/` contém os esquemas implementado com Panderas:
- Tipos de dados
- Descrições das colunas
- Metadata da tabela
- Serialização com `.yaml`

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