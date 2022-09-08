import boto3
import os
import glob
from decouple import config


secret = config("SECRET_KEY")
access = config("ACCESS_KEY")

def push():
    client = boto3.client('s3', aws_access_key_id= secret,
                    aws_secret_access_key= access)

    response = client.list_buckets()
    if "archivoslimpios" not in response:
        client.create_bucket(Bucket="archivoslimpios")
        
    ficheros = glob.glob('./Normalizados/*')
    n = 0  
    s3 = boto3.resource("s3")
    for i in ficheros:
        direc = os.path.basename(i)
        s3.meta.client.upload_file(i, "archivoslimpios", direc)
        n += 1
        print("{} Archivos subidos".format(n))
