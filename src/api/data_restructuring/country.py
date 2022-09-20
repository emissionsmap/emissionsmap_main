import pandas as pd
import geopandas as gpd

def pais():
    geojson1 = gpd.read_file('data_warehouse/world.geojson')
    df_pais = pd.DataFrame()
    df_pais['id'] = geojson1.ISO_A3
    df_pais['pais'] = geojson1.NAME_LONG
    # df_pais.to_csv('pais_maestro.csv',index=False)
    return df_pais

def tabla_owid():
    df = pd.read_csv('data_warehouse/owid-energy-consumption-source.csv')
    new = df[['iso_code','year','population','gdp','carbon_intensity_elec','electricity_generation','electricity_demand',
        'oil_electricity','oil_consumption','coal_electricity','coal_consumption','gas_electricity',
        'gas_consumption','nuclear_electricity','nuclear_consumption','hydro_electricity','hydro_consumption',
        'solar_electricity','solar_consumption','wind_electricity','wind_consumption','other_renewable_electricity',
        'other_renewable_consumption']]
    codigo_pais = pais().rename(columns={'id':'iso_code'})
    df_new = pd.merge(codigo_pais,new,how='left',on='iso_code')
    df= df_new[df_new.year >= 2000]
    return df

def informacion():
    df = tabla_owid()
    df = df[['iso_code','year','population','gdp','electricity_generation','electricity_demand']]
    df.reset_index(drop=True, inplace=True)
    df.reset_index(inplace=True)
    df.rename(columns={'index':'id','year':'anio','population':'poblacion','gdp':'pbi','electricity_generation':'gen_elect',
            'electricity_demand':'dem_elect','iso_code':'pais_id',}, inplace=True)
    df.id += 1 
    return df

def consumo():
    df = tabla_owid()
    df_consumo = df[['iso_code','year','oil_consumption','coal_consumption','gas_consumption',
    'nuclear_consumption','hydro_consumption','solar_consumption','wind_consumption','other_renewable_consumption']].copy()
    df_consumo.rename(columns={'year':'anio','oil_consumption':'petroleo','coal_consumption':'carbon','gas_consumption':'gas',
        'nuclear_consumption':'nuclear','hydro_consumption':'hidraulica','solar_consumption':'solar',
        'wind_consumption':'eolica','other_renewable_consumption':'otras_renovables'},inplace=True)
    df_consumo.reset_index(drop=True,inplace=True)
    df_consumo.reset_index(inplace=True)
    df_consumo.rename(columns={'index':'informacion_id','iso_code':'codigo'},inplace=True)
    df_consumo.informacion_id += 1
    df_consumo.reset_index(inplace=True)
    df_consumo.rename(columns={'index':'id','iso_code':'codigo'},inplace=True)
    df_consumo.id += 1
    return df_consumo.to_csv('consumo_pais.csv',index=False)


def produccion():
    df = tabla_owid()
    df_produccion = df[['year','iso_code','oil_electricity','coal_electricity','gas_electricity',
    'nuclear_electricity','hydro_electricity','solar_electricity','wind_electricity','other_renewable_electricity']].copy()
    df_produccion.rename(columns={'iso_code':'codigo','year':'anio','oil_electricity':'petroleo','coal_electricity':'carbon','gas_electricity':'gas',
        'nuclear_electricity':'nuclear','hydro_electricity':'hidraulica','solar_electricity':'solar',
        'wind_electricity':'eolica','other_renewable_electricity':'otras_renovables'},inplace=True)
    df_produccion.reset_index(drop=True,inplace=True)
    df_produccion.reset_index(inplace=True)
    df_produccion.rename(columns={'index':'informacion_id','iso_code':'codigo'},inplace=True)
    df_produccion.informacion_id += 1
    df_produccion.reset_index(inplace=True)
    df_produccion.rename(columns={'index':'id','iso_code':'codigo'},inplace=True)
    df_produccion.id += 1
    return df_produccion.to_csv('produccion_pais.csv',index=False)
