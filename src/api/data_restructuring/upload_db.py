import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
import os
import pandas as pd
from decouple import config

user = config('USER_BASE')
passw = config('PASSWORD_BASE')
host = config('HOST')
database = config('DATABASE')

def baseDeDatos (df, tabla):
    try:
        conex = create_engine("postgresql+psycopg2://{}:{}@{}/{}".format(user,passw,host,database))
        conexpostgres = conex.connect()
        metadatas = sqlalchemy.MetaData()
        df.to_sql(tabla, conexpostgres, if_exists="append", index=False)
        return "Tabla subida"
    except Exception as ex:
        return ex

def upload ():
    with os.scandir("./data") as ficheros:
        n = 0
        for i in ficheros:
            dir= "./data/" + i.name
            df = pd.read_csv(dir)
            baseDeDatos(df, i.name[:-4])
            n+=1
            print("{} Archivos subidos a la base de datos".format(n))
        print("Todos los archivos se subieron correctamente")

upload()