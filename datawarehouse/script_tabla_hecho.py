import pandas as pd
import numpy as np
import hashlib

def _crearhash(DataFrame):
    for i in DataFrame.columns:
        if i == "pais" or i == "combustible" or i == "anio" or  i == "continente":
            nom = "Id" + i
            if DataFrame[i].dtype == 'int64':
                DataFrame[i] = DataFrame[i].astype(str)
                DataFrame[nom] = DataFrame[i].apply(lambda x:hashlib.md5(x.encode()).hexdigest() if x is not None else x)
                DataFrame[i] = DataFrame[i].astype(int)
            elif DataFrame[i].dtype == 'float64':
                DataFrame[i] = DataFrame[i].astype(str)
                DataFrame[nom] = DataFrame[i].apply(lambda x:hashlib.md5(x.encode()).hexdigest() if x is not None else x)
                DataFrame[i] = DataFrame[i].astype(float)               
            else:
                nom = "Id" + i
                DataFrame[nom] = DataFrame[i].apply(lambda x:hashlib.md5(x.encode()).hexdigest() if x is not None else x)
    return DataFrame

def thecho():
    df1 = pd.read_csv("Normalizados/energiaco2.csv")
    pais = list(df1["pais"].unique())
    continente = list(df1["continente"].unique())


    df3 = pd.read_csv("Normalizados/gases.csv")
    año = list(df3["anio"].unique())

    tipo_ener = ['Biomass',
            'Coal',
            'Cogeneration',
            'Gas',
            'Geothermal',
            'Hydro',
            'Nuclear',
            'Oil',
            'Other',
            'Petcoke',
            'Solar',
            'Storage',
            'Waste',
            'Wave and Tidal',
            'Wind',
            'all_energy_types',
            'natural_gas',
            'petroleum_n_other_liquids',
            'nuclear',
            'renewables_n_other']

    final = {
    "anio":año,
    "pais":pais,
    "combustible":tipo_ener,
    "continente":continente
    }

    df_final = pd.DataFrame.from_dict(final, orient="index")
    df_final = df_final.transpose()

    for i in df_final.columns:
        df_final[i] = df_final[i].apply(lambda x: str(x))


    _crearhash(df_final)

    df_final.to_csv("./Normalizados/Tabla_Hecho.csv", index=False)
