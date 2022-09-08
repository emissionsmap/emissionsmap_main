import glob 
import boto3
import os
import glob
from decouple import config

secret = config("SECRET_KEY")
access = config("ACCESS_KEY")

def pushS3():
    client = boto3.client('s3', aws_access_key_id=access,
                    aws_secret_access_key=secret)

    client.create_bucket(Bucket="archivossucios")

    ficheros = glob.glob('./data/*')
    n=0
    s3 = boto3.resource("s3")
    for i in ficheros:
        Key = os.path.basename(i)
        s3.meta.client.upload_file(i, "archivossucios", Key)
        n += 1
        print("{} Archivos subidos a S3".format(n))
    print("Todos los archivos fueron subidos a S3")

if __name__ == "__main__":
  pushS3()
