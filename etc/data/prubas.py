import requests
import datetime
import zipfile
import json
import os
import pandas as pd
from shutil import rmtree
from pytz import timezone

df = pd.read_csv('./files/20210601_1852_PREP_JUNTAS_CAMP/CAMP_JUNTAS_2021.csv', header=None, sep='\n')
df = df[0].str.split(',', expand=True)
df = df.drop(df.index[[0,1,2,3,4,5]])
df = df.reset_index()

pan = pd.to_numeric(df[16]).sum()
pri = pd.to_numeric(df[17]).sum()
prd = pd.to_numeric(df[18]).sum()
pt = pd.to_numeric(df[19]).sum()
pvem = pd.to_numeric(df[20]).sum()
mc = pd.to_numeric(df[21]).sum()
mor = pd.to_numeric(df[22]).sum()
pes = pd.to_numeric(df[23]).sum()
rsp = pd.to_numeric(df[24]).sum()
fm = pd.to_numeric(df[25]).sum()
pan_pri_prd = pd.to_numeric(df[26]).sum()
pan_pri = pd.to_numeric(df[27]).sum()
pan_prd = pd.to_numeric(df[28]).sum()
pri_prd = pd.to_numeric(df[29]).sum()
no_reg = pd.to_numeric(df[30]).sum()
data = { "PAN":pan,"PRI":pri,"PRD":prd,"PT":pt,"PVEM":pvem,"MC":mc,"MOR":mor,"PES":pes,"RSP":rsp,"FM":fm,"C_PAN_PRI_PRD": pan_pri_prd, "C_PAN_PRI":pan_pri,"C_PAN_PRD": pan_prd, "C_PRI_PRD": pri_prd,"NO_REGISTRADOS": no_reg }
# data = str(data)
result = json.dumps(str(data))
print(data)