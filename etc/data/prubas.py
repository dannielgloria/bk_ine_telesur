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
df = df.T
print (df)
CALAKMUL = pd.DataFrame(df['CALAKMUL'])
CALAKMUL = CALAKMUL.sort_values('CALAKMUL',ascending=False)
CALAKMUL = CALAKMUL.head().T
CALAKMUL = CALAKMUL.drop(CALAKMUL.columns[[1,2,3,4]], axis='columns')
CALAKMUL = str(CALAKMUL.to_json(orient="index")).replace('{','')
CALAKMUL = CALAKMUL.replace(':"','{"')
CALAKMUL = CALAKMUL.replace('}}','}')
CALAKMUL = CALAKMUL.replace('":','" ')
CALAKMUL = CALAKMUL.replace('"CALAKMUL"{"','"GANADOR":"')
CALAKMUL = CALAKMUL.split()
CALAKMUL = CALAKMUL[0]
CALAKMUL = '"CALAKMUL":{'+CALAKMUL+"}"

CALKINI = pd.DataFrame(df['CALKINI'])
CALKINI = CALKINI.sort_values('CALKINI',ascending=False)
CALKINI = CALKINI.head().T
CALKINI = CALKINI.drop(CALKINI.columns[[1,2,3,4]], axis='columns')
CALKINI = str(CALKINI.to_json(orient="index")).replace('{','')
CALKINI = CALKINI.replace(':"','{"')
CALKINI = CALKINI.replace('}}','}')
CALKINI = CALKINI.replace('":','" ')
CALKINI = CALKINI.replace('"CALKINI"{"','"GANADOR":"')
CALKINI = CALKINI.split()
CALKINI = CALKINI[0]
CALKINI = '"CALKINI":{'+CALKINI+"}"

CAMPECHE = pd.DataFrame(df['CAMPECHE'])
CAMPECHE = CAMPECHE.sort_values('CAMPECHE',ascending=False)
CAMPECHE = CAMPECHE.head().T
CAMPECHE = CAMPECHE.drop(CAMPECHE.columns[[1,2,3,4]], axis='columns')
CAMPECHE = str(CAMPECHE.to_json(orient="index")).replace('{','')
CAMPECHE = CAMPECHE.replace(':"','{"')
CAMPECHE = CAMPECHE.replace('}}','}')
CAMPECHE = CAMPECHE.replace('":','" ')
CAMPECHE = CAMPECHE.replace('"CAMPECHE"{"','"GANADOR":"')
CAMPECHE = CAMPECHE.split()
CAMPECHE = CAMPECHE[0]
CAMPECHE = '"CAMPECHE":{'+CAMPECHE+"}"

CANDELARIA = pd.DataFrame(df['CANDELARIA'])
CANDELARIA = CANDELARIA.sort_values('CANDELARIA',ascending=False)
CANDELARIA = CANDELARIA.head().T
CANDELARIA = CANDELARIA.drop(CANDELARIA.columns[[1,2,3,4]], axis='columns')
CANDELARIA = str(CANDELARIA.to_json(orient="index")).replace('{','')
CANDELARIA = CANDELARIA.replace(':"','{"')
CANDELARIA = CANDELARIA.replace('}}','}')
CANDELARIA = CANDELARIA.replace('":','" ')
CANDELARIA = CANDELARIA.replace('"CANDELARIA"{"','"GANADOR":"')
CANDELARIA = CANDELARIA.split()
CANDELARIA = CANDELARIA[0]
CANDELARIA = '"CANDELARIA":{'+CANDELARIA+"}"

CARMEN = pd.DataFrame(df['CARMEN'])
CARMEN = CARMEN.sort_values('CARMEN',ascending=False)
CARMEN = CARMEN.head().T
CARMEN = CARMEN.drop(CARMEN.columns[[1,2,3,4]], axis='columns')
CARMEN = str(CARMEN.to_json(orient="index")).replace('{','')
CARMEN = CARMEN.replace(':"','{"')
CARMEN = CARMEN.replace('}}','}')
CARMEN = CARMEN.replace('":','" ')
CARMEN = CARMEN.replace('"CARMEN"{"','"GANADOR":"')
CARMEN = CARMEN.split()
CARMEN = CARMEN[0]
CARMEN = '"CARMEN":{'+CARMEN+"}"


CHAMPOTON = pd.DataFrame(df['CHAMPOTON'])
CHAMPOTON = CHAMPOTON.sort_values('CHAMPOTON',ascending=False)
CHAMPOTON = CHAMPOTON.head().T
CHAMPOTON = CHAMPOTON.drop(CHAMPOTON.columns[[1,2,3,4]], axis='columns')
CHAMPOTON = str(CHAMPOTON.to_json(orient="index")).replace('{','')
CHAMPOTON = CHAMPOTON.replace(':"','{"')
CHAMPOTON = CHAMPOTON.replace('}}','}')
CHAMPOTON = CHAMPOTON.replace('":','" ')
CHAMPOTON = CHAMPOTON.replace('"CHAMPOTON"{"','"GANADOR":"')
CHAMPOTON = CHAMPOTON.split()
CHAMPOTON = CHAMPOTON[0]
CHAMPOTON = '"CHAMPOTON":{'+CHAMPOTON+"}"

DZITBALCHE = pd.DataFrame(df['DZITBALCHE'])
DZITBALCHE = DZITBALCHE.sort_values('DZITBALCHE',ascending=False)
DZITBALCHE = DZITBALCHE.head().T
DZITBALCHE = DZITBALCHE.drop(DZITBALCHE.columns[[1,2,3,4]], axis='columns')
DZITBALCHE = str(DZITBALCHE.to_json(orient="index")).replace('{','')
DZITBALCHE = DZITBALCHE.replace(':"','{"')
DZITBALCHE = DZITBALCHE.replace('}}','}')
DZITBALCHE = DZITBALCHE.replace('":','" ')
DZITBALCHE = DZITBALCHE.replace('"DZITBALCHE"{"','"GANADOR":"')
DZITBALCHE = DZITBALCHE.split()
DZITBALCHE = DZITBALCHE[0]
DZITBALCHE = '"DZITBALCHE":{'+DZITBALCHE+"}"

ESCARCEGA = pd.DataFrame(df['ESCARCEGA'])
ESCARCEGA = ESCARCEGA.sort_values('ESCARCEGA',ascending=False)
ESCARCEGA = ESCARCEGA.head().T
ESCARCEGA = ESCARCEGA.drop(ESCARCEGA.columns[[1,2,3,4]], axis='columns')
ESCARCEGA = str(ESCARCEGA.to_json(orient="index")).replace('{','')
ESCARCEGA = ESCARCEGA.replace(':"','{"')
ESCARCEGA = ESCARCEGA.replace('}}','}')
ESCARCEGA = ESCARCEGA.replace('":','" ')
ESCARCEGA = ESCARCEGA.replace('"ESCARCEGA"{"','"GANADOR":"')
ESCARCEGA = ESCARCEGA.split()
ESCARCEGA = ESCARCEGA[0]
ESCARCEGA = '"ESCARCEGA":{'+ESCARCEGA+"}"

HECELCHAKAN = pd.DataFrame(df['HECELCHAKAN'])
HECELCHAKAN = HECELCHAKAN.sort_values('HECELCHAKAN',ascending=False)
HECELCHAKAN = HECELCHAKAN.head().T
HECELCHAKAN = HECELCHAKAN.drop(HECELCHAKAN.columns[[1,2,3,4]], axis='columns')
HECELCHAKAN = str(HECELCHAKAN.to_json(orient="index")).replace('{','')
HECELCHAKAN = HECELCHAKAN.replace(':"','{"')
HECELCHAKAN = HECELCHAKAN.replace('}}','}')
HECELCHAKAN = HECELCHAKAN.replace('":','" ')
HECELCHAKAN = HECELCHAKAN.replace('"HECELCHAKAN"{"','"GANADOR":"')
HECELCHAKAN = HECELCHAKAN.split()
HECELCHAKAN = HECELCHAKAN[0]
HECELCHAKAN = '"HECELCHAKAN":{'+HECELCHAKAN+"}"

PALIZADA = pd.DataFrame(df['PALIZADA'])
PALIZADA = PALIZADA.sort_values('PALIZADA',ascending=False)
PALIZADA = PALIZADA.head().T
PALIZADA = PALIZADA.drop(PALIZADA.columns[[1,2,3,4]], axis='columns')
PALIZADA = str(PALIZADA.to_json(orient="index")).replace('{','')
PALIZADA = PALIZADA.replace(':"','{"')
PALIZADA = PALIZADA.replace('}}','}')
PALIZADA = PALIZADA.replace('":','" ')
PALIZADA = PALIZADA.replace('"PALIZADA"{"','"GANADOR":"')
PALIZADA = PALIZADA.split()
PALIZADA = PALIZADA[0]
PALIZADA = '"PALIZADA":{'+PALIZADA+"}"

SEYBAPLAYA = pd.DataFrame(df['SEYBAPLAYA'])
SEYBAPLAYA = SEYBAPLAYA.sort_values('SEYBAPLAYA',ascending=False)
SEYBAPLAYA = SEYBAPLAYA.head().T
SEYBAPLAYA = SEYBAPLAYA.drop(SEYBAPLAYA.columns[[1,2,3,4]], axis='columns')
SEYBAPLAYA = str(SEYBAPLAYA.to_json(orient="index")).replace('{','')
SEYBAPLAYA = SEYBAPLAYA.replace(':"','{"')
SEYBAPLAYA = SEYBAPLAYA.replace('}}','}')
SEYBAPLAYA = SEYBAPLAYA.replace('":','" ')
SEYBAPLAYA = SEYBAPLAYA.replace('"SEYBAPLAYA"{"','"GANADOR":"')
SEYBAPLAYA = SEYBAPLAYA.split()
SEYBAPLAYA = SEYBAPLAYA[0]
SEYBAPLAYA = '"SEYBAPLAYA":{'+SEYBAPLAYA+"}"

TENABO = pd.DataFrame(df['TENABO'])
TENABO = TENABO.sort_values('TENABO',ascending=False)
TENABO = TENABO.head().T
TENABO = TENABO.drop(TENABO.columns[[1,2,3,4]], axis='columns')
TENABO = str(TENABO.to_json(orient="index")).replace('{','')
TENABO = TENABO.replace(':"','{"')
TENABO = TENABO.replace('}}','}')
TENABO = TENABO.replace('":','" ')
TENABO = TENABO.replace('"TENABO"{"','"GANADOR":"')
TENABO = TENABO.split()
TENABO = TENABO[0]
TENABO = '"TENABO":{'+TENABO+"}"

result = '{'+CALAKMUL+','+CALKINI+','+CAMPECHE+','+CANDELARIA+','+CARMEN+','+CHAMPOTON+','+CHAMPOTON+','+ESCARCEGA+','+HECELCHAKAN+','+PALIZADA+','+SEYBAPLAYA+','+TENABO+'}'
# result = result.replace("'",'"')
# result = json.loads(result)
# result = result.replace("'",'"')
# result = result.replace('}}','}')

#* "XXI":{"PAN_PRI_PRD":2754}
print (result)
# result = df.to_json(orient="index")
# parsed = json.loads(result)
# a = json.dumps(parsed, indent=4)
