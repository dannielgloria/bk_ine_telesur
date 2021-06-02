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
total = df[35].sum()
pan = df[int(16)].sum()
pri = df[17].sum()
prd = df[18].sum()
pt = df[19].sum()
pvem = df[20].sum()
mc = df[21].sum()
mor = df[22].sum()
pes = df[23].sum()
rsp = df[24].sum()
fm = df[25].sum()
pan_pri_prd = df[26].sum()
pan_pri = df[27].sum()
pan_prd = df[28].sum()
pri_prd = df[29].sum()
pt_mor = df[30].sum()
data = { "PAN":pan,"PRI":pri,"PRD":prd,"PT":pt,"PVEM":pvem,"MC":mc,"MOR":mor,"PES":pes,"RSP":rsp,"FM":fm,"C_PAN_PRI_PRD": pan_pri_prd, "C_PAN_PRI":pan_pri,"C_PAN_PRD": pan_prd, "C_PRI_PRD": pri_prd, "C_PT_MOR": pt_mor }
result = json.dumps(data)
# da = df.drop(columns=[0])
print (result)
# df = df.drop(columns=['ID_ESTADO'])
# df = df.set_index('PARTIDO_CI')
# da = df.T

# # print(df)
# # # df = df.drop(columns=['PARTIDO_CI'])
# # print(df)
# # df.drop(['PARTIDO_CI'])
# result = df.to_json()
# print(result)