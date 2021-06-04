import requests
import datetime
import zipfile
import json
import os
import pandas as pd
from shutil import rmtree
from pytz import timezone

df = pd.read_csv('./files/20210601_1852_PREP_AYUN_CAMP/CAMP_AYUN_2021.csv', header=None, sep='\n')
df = df[0].str.split(',', expand=True)
df = df.drop(df.index[[0,1,2,3,4,5]])
df = df.reset_index()
# df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')
# print (co)
# df = pd.to_numeric(df[16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34])
# cols = df.columns.drop(5)
df = df.drop(['index', 0, 1,2,3,4,6,7,8,9,10,11,12,13,14,15,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46], axis=1)
cols = df.columns.drop(5)
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')
df = df.groupby([5]).agg(
    {16:'sum',
     17:'sum',
     18:'sum',
     19:'sum',
     20:'sum',
     21:'sum',
     22:'sum',
     23:'sum',
     24:'sum',
     25:'sum',
     26:'sum',
     27:'sum',
    }).reset_index()
df = df.rename(columns={
    5: 'MUNICIPIO',
    16:'PAN',
    17:'PRI',
    18:'PRD',
    19:'PT',
    20:'PVEM',
    21:'MC',
    22:'MOR',
    23:'PES',
    24:'RSP',
    25:'FM',
    26:'CI-1',
    27:'PAN_PRI_PRD_a',
})
df = df.rename(index={0: 'CALAKMUL',1: 'CALKINI',2: 'CAMPECHE',3: 'CANDELARIA',4: 'CARMEN',5: 'CHAMPOTON',6: 'DZITBALCHE',7: 'ESCARCEGA',8: 'HECELCHAKAN',9: 'HOPELCHEN',10: 'PALIZADA',11: 'SEYBAPLAYA',12: 'TENABO'})
rc = ['PAN','PRI','PRD','PAN_PRI_PRD_a']
df['PAN_PRI_PRD'] = df[rc].sum(axis=1)
df = df.drop(['MUNICIPIO','PAN','PRI','PRD','PAN_PRI_PRD_a'], axis=1)
result = df.to_json(orient="index")
parsed = json.loads(result)
a = json.dumps(parsed, indent=4)
print (a)
