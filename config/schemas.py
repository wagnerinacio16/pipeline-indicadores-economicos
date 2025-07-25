"""
Schemas Pandera para validação dos indicadores econômicos do pipeline.
"""

import pandera.pandas as pa
from config.constants import *

data_inicial = dt.datetime.strptime(DATA_INICIAL, "%d/%m/%Y")
data_final = dt.datetime.strptime(DATA_FINAL, "%d/%m/%Y")

schema_ars_brl = pa.DataFrameSchema(
    name="ARS_BRL",
    description="Tabela contendo a série histórica da taxa de câmbio diária entre o Peso Argentino (ARS) e o Real Brasileiro (BRL), disponibilizada pelo Banco Central do Brasil (BACEN).",
    columns={
        "data": pa.Column(
            pa.DateTime,
            nullable=False,
            unique=True,
            checks=[pa.Check.in_range(data_inicial, data_final)],
            description="Data da cotação da taxa de câmbio ARS/BRL. Formato YYYY-MM-DD.",
        ),
        "ars_brl": pa.Column(
            pa.Float,
            nullable=False,
            checks=pa.Check.greater_than(0),
            description="Valor da taxa de câmbio do Peso Argentino (ARS) para o Real (BRL).",
        ),
    },
)

schema_ipca = pa.DataFrameSchema(
    name="IPCA",
    description="Índice de Preços ao Consumidor Amplo (IBGE). Série histórica mensal.",
    columns={
        "data": pa.Column(
            pa.DateTime,
            nullable=False,
            unique=True,
            checks=[pa.Check.in_range(data_inicial, data_final)],
            description="Data da observação. Formato YYYY-MM-DD.",
        ),
        "ipca": pa.Column(
            pa.Float,
            nullable=False,
            checks=pa.Check.greater_than(0),
            description="Valor do IPCA.",
        ),
    },
)

schema_selic_meta = pa.DataFrameSchema(
    name="SELIC_META",
    description="Taxa Selic Meta (BACEN). Série histórica diária.",
    columns={
        "data": pa.Column(
            pa.DateTime,
            nullable=False,
            unique=True,
            checks=[pa.Check.in_range(data_inicial, data_final)],
            description="Data da observação. Formato YYYY-MM-DD.",
        ),
        "selic_meta": pa.Column(
            pa.Float,
            nullable=False,
            checks=pa.Check.greater_than(0),
            description="Valor da taxa Selic Meta.",
        ),
    },
)

schema_eur_brl = pa.DataFrameSchema(
    name="EUR_BRL",
    description="Tabela contendo a série histórica da taxa de câmbio diária entre o Euro (EUR) e o Real Brasileiro (BRL), disponibilizada pelo Banco Central do Brasil (BACEN).",
    columns={
        "data": pa.Column(
            pa.DateTime,
            nullable=False,
            unique=True,
            checks=[pa.Check.in_range(data_inicial, data_final)],
            description="Data da cotação da taxa de câmbio EUR/BRL. Formato YYYY-MM-DD.",
        ),
        "eur_brl": pa.Column(
            pa.Float,
            nullable=False,
            checks=pa.Check.greater_than(0),
            description="Valor da taxa de câmbio do Euro (EUR) para o Real (BRL).",
        ),
    },
)

schema_usd_brl = pa.DataFrameSchema(
    name="USD_BRL",
    description="Tabela contendo a série histórica da taxa de câmbio diária entre o Dólar Americano (USD) e o Real Brasileiro (BRL), disponibilizada pelo Banco Central do Brasil (BACEN).",
    columns={
        "data": pa.Column(
            pa.DateTime,
            nullable=False,
            unique=True,
            checks=[pa.Check.in_range(data_inicial, data_final)],
            description="Data da cotação da taxa de câmbio USD/BRL. Formato YYYY-MM-DD.",
        ),
        "usd_brl": pa.Column(
            pa.Float,
            nullable=False,
            checks=pa.Check.greater_than(0),
            description="Valor da taxa de câmbio do Dólar Americano (USD) para o Real (BRL).",
        ),
    },
)

schema_ibc_br = pa.DataFrameSchema(
    name="IBC_BR",
    description="Índice de Atividade Econômica do Banco Central (IBC-BR). Série histórica mensal.",
    columns={
        "data": pa.Column(
            pa.DateTime,
            nullable=False,
            unique=True,
            checks=[pa.Check.in_range(data_inicial, data_final)],
            description="Data da observação. Formato YYYY-MM-DD.",
        ),
        "ibc_br": pa.Column(
            pa.Float,
            nullable=False,
            checks=pa.Check.greater_than(0),
            description="Valor do índice IBC-BR.",
        ),
    },
)

schema_inadimplencia_pf = pa.DataFrameSchema(
    name="INADIMPLENCIA_PF",
    description="Índice de inadimplência de pessoas físicas. Série histórica mensal.",
    columns={
        "data": pa.Column(
            pa.DateTime,
            nullable=False,
            unique=True,
            checks=[pa.Check.in_range(data_inicial, data_final)],
            description="Data da observação. Formato YYYY-MM-DD.",
        ),
        "inadimplencia_pf": pa.Column(
            pa.Float,
            nullable=False,
            checks=pa.Check.greater_than_or_equal_to(0),
            description="Índice de inadimplência de pessoas físicas.",
        ),
    },
)

schema_chf_brl = pa.DataFrameSchema(
    name="CHF_BRL",
    description="Tabela contendo a série histórica da taxa de câmbio diária entre o Franco Suíço (CHF) e o Real Brasileiro (BRL), disponibilizada pelo Banco Central do Brasil (BACEN).",
    columns={
        "data": pa.Column(
            pa.DateTime,
            nullable=False,
            unique=True,
            checks=[pa.Check.in_range(data_inicial, data_final)],
            description="Data da cotação da taxa de câmbio CHF/BRL. Formato YYYY-MM-DD.",
        ),
        "chf_brl": pa.Column(
            pa.Float,
            nullable=False,
            checks=pa.Check.greater_than(0),
            description="Valor da taxa de câmbio do Franco Suíço (CHF) para o Real (BRL).",
        ),
    },
)

schema_cny_brl = pa.DataFrameSchema(
    name="CNY_BRL",
    description="Tabela contendo a série histórica da taxa de câmbio diária entre o Yuan Chinês (CNY) e o Real Brasileiro (BRL), disponibilizada pelo Banco Central do Brasil (BACEN).",
    columns={
        "data": pa.Column(
            pa.DateTime,
            nullable=False,
            unique=True,
            checks=[pa.Check.in_range(data_inicial, data_final)],
            description="Data da cotação da taxa de câmbio CNY/BRL. Formato YYYY-MM-DD.",
        ),
        "cny_brl": pa.Column(
            pa.Float,
            nullable=False,
            checks=pa.Check.greater_than(0),
            description="Valor da taxa de câmbio do Yuan Chinês (CNY) para o Real (BRL).",
        ),
    },
)

schema_gbp_brl = pa.DataFrameSchema(
    name="GBP_BRL",
    description="Tabela contendo a série histórica da taxa de câmbio diária entre a Libra Esterlina (GBP) e o Real Brasileiro (BRL), disponibilizada pelo Banco Central do Brasil (BACEN).",
    columns={
        "data": pa.Column(
            pa.DateTime,
            nullable=False,
            unique=True,
            checks=[pa.Check.in_range(data_inicial, data_final)],
            description="Data da cotação da taxa de câmbio GBP/BRL. Formato YYYY-MM-DD.",
        ),
        "gbp_brl": pa.Column(
            pa.Float,
            nullable=False,
            checks=pa.Check.greater_than(0),
            description="Valor da taxa de câmbio da Libra Esterlina (GBP) para o Real (BRL).",
        ),
    },
)

schema_jpy_brl = pa.DataFrameSchema(
    name="JPY_BRL",
    description="Tabela contendo a série histórica da taxa de câmbio diária entre o Iene Japonês (JPY) e o Real Brasileiro (BRL), disponibilizada pelo Banco Central do Brasil (BACEN).",
    columns={
        "data": pa.Column(
            pa.DateTime,
            nullable=False,
            unique=True,
            checks=[pa.Check.in_range(data_inicial, data_final)],
            description="Data da cotação da taxa de câmbio JPY/BRL. Formato YYYY-MM-DD.",
        ),
        "jpy_brl": pa.Column(
            pa.Float,
            nullable=False,
            checks=pa.Check.greater_than(0),
            description="Valor da taxa de câmbio do Iene Japonês (JPY) para o Real (BRL).",
        ),
    },
)

schema_desemprego = pa.DataFrameSchema(
    name="DESEMPREGO",
    description="Taxa de desemprego. Série histórica mensal.",
    columns={
        "data": pa.Column(
            pa.DateTime,
            nullable=False,
            unique=True,
            checks=[pa.Check.in_range(data_inicial, data_final)],
            description="Data da observação. Formato YYYY-MM-DD.",
        ),
        "desemprego": pa.Column(
            pa.Float,
            nullable=False,
            checks=pa.Check.greater_than_or_equal_to(0),
            description="Taxa de desemprego.",
        ),
    },
)
