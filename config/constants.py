from config.settings import * 

DATA_FINAL = dt.datetime.now().strftime('%d/%m/%Y')
DATA_INICIAL = dt.datetime.now().replace(year=dt.datetime.now().year-10).strftime('%d/%m/%Y')

API = {
    "IBGE": {
        "FONTE":"IBGE",
        "URL":"https://servicodados.ibge.gov.br/api/v3/agregados"},

    "BACEN": {
        "FONTE":"BACEN",
        "URL": "https://api.bcb.gov.br/dados/serie/bcdata.sgs."
    }
}

PARAMETROS = {
    "IBGE": {
        "IPCA": {
            "AGREGADO": "7060",
            "VARIAVEL": "63",
        },

        "DESEMPREGO": {
            "AGREGADO": "4099",
            "VARIAVEL": "4099",
        },
    },

    "BACEN": {
        "SELIC_META": "432",
        "IBC_BR": "24363",
        "INADIMPLENCIA_PF": "20710",
        #COTACAO CAMBIO
        "USD_BRL": "1",       #Dolar Americano
        "EUR_BRL": "21619",   #Euro
        "GBP_BRL": "21623",   #Libra Esterlina
        "JPY_BRL": "21620",   #Iene Japones
        "ARS_BRL": "21622",   #Peso Argentino
        "CHF_BRL": "21621",   #Franco Suico
        "CNY_BRL": "21627"    #Yuan Chines
    }
}


INDICADORES = {
    "IPCA": {
        "NOME": "Índice Nacional de Preços ao Consumidor Amplo (IPCA)",
        "CATEGORIA": "INFLACAO",
        "FONTE": API["IBGE"]["FONTE"],
        "GRANULARIDADE": "MENSAL",
        "URL": str(f"{API['IBGE']['URL']}/{PARAMETROS['IBGE']['IPCA']['AGREGADO']}/periodos/all/variaveis/{PARAMETROS['IBGE']['IPCA']['VARIAVEL']}?localidades=N1[all]")
    },
    "SELIC_META": {
        "NOME": "Taxa Selic Meta",
        "CATEGORIA": "JUROS",
        "FONTE": API["BACEN"]["FONTE"],
        "GRANULARIDADE": "MENSAL",
        "URL": str(f"{API['BACEN']['URL']}{PARAMETROS['BACEN']['SELIC_META']}/dados?formato=json&dataInicial={DATA_INICIAL}&dataFinal={DATA_FINAL}")
    },
    "IBC_BR": {
        "NOME": "Índice de Atividade Econômica do Banco Central (IBC-Br)",
        "CATEGORIA": "atividade_economica",
        "FONTE": API["BACEN"]["FONTE"],
        "GRANULARIDADE": "MENSAL",
        "URL": str(f"{API['BACEN']['URL']}{PARAMETROS['BACEN']['IBC_BR']}/dados?formato=json&dataInicial={DATA_INICIAL}&dataFinal={DATA_FINAL}")
    },
    "DESEMPREGO": {
        "NOME": "Taxa de Desemprego",
        "CATEGORIA": "MERCADO_TRABALHO",
        "FONTE": API['IBGE']['FONTE'],
        "GRANULARIDADE": "MENSAL",
        "URL": str(f"{API['IBGE']['URL']}/{PARAMETROS['IBGE']['DESEMPREGO']['AGREGADO']}/periodos/all/variaveis/{PARAMETROS['IBGE']['DESEMPREGO']['VARIAVEL']}?localidades=N1[all]")
    },
    "INADIMPLENCIA_PF": {
        "NOME": "Inadimplência Pessoa Física",
        "CATEGORIA": "CREDITO_CONSUMO",
        "FONTE": "BACEN",
        "GRANULARIDADE": "MENSAL",
        "URL": str(f"{API['BACEN']['URL']}{PARAMETROS['BACEN']['INADIMPLENCIA_PF']}/dados?formato=json&dataInicial={DATA_INICIAL}&dataFinal={DATA_FINAL}")
    },
    #Cotação Moedas
    "ARS_BRL":{
        "NOME": "Cotação Peso Argentino",
        "FONTE": API['BACEN']['FONTE'],
        "GRANULARIDADE": "DIARIA",
        "URL": str(f"{API['BACEN']['URL']}{PARAMETROS['BACEN']['ARS_BRL']}/dados?formato=json&dataInicial={DATA_INICIAL}&dataFinal={DATA_FINAL}")
    },
    "USD_BRL":{
        "NOME": "Cotação Dolór Americano",
        "FONTE": API['BACEN']['FONTE'],
        "GRANULARIDADE": "DIARIA",
        "URL": str(f"{API['BACEN']['URL']}{PARAMETROS['BACEN']['USD_BRL']}/dados?formato=json&dataInicial={DATA_INICIAL}&dataFinal={DATA_FINAL}")
    },
    "EUR_BRL":{
        "NOME": "Cotação Euro",
        "FONTE": API['BACEN']['FONTE'],
        "GRANULARIDADE": "DIARIA",
        "URL": str(f"{API['BACEN']['URL']}{PARAMETROS['BACEN']['EUR_BRL']}/dados?formato=json&dataInicial={DATA_INICIAL}&dataFinal={DATA_FINAL}")
    },
    "GBP_BRL":{
        "NOME": "Cotação Libra Esterlina",
        "FONTE": API['BACEN']['FONTE'],
         "GRANULARIDADE": "DIARIA",
        "URL": str(f"{API['BACEN']['URL']}{PARAMETROS['BACEN']['GBP_BRL']}/dados?formato=json&dataInicial={DATA_INICIAL}&dataFinal={DATA_FINAL}")
    },
    "JPY_BRL":{
        "NOME": "Cotação Iêne Japones",
        "FONTE": API['BACEN']['FONTE'],
        "GRANULARIDADE": "DIARIA",
        "URL": str(f"{API['BACEN']['URL']}{PARAMETROS['BACEN']['JPY_BRL']}/dados?formato=json&dataInicial={DATA_INICIAL}&dataFinal={DATA_FINAL}")
    },
    "CHF_BRL":{
        "NOME": "Cotação Franco Suíço",
        "FONTE": API['BACEN']['FONTE'],
        "GRANULARIDADE": "DIARIA",
        "URL": str(f"{API['BACEN']['URL']}{PARAMETROS['BACEN']['CHF_BRL']}/dados?formato=json&dataInicial={DATA_INICIAL}&dataFinal={DATA_FINAL}")
    },
    "CNY_BRL":{
        "NOME": "Cotação Yan Chinês",
        "FONTE": API['BACEN']['FONTE'],
        "GRANULARIDADE": "DIARIA",
        "URL": str(f"{API['BACEN']['URL']}{PARAMETROS['BACEN']['CNY_BRL']}/dados?formato=json&dataInicial={DATA_INICIAL}&dataFinal={DATA_FINAL}")
    }
    
}

