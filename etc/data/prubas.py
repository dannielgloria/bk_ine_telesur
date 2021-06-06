import requests
import datetime
import zipfile
import json
import os
import pandas as pd
from shutil import rmtree
from pytz import timezone

# content = os.listdir('./etc/data/files')
# content = os.listdir('./files')
# cambio _ por espacios
#
# * 20210601_1852_
# !print(os.listdir("./files/"))
# !for filename in os.listdir("./files/"):
# !    if filename.startswith("FILE"):
# !        os.rename(filename, filename[14:])
# !        print(os.listdir("./files"))
# # os.rename(filename, filename[:])
# !print(os.listdir("./files"))


# os.remove('./files/.DS_Store')
carpeta = os.listdir("./files/")
dirname = carpeta[0] 
dirname =  dirname[:14]
dirname2 = carpeta[2] 
dirname2 =  dirname2[:14]
dirname3 = carpeta[1] 
dirname3 =  dirname3[:14]
if (dirname != dirname2):
    print('si fue distinto')
    dirname = dirname3
else:
    print('no fue distinto')
    dirname = dirname3
    
print (dirname)


# import os
# archivo = "/home/decodigo/Documentos/python/archivos/archivo.txt"
# nombre_nuevo = "/home/decodigo/Documentos/python/archivos/archivo_renombrado.txt"
# os.rename(archivo, nombre_nuevo)

# content
# https://difusores.prep2021-cam.mx/assets/entregables/55/1/20210601_1852_PREP_CAMP.zip

# df = pd.read_csv('./files/20210601_1852_PREP_DIP_LOC_CAMP/CAMP_DIP_LOC_2021.csv', header=None, sep='\n')
# df = df[0].str.split(',', expand=True)
# df = df.reset_index()
# result = str(df.loc[1,0]).replace(' (UTC-5)', '') 
# result = result.replace('/',' ')
# result = result.split()
# result = 'Junio ' + result[0] + '  ' + result[3]
# print (result)
# result = {'hora':result}
# result = str(result)
# result=result.replace("'", '"')
# print (result)