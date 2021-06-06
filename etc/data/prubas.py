import requests
import datetime
import zipfile
import json
import os
import pandas as pd
from shutil import rmtree
from pytz import timezone

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