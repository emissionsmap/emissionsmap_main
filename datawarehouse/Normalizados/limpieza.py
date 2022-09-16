import pandas as pd

def gases():
    gases = pd.read_csv('gases.csv')
    gases.rename(columns={'medios n20':'N2O','medios sf6':'SF6','medios de co2':'CO2','medios canal 4':'CH4'},inplace=True)
    gases.drop(['Id_anio'],axis=1, inplace=True)
    gases.sort_values('anio')
    return gases.to_csv('gases2.csv',index=False)

def historico_GHG():
    #unidades en millones de toneladas métricas de equivalente de dióxido de carbono (MTCO₂e)
    historico_GHG = pd.read_csv('historic_emissions.csv')
    historico_GHG.drop(['Idpais','Idcontinente','fuente de datos','sector','gas','unidad'],axis=1, inplace=True)
    return historico_GHG.to_csv('historico_GHG.csv',index=False)

def huella_mundial():
    huella_mundial = pd.read_csv('huella_biocapacidad.csv')
    huella_mundial.drop(['Id_anio'],axis=1, inplace=True)
    return huella_mundial.to_csv('huella_mundial.csv',index=False)

def huella_pais():
    #IDS: indice de desarrollo sostenible
    #ELE: expectativa de vida estimada
    #IDH: indice de desarrollo humano
    huella_pais = pd.read_csv('huella_sostenible_por_paiss.csv')
    huella_pais.drop(['Idpais','Idcontinente','grupo ingresos'],axis=1, inplace=True)
    huella_pais.rename(columns={'indice objetivos desarrollo sostenible':'IDS',
                        'indice desarrollo humano':'IDH',
                        'expectativa vida':'ELE','pib per capita':'PIB_PerCap'}, inplace=True)
    return huella_pais.to_csv('huella_pais.csv',index=False)

def temperatura_mundial():
    # MAT: temperatura media anual
    temperatura_mundial = pd.read_csv('temperatura_anomalia.csv')
    temperatura_mundial.drop(['Id_anio'],axis=1, inplace=True)
    temperatura_mundial.rename(columns={'anomalia la temperatura media promedio 1961 a 1990':'MAT'}, inplace=True)
    return temperatura_mundial.to_csv('temperatura_mundial.csv',index=False)

gases()
historico_GHG()
huella_mundial()
huella_pais()
temperatura_mundial()