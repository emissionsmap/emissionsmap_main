import pandas as pd

def gases_mundial():
    gases = pd.read_csv('data_warehouse/gases.csv')
    gases.rename(columns={'medios n20':'N2O','medios sf6':'SF6','medios de co2':'CO2','medios canal 4':'CH4'},inplace=True)
    gases.drop(['Id_anio'],axis=1, inplace=True)
    gases = gases[gases.anio >= 1961]
    gases = gases.sort_values('anio')
    gases.reset_index(drop=True, inplace=True)
    gases.reset_index(inplace=True)
    gases.rename(columns={'index':'id'},inplace=True)
    gases.id += 1
    return gases.to_csv('gases_mundial.csv',index=False)

def historico_GHG():
    historico_GHG = pd.read_csv('data_warehouse/historic_emissions.csv')
    historico_GHG.drop(['Idpais','Idcontinente','fuente de datos','sector','gas','unidad'],axis=1, inplace=True)
    historico = historico_GHG.iloc[:,2:23]
    df = pd.DataFrame()
    df['id'] = historico_GHG.codigo
    df['pais'] = historico_GHG.pais
    emisiones = pd.concat([df,historico],axis=1)
    return emisiones.to_csv('emisiones_pais.csv',index=False)

def huella_mundial():
    huella_mundial = pd.read_csv('data_warehouse/huella_biocapacidad.csv')
    huella_mundial.drop(['Id_anio'],axis=1, inplace=True)
    huella_mundial = huella_mundial[huella_mundial.anio >= 1961]
    huella_mundial.drop('poblacion', axis=1, inplace=True)
    huella_mundial.reset_index(drop=True, inplace=True)
    huella_mundial.reset_index(inplace=True)
    huella_mundial.rename(columns={'index':'id'},inplace=True)
    huella_mundial.id += 1
    huella_mundial['tierra'] = round(huella_mundial['tierra'],2)
    return huella_mundial.to_csv('huella_mundial.csv',index=False)

def huella_pais():
    #IDS: indice de desarrollo sostenible
    #ELE: expectativa de vida estimada
    #IDH: indice de desarrollo humano
    huella_pais = pd.read_csv('data_warehouse/huella_sostenible_por_paiss.csv')
    huella_pais.drop(['Idpais','Idcontinente','grupo ingresos'],axis=1, inplace=True)
    huella_pais.rename(columns={'indice objetivos desarrollo sostenible':'IDS',
                        'indice desarrollo humano':'IDH',
                        'expectativa vida':'ELE','pib per capita':'PIB_PerCap'}, inplace=True)
    huella = huella_pais.iloc[:,2:12]
    df = pd.DataFrame()
    df['id'] = huella_pais.codigo
    df['pais'] = huella_pais.pais
    huellapais = pd.concat([df,huella],axis=1)
    return huella_pais.to_csv('huella_pais.csv',index=False)

def temperatura_mundial():
    # MAT: temperatura media anual
    temperatura_mundial = pd.read_csv('data_warehouse/temperatura_anomalia.csv')
    temperatura_mundial.drop(['Id_anio'],axis=1, inplace=True)
    temperatura_mundial.rename(columns={'anomalia la temperatura media promedio 1961 a 1990':'MAT'}, inplace=True)
    temperatura_mundial= temperatura_mundial[temperatura_mundial.anio >= 1961]
    temperatura_mundial.reset_index(drop=True, inplace=True)
    temperatura_mundial.reset_index(inplace=True)
    temperatura_mundial.rename(columns={'index':'id'},inplace=True)
    temperatura_mundial.id += 1
    return temperatura_mundial.to_csv('temperatura_mundial.csv',index=False)

def mundial_maestro():
    huella_mundial = pd.read_csv('data_warehouse/huella_biocapacidad.csv')
    huella_mundial.drop(['Id_anio'],axis=1, inplace=True)
    huella_mundial = huella_mundial[huella_mundial.anio >= 1961]
    mundial_maestro = huella_mundial.iloc[:,:2]
    return mundial_maestro.to_csv('mundial_maestro.csv',index=False)

mundial_maestro()
temperatura_mundial()
huella_mundial()
gases_mundial()