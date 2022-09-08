import pandas as pd
import numpy as np
import hashlib
import csv
import os
from googletrans import Translator
from fuzzywuzzy import fuzz, process
import glob
import pycountry_convert as pc
import re
import unidecode
import warnings
#Encuentra el delimitador de un archivo
def _delimitador (path):
    if path[-4:] == ".txt":
        delimiter = ","
    else:
        data = open(path, "r", encoding="utf-8").read()
        delimiter = csv.Sniffer().sniff(data).delimiter
    return delimiter  

#Genera continente
def continente (nom):
    try:
        country_alpha2 = pc.country_name_to_country_alpha2(nom)
        country_continent = pc.country_alpha2_to_continent_code(country_alpha2)
        continent_name = pc.convert_continent_code_to_continent_name(country_continent)
        return continent_name
    except:
        pass


#Genera  codigo del pais
def iso3 (nom):
    try:
        country_alpha2 = pc.country_name_to_country_alpha3(nom)
        return country_alpha2
    except:
        pass

#saca parentesis de las columnas
def sacarparent(df):
    for i in df.columns:
        text = i
        regEx = re.compile(r'([^\(]*)\([^\)]*\) *(.*)')
        m = regEx.match(text)
        while m:
            text = m.group(1) + m.group(2)
            m = regEx.match(text)
        df.rename(columns={i:text.strip()}, inplace=True)

#quita palabras espesificas de las columnas
def sacarpalabras(df):
    for i in df.columns:
        b = re.sub('twh|consumo|Total|de |otros|geo|-|electricidad|del ', "", i)
        df.rename(columns={i:b.strip()}, inplace=True)

#detecta dotos los archivos de una ruta especifica
def _archivos(path):
    dire = path + "/*/*"
    fiches = glob.glob(dire)
    archivos = []
    directorios = []
    for name in fiches:
        arch = os.path.basename(name)
        if arch[-4:] == ".csv":
            archivos.append(arch)
            directorios.append(name)
    return archivos, directorios


#normaliza columna
def renombracol(data):
    translator = Translator() #metodo de google
    for i in data.columns:
        b = i.replace('_',' ') #Iteracion para cambiar caracter
        data.rename(columns={i:b}, inplace=True) 

    
    #Aqui se concatenan cadenas para formar una sola cadena con todas las vocales que tengan tildes.
    tildes = ("àáâãäåèéêëìíîïòóôõöùúûü")

    # Cada letra aquí corresponde a una vocal acentuada.
    vocales = ("aaaaaaeeeeiiiiooooouuuu")

    # Aqui con el método maketrans relacionamos las dos cadenas antes creadas, esto devuelve un diccionario compatible con el método translate.
    quitatildes = str.maketrans(tildes, vocales)    
       
    for i in data.columns:
        a = translator.translate(i, dest="es").text.lower()
        a = a.translate(quitatildes)
        if a == 'año':
            a = 'anio'
        elif a == "entidad":
            a = "pais"
        data.rename(columns={i: a}, inplace=True) #iterecion para obtenr nombre de columna y traducir
    
    for i in data.columns:
        if i == "sin nombre: 0" or i == "unnamed: 0":
            data.drop(columns=i, inplace=True)
        if i == "poblacion" and len(str(data[i].iloc[5])) > 7:
            data["poblacion"] == round(data["poblacion"] / 100000000, 2)
        if len(i) >= 25:
            sacarpalabras(data)
    
    for i in data.columns:
        if data[i].dtype == "O":
            data[i] = data[i].str.replace(',', '.')

    if "pais" in data.columns and "continente" not in data.columns:
        data.insert(loc=1, column="continente", value=data["pais"].apply(lambda x: continente(x)))
    
    if "codigo" not in data.columns and "pais" in data.columns:
        data.insert(loc=1, column="codigo", value=data["pais"].apply(lambda x: iso3(x)))
        data = data[data["codigo"].isna() == False]

    sacarparent(data)

    return data

#crea columna ID con hash
def _crearhash(DataFrame):
    for i in DataFrame.columns:
        if i == "pais" or i == "combustible" or i == "anio" or  i == "continente":
            nom = "Id_" + i
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


#limpieza de la tabla energyco2
def _limpieza_energy (df):

    df.dropna(subset=["emision co2"], inplace=True)

    for i in df.columns:
        if i == "tipo energia":
            df.rename(columns={i:"combustible"}, inplace=True)
        elif "energ" in i:
            nom = i + " " + "twh"
            df[nom] = df[i] / 3.412e+12
    df["poblacion"] = round(df["poblacion"] / 1000)
    return df


#corre la limpieza
def dataFrame (root):
    archivos, rutas = _archivos(root)
    os.mkdir("Normalizados")
    n = 0
    for i in rutas:
        for e in archivos:
            if e in i:
                if e == "energyco2.csv":
                    deli = _delimitador(i)
                    translator = Translator()
                    nombre = translator.translate(e, dest="es").text
                    df = pd.read_csv(i, delimiter=deli, low_memory=False)
                    df = renombracol(df)
                    df = _limpieza_energy(df)                    
                    df = _crearhash(df)
                    salida = "./Normalizados/" + nombre
                    df.to_csv(salida, index=False)
                    n+=1
                    print("{} Archivo Normalizado".format(n))
                    warnings.filterwarnings('ignore')

                else:
                    deli = _delimitador(i)
                    translator = Translator()
                    nombre = translator.translate(e, dest="es").text
                    nombre = unidecode.unidecode(nombre).lower()
                    df = pd.read_csv(i, delimiter=deli, low_memory=False, on_bad_lines="skip")
                    df = renombracol(df)
                    df = _crearhash(df)
                    salida = "./Normalizados/" + nombre
                    df.to_csv(salida, index=False)
                    n+=1
                    print("{} Archivo Normalizado".format(n))
        
