from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from decouple import config
import pandas as pd

def get_engine(user,passw,db,port,host):
    url = f'postgresql+psycopg2://{user}:{passw}@{host}:{port}/{db}'
    if not database_exists(url):
        create_database
    engine = create_engine(url)  
    return engine

def get_connection():
    return get_engine(config('USER_BASE'),
                      config('PASSWORD_BASE'),
                      config('DATABASE'),
                      config('PORT'),
                      config('HOST'))

def load_db(name_table:str):
    try:
        pd.read_sql(name=name_table,con=get_connection())
    except:
        print("No se puede conectar")

