from script_tabla_hecho import thecho
from script_Limpieza import dataFrame
from postgres_upload import upload
from uploadS3 import push


import os
def main ():
    try:
        direc = os.getcwd()
        if "Normalizados" not in os.listdir(direc):
            dataFrame(direc)
            thecho()
        upload()
        push()
        print("TERMINADO")
    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    main()
    
