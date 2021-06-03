import requests
import datetime
import zipfile
import json
import os
import pandas as pd
from shutil import rmtree
from pytz import timezone

df = pd.read_csv('./files/20210601_1852_PREP_GOB_CAMP/CAMP_GOB_CANDIDATURA_2021.csv')
df = df.drop(columns=['ID_ESTADO'])
df = df.set_index('PARTIDO_CI')
result = str(df.to_json())
result=result.replace('{"CANDIDATURA_PROPIETARIA":', '')
result=result.replace('"}}', '"}')
print (df)
print (result)