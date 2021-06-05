import requests
import datetime
import zipfile
import json
import os
import pandas as pd
from shutil import rmtree
from pytz import timezone

# df = pd.read_csv('./files/20210601_1852_PREP_AYUN_CAMP/CAMP_AYUN_2021.csv', header=None, sep='\n')
# df = df[0].str.split(',', expand=True)
# df = df.drop(df.index[[0,1,2,3,4,5]])
# df = df.reset_index()
# df = df.drop(['index', 0, 1,2,3,4,6,7,8,9,10,11,12,13,14,15,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46], axis=1)
# cols = df.columns.drop(5)
# df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')
# df = df.groupby([5]).agg(
# {16:'sum',
# 17:'sum',
# 18:'sum',
# 19:'sum',
# 20:'sum',
# 21:'sum',
# 22:'sum',
# 23:'sum',
# 24:'sum',
# 25:'sum',
# 26:'sum',
# 27:'sum',
# }).reset_index()
# df = df.rename(columns={
# 5: 'MUNICIPIO',
# 16:'PAN',
# 17:'PRI',
# 18:'PRD',
# 19:'PT',
# 20:'PVEM',
# 21:'MC',
# 22:'MOR',
# 23:'PES',
# 24:'RSP',
# 25:'FM',
# 26:'CI-1',
# 27:'PAN_PRI_PRD_a',
# })
# df = df.rename(index={0: 'CALAKMUL',1: 'CALKINI',2: 'CAMPECHE',3: 'CANDELARIA',4: 'CARMEN',5: 'CHAMPOTON',6: 'DZITBALCHE',7: 'ESCARCEGA',8: 'HECELCHAKAN',9: 'HOPELCHEN',10: 'PALIZADA',11: 'SEYBAPLAYA',12: 'TENABO'})
# rc = ['PAN','PRI','PRD','PAN_PRI_PRD_a']
# df['PAN_PRI_PRD'] = df[rc].sum(axis=1)
# df = df.drop(['MUNICIPIO','PAN','PRI','PRD','PAN_PRI_PRD_a'], axis=1)
# df = df.T
# print (df)
# CALAKMUL = pd.DataFrame(df['CALAKMUL'])
# CALAKMUL = CALAKMUL.sort_values('CALAKMUL',ascending=False)
# CALAKMUL = CALAKMUL.head().T
# CALAKMUL = CALAKMUL.drop(CALAKMUL.columns[[1,2,3,4]], axis='columns')
# CALAKMUL = str(CALAKMUL.to_json(orient="index")).replace('{','')
# CALAKMUL = CALAKMUL.replace(':"','{"')
# CALAKMUL = CALAKMUL.replace('}}','}')
# CALAKMUL = CALAKMUL.replace('":','" ')
# CALAKMUL = CALAKMUL.replace('"CALAKMUL"{"','"GANADOR":"')
# CALAKMUL = CALAKMUL.split()
# CALAKMUL = CALAKMUL[0]
# CALAKMUL = '"CALAKMUL":{'+CALAKMUL+"}"

# CALKINI = pd.DataFrame(df['CALKINI'])
# CALKINI = CALKINI.sort_values('CALKINI',ascending=False)
# CALKINI = CALKINI.head().T
# CALKINI = CALKINI.drop(CALKINI.columns[[1,2,3,4]], axis='columns')
# CALKINI = str(CALKINI.to_json(orient="index")).replace('{','')
# CALKINI = CALKINI.replace(':"','{"')
# CALKINI = CALKINI.replace('}}','}')
# CALKINI = CALKINI.replace('":','" ')
# CALKINI = CALKINI.replace('"CALKINI"{"','"GANADOR":"')
# CALKINI = CALKINI.split()
# CALKINI = CALKINI[0]
# CALKINI = '"CALKINI":{'+CALKINI+"}"

# CAMPECHE = pd.DataFrame(df['CAMPECHE'])
# CAMPECHE = CAMPECHE.sort_values('CAMPECHE',ascending=False)
# CAMPECHE = CAMPECHE.head().T
# CAMPECHE = CAMPECHE.drop(CAMPECHE.columns[[1,2,3,4]], axis='columns')
# CAMPECHE = str(CAMPECHE.to_json(orient="index")).replace('{','')
# CAMPECHE = CAMPECHE.replace(':"','{"')
# CAMPECHE = CAMPECHE.replace('}}','}')
# CAMPECHE = CAMPECHE.replace('":','" ')
# CAMPECHE = CAMPECHE.replace('"CAMPECHE"{"','"GANADOR":"')
# CAMPECHE = CAMPECHE.split()
# CAMPECHE = CAMPECHE[0]
# CAMPECHE = '"CAMPECHE":{'+CAMPECHE+"}"

# CANDELARIA = pd.DataFrame(df['CANDELARIA'])
# CANDELARIA = CANDELARIA.sort_values('CANDELARIA',ascending=False)
# CANDELARIA = CANDELARIA.head().T
# CANDELARIA = CANDELARIA.drop(CANDELARIA.columns[[1,2,3,4]], axis='columns')
# CANDELARIA = str(CANDELARIA.to_json(orient="index")).replace('{','')
# CANDELARIA = CANDELARIA.replace(':"','{"')
# CANDELARIA = CANDELARIA.replace('}}','}')
# CANDELARIA = CANDELARIA.replace('":','" ')
# CANDELARIA = CANDELARIA.replace('"CANDELARIA"{"','"GANADOR":"')
# CANDELARIA = CANDELARIA.split()
# CANDELARIA = CANDELARIA[0]
# CANDELARIA = '"CANDELARIA":{'+CANDELARIA+"}"

# CARMEN = pd.DataFrame(df['CARMEN'])
# CARMEN = CARMEN.sort_values('CARMEN',ascending=False)
# CARMEN = CARMEN.head().T
# CARMEN = CARMEN.drop(CARMEN.columns[[1,2,3,4]], axis='columns')
# CARMEN = str(CARMEN.to_json(orient="index")).replace('{','')
# CARMEN = CARMEN.replace(':"','{"')
# CARMEN = CARMEN.replace('}}','}')
# CARMEN = CARMEN.replace('":','" ')
# CARMEN = CARMEN.replace('"CARMEN"{"','"GANADOR":"')
# CARMEN = CARMEN.split()
# CARMEN = CARMEN[0]
# CARMEN = '"CARMEN":{'+CARMEN+"}"


# CHAMPOTON = pd.DataFrame(df['CHAMPOTON'])
# CHAMPOTON = CHAMPOTON.sort_values('CHAMPOTON',ascending=False)
# CHAMPOTON = CHAMPOTON.head().T
# CHAMPOTON = CHAMPOTON.drop(CHAMPOTON.columns[[1,2,3,4]], axis='columns')
# CHAMPOTON = str(CHAMPOTON.to_json(orient="index")).replace('{','')
# CHAMPOTON = CHAMPOTON.replace(':"','{"')
# CHAMPOTON = CHAMPOTON.replace('}}','}')
# CHAMPOTON = CHAMPOTON.replace('":','" ')
# CHAMPOTON = CHAMPOTON.replace('"CHAMPOTON"{"','"GANADOR":"')
# CHAMPOTON = CHAMPOTON.split()
# CHAMPOTON = CHAMPOTON[0]
# CHAMPOTON = '"CHAMPOTON":{'+CHAMPOTON+"}"

# DZITBALCHE = pd.DataFrame(df['DZITBALCHE'])
# DZITBALCHE = DZITBALCHE.sort_values('DZITBALCHE',ascending=False)
# DZITBALCHE = DZITBALCHE.head().T
# DZITBALCHE = DZITBALCHE.drop(DZITBALCHE.columns[[1,2,3,4]], axis='columns')
# DZITBALCHE = str(DZITBALCHE.to_json(orient="index")).replace('{','')
# DZITBALCHE = DZITBALCHE.replace(':"','{"')
# DZITBALCHE = DZITBALCHE.replace('}}','}')
# DZITBALCHE = DZITBALCHE.replace('":','" ')
# DZITBALCHE = DZITBALCHE.replace('"DZITBALCHE"{"','"GANADOR":"')
# DZITBALCHE = DZITBALCHE.split()
# DZITBALCHE = DZITBALCHE[0]
# DZITBALCHE = '"DZITBALCHE":{'+DZITBALCHE+"}"

# ESCARCEGA = pd.DataFrame(df['ESCARCEGA'])
# ESCARCEGA = ESCARCEGA.sort_values('ESCARCEGA',ascending=False)
# ESCARCEGA = ESCARCEGA.head().T
# ESCARCEGA = ESCARCEGA.drop(ESCARCEGA.columns[[1,2,3,4]], axis='columns')
# ESCARCEGA = str(ESCARCEGA.to_json(orient="index")).replace('{','')
# ESCARCEGA = ESCARCEGA.replace(':"','{"')
# ESCARCEGA = ESCARCEGA.replace('}}','}')
# ESCARCEGA = ESCARCEGA.replace('":','" ')
# ESCARCEGA = ESCARCEGA.replace('"ESCARCEGA"{"','"GANADOR":"')
# ESCARCEGA = ESCARCEGA.split()
# ESCARCEGA = ESCARCEGA[0]
# ESCARCEGA = '"ESCARCEGA":{'+ESCARCEGA+"}"

# HECELCHAKAN = pd.DataFrame(df['HECELCHAKAN'])
# HECELCHAKAN = HECELCHAKAN.sort_values('HECELCHAKAN',ascending=False)
# HECELCHAKAN = HECELCHAKAN.head().T
# HECELCHAKAN = HECELCHAKAN.drop(HECELCHAKAN.columns[[1,2,3,4]], axis='columns')
# HECELCHAKAN = str(HECELCHAKAN.to_json(orient="index")).replace('{','')
# HECELCHAKAN = HECELCHAKAN.replace(':"','{"')
# HECELCHAKAN = HECELCHAKAN.replace('}}','}')
# HECELCHAKAN = HECELCHAKAN.replace('":','" ')
# HECELCHAKAN = HECELCHAKAN.replace('"HECELCHAKAN"{"','"GANADOR":"')
# HECELCHAKAN = HECELCHAKAN.split()
# HECELCHAKAN = HECELCHAKAN[0]
# HECELCHAKAN = '"HECELCHAKAN":{'+HECELCHAKAN+"}"

# PALIZADA = pd.DataFrame(df['PALIZADA'])
# PALIZADA = PALIZADA.sort_values('PALIZADA',ascending=False)
# PALIZADA = PALIZADA.head().T
# PALIZADA = PALIZADA.drop(PALIZADA.columns[[1,2,3,4]], axis='columns')
# PALIZADA = str(PALIZADA.to_json(orient="index")).replace('{','')
# PALIZADA = PALIZADA.replace(':"','{"')
# PALIZADA = PALIZADA.replace('}}','}')
# PALIZADA = PALIZADA.replace('":','" ')
# PALIZADA = PALIZADA.replace('"PALIZADA"{"','"GANADOR":"')
# PALIZADA = PALIZADA.split()
# PALIZADA = PALIZADA[0]
# PALIZADA = '"PALIZADA":{'+PALIZADA+"}"

# SEYBAPLAYA = pd.DataFrame(df['SEYBAPLAYA'])
# SEYBAPLAYA = SEYBAPLAYA.sort_values('SEYBAPLAYA',ascending=False)
# SEYBAPLAYA = SEYBAPLAYA.head().T
# SEYBAPLAYA = SEYBAPLAYA.drop(SEYBAPLAYA.columns[[1,2,3,4]], axis='columns')
# SEYBAPLAYA = str(SEYBAPLAYA.to_json(orient="index")).replace('{','')
# SEYBAPLAYA = SEYBAPLAYA.replace(':"','{"')
# SEYBAPLAYA = SEYBAPLAYA.replace('}}','}')
# SEYBAPLAYA = SEYBAPLAYA.replace('":','" ')
# SEYBAPLAYA = SEYBAPLAYA.replace('"SEYBAPLAYA"{"','"GANADOR":"')
# SEYBAPLAYA = SEYBAPLAYA.split()
# SEYBAPLAYA = SEYBAPLAYA[0]
# SEYBAPLAYA = '"SEYBAPLAYA":{'+SEYBAPLAYA+"}"

# TENABO = pd.DataFrame(df['TENABO'])
# TENABO = TENABO.sort_values('TENABO',ascending=False)
# TENABO = TENABO.head().T
# TENABO = TENABO.drop(TENABO.columns[[1,2,3,4]], axis='columns')
# TENABO = str(TENABO.to_json(orient="index")).replace('{','')
# TENABO = TENABO.replace(':"','{"')
# TENABO = TENABO.replace('}}','}')
# TENABO = TENABO.replace('":','" ')
# TENABO = TENABO.replace('"TENABO"{"','"GANADOR":"')
# TENABO = TENABO.split()
# TENABO = TENABO[0]
# TENABO = '"TENABO":{'+TENABO+"}"

# result = '{'+CALAKMUL+','+CALKINI+','+CAMPECHE+','+CANDELARIA+','+CARMEN+','+CHAMPOTON+','+CHAMPOTON+','+ESCARCEGA+','+HECELCHAKAN+','+PALIZADA+','+SEYBAPLAYA+','+TENABO+'}'
# print (result)
df = pd.read_csv('./files/20210601_1852_PREP_DIP_LOC_CAMP/CAMP_DIP_LOC_2021.csv', header=None, sep='\n')
df = df[0].str.split(',', expand=True)
df = df.drop(df.index[[0,1,2,3,4,5]])
df = df.reset_index()
df = df.drop(['index', 0, 1,2,3,5,6,7,8,9,10,11,12,13,14,15,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45], axis=1)
cols = df.columns.drop(4)
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')
df = df.groupby([4]).agg(
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
    }).reset_index()
df = df.rename(columns={
    4: 'CONGRESO',
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
    26:'PAN_PRI_PRD_a',
    })
df = df.rename(index={0: 'I',1: 'II',2: 'III',3: 'IV',4: 'V',5: 'VI',6: 'VII',7: 'VIII',8: 'IX',9: 'X',10: 'XI',11: 'XII',12: 'XIII',13: 'XIV',14: 'XV',15: 'XVI',16: 'XVII',17: 'XVIII',18: 'XIX',19: 'XX',20: 'XXI'})
rc = ['PAN','PRI','PRD','PAN_PRI_PRD_a']
df['PAN_PRI_PRD'] = df[rc].sum(axis=1)
df = df.drop(['CONGRESO','PAN','PRI','PRD','PAN_PRI_PRD_a'], axis=1)
df = df.T
I = pd.DataFrame(df['I'])
I = I.sort_values('I',ascending=False)
I = I.head().T
I = I.drop(I.columns[[1,2,3,4]], axis='columns')
I = str(I.to_json(orient="index")).replace('{','')
I = I.replace(':"','{"')
I = I.replace('}}','}')
I = I.replace('":','" ')
I = I.replace('"I"{"','"GANADOR":"')
I = I.split()
I = I[0]
I = '"I":{'+I+"}"

II = pd.DataFrame(df['II'])
II = II.sort_values('II',ascending=False)
II = II.head().T
II = II.drop(II.columns[[1,2,3,4]], axis='columns')
II = str(II.to_json(orient="index")).replace('{','')
II = II.replace(':"','{"')
II = II.replace('}}','}')
II = II.replace('":','" ')
II = II.replace('"II"{"','"GANADOR":"')
II = II.split()
II = II[0]
II = '"II":{'+II+"}"

III = pd.DataFrame(df['III'])
III = III.sort_values('III',ascending=False)
III = III.head().T
III = III.drop(III.columns[[1,2,3,4]], axis='columns')
III = str(III.to_json(orient="index")).replace('{','')
III = III.replace(':"','{"')
III = III.replace('}}','}')
III = III.replace('":','" ')
III = III.replace('"III"{"','"GANADOR":"')
III = III.split()
III = III[0]
III = '"III":{'+III+"}"

IV = pd.DataFrame(df['IV'])
IV = IV.sort_values('IV',ascending=False)
IV = IV.head().T
IV = IV.drop(IV.columns[[1,2,3,4]], axis='columns')
IV = str(IV.to_json(orient="index")).replace('{','')
IV = IV.replace(':"','{"')
IV = IV.replace('}}','}')
IV = IV.replace('":','" ')
IV = IV.replace('"IV"{"','"GANADOR":"')
IV = IV.split()
IV = IV[0]
IV = '"IV":{'+IV+"}"

V = pd.DataFrame(df['V'])
V = V.sort_values('V',ascending=False)
V = V.head().T
V = V.drop(V.columns[[1,2,3,4]], axis='columns')
V = str(V.to_json(orient="index")).replace('{','')
V = V.replace(':"','{"')
V = V.replace('}}','}')
V = V.replace('":','" ')
V = V.replace('"V"{"','"GANADOR":"')
V = V.split()
V = V[0]
V = '"V":{'+V+"}"


VI = pd.DataFrame(df['VI'])
VI = VI.sort_values('VI',ascending=False)
VI = VI.head().T
VI = VI.drop(VI.columns[[1,2,3,4]], axis='columns')
VI = str(VI.to_json(orient="index")).replace('{','')
VI = VI.replace(':"','{"')
VI = VI.replace('}}','}')
VI = VI.replace('":','" ')
VI = VI.replace('"VI"{"','"GANADOR":"')
VI = VI.split()
VI = VI[0]
VI = '"VI":{'+VI+"}"

VII = pd.DataFrame(df['VII'])
VII = VII.sort_values('VII',ascending=False)
VII = VII.head().T
VII = VII.drop(VII.columns[[1,2,3,4]], axis='columns')
VII = str(VII.to_json(orient="index")).replace('{','')
VII = VII.replace(':"','{"')
VII = VII.replace('}}','}')
VII = VII.replace('":','" ')
VII = VII.replace('"VII"{"','"GANADOR":"')
VII = VII.split()
VII = VII[0]
VII = '"VII":{'+VII+"}"

VIII = pd.DataFrame(df['VIII'])
VIII = VIII.sort_values('VIII',ascending=False)
VIII = VIII.head().T
VIII = VIII.drop(VIII.columns[[1,2,3,4]], axis='columns')
VIII = str(VIII.to_json(orient="index")).replace('{','')
VIII = VIII.replace(':"','{"')
VIII = VIII.replace('}}','}')
VIII = VIII.replace('":','" ')
VIII = VIII.replace('"VIII"{"','"GANADOR":"')
VIII = VIII.split()
VIII = VIII[0]
VIII = '"VIII":{'+VIII+"}"

IX = pd.DataFrame(df['IX'])
IX = IX.sort_values('IX',ascending=False)
IX = IX.head().T
IX = IX.drop(IX.columns[[1,2,3,4]], axis='columns')
IX = str(IX.to_json(orient="index")).replace('{','')
IX = IX.replace(':"','{"')
IX = IX.replace('}}','}')
IX = IX.replace('":','" ')
IX = IX.replace('"IX"{"','"GANADOR":"')
IX = IX.split()
IX = IX[0]
IX = '"IX":{'+IX+"}"

X = pd.DataFrame(df['X'])
X = X.sort_values('X',ascending=False)
X = X.head().T
X = X.drop(X.columns[[1,2,3,4]], axis='columns')
X = str(X.to_json(orient="index")).replace('{','')
X = X.replace(':"','{"')
X = X.replace('}}','}')
X = X.replace('":','" ')
X = X.replace('"X"{"','"GANADOR":"')
X = X.split()
X = X[0]
X = '"X":{'+X+"}"

XI = pd.DataFrame(df['XI'])
XI = XI.sort_values('XI',ascending=False)
XI = XI.head().T
XI = XI.drop(XI.columns[[1,2,3,4]], axis='columns')
XI = str(XI.to_json(orient="index")).replace('{','')
XI = XI.replace(':"','{"')
XI = XI.replace('}}','}')
XI = XI.replace('":','" ')
XI = XI.replace('"XI"{"','"GANADOR":"')
XI = XI.split()
XI = XI[0]
XI = '"XI":{'+XI+"}"

XII = pd.DataFrame(df['XII'])
XII = XII.sort_values('XII',ascending=False)
XII = XII.head().T
XII = XII.drop(XII.columns[[1,2,3,4]], axis='columns')
XII = str(XII.to_json(orient="index")).replace('{','')
XII = XII.replace(':"','{"')
XII = XII.replace('}}','}')
XII = XII.replace('":','" ')
XII = XII.replace('"XII"{"','"GANADOR":"')
XII = XII.split()
XII = XII[0]
XII = '"XII":{'+XII+"}"

XIII = pd.DataFrame(df['XIII'])
XIII = XIII.sort_values('XIII',ascending=False)
XIII = XIII.head().T
XIII = XIII.drop(XIII.columns[[1,2,3,4]], axis='columns')
XIII = str(XIII.to_json(orient="index")).replace('{','')
XIII = XIII.replace(':"','{"')
XIII = XIII.replace('}}','}')
XIII = XIII.replace('":','" ')
XIII = XIII.replace('"XIII"{"','"GANADOR":"')
XIII = XIII.split()
XIII = XIII[0]
XIII = '"XIII":{'+XIII+"}"

XIV = pd.DataFrame(df['XIV'])
XIV = XIV.sort_values('XIV',ascending=False)
XIV = XIV.head().T
XIV = XIV.drop(XIV.columns[[1,2,3,4]], axis='columns')
XIV = str(XIV.to_json(orient="index")).replace('{','')
XIV = XIV.replace(':"','{"')
XIV = XIV.replace('}}','}')
XIV = XIV.replace('":','" ')
XIV = XIV.replace('"XIV"{"','"GANADOR":"')
XIV = XIV.split()
XIV = XIV[0]
XIV = '"XIV":{'+XIV+"}"

XV = pd.DataFrame(df['XV'])
XV = XV.sort_values('XV',ascending=False)
XV = XV.head().T
XV = XV.drop(XV.columns[[1,2,3,4]], axis='columns')
XV = str(XV.to_json(orient="index")).replace('{','')
XV = XV.replace(':"','{"')
XV = XV.replace('}}','}')
XV = XV.replace('":','" ')
XV = XV.replace('"XV"{"','"GANADOR":"')
XV = XV.split()
XV = XV[0]
XV = '"XV":{'+XV+"}"

XVI = pd.DataFrame(df['XVI'])
XVI = XVI.sort_values('XVI',ascending=False)
XVI = XVI.head().T
XVI = XVI.drop(XVI.columns[[1,2,3,4]], axis='columns')
XVI = str(XVI.to_json(orient="index")).replace('{','')
XVI = XVI.replace(':"','{"')
XVI = XVI.replace('}}','}')
XVI = XVI.replace('":','" ')
XVI = XVI.replace('"XVI"{"','"GANADOR":"')
XVI = XVI.split()
XVI = XVI[0]
XVI = '"XVI":{'+XVI+"}"

XVII = pd.DataFrame(df['XVII'])
XVII = XVII.sort_values('XVII',ascending=False)
XVII = XVII.head().T
XVII = XVII.drop(XVII.columns[[1,2,3,4]], axis='columns')
XVII = str(XVII.to_json(orient="index")).replace('{','')
XVII = XVII.replace(':"','{"')
XVII = XVII.replace('}}','}')
XVII = XVII.replace('":','" ')
XVII = XVII.replace('"XVII"{"','"GANADOR":"')
XVII = XVII.split()
XVII = XVII[0]
XVII = '"XVII":{'+XVII+"}"

XVIII = pd.DataFrame(df['XVIII'])
XVIII = XVIII.sort_values('XVIII',ascending=False)
XVIII = XVIII.head().T
XVIII = XVIII.drop(XVIII.columns[[1,2,3,4]], axis='columns')
XVIII = str(XVIII.to_json(orient="index")).replace('{','')
XVIII = XVIII.replace(':"','{"')
XVIII = XVIII.replace('}}','}')
XVIII = XVIII.replace('":','" ')
XVIII = XVIII.replace('"XVIII"{"','"GANADOR":"')
XVIII = XVIII.split()
XVIII = XVIII[0]
XVIII = '"XVIII":{'+XVIII+"}"

XIX = pd.DataFrame(df['XIX'])
XIX = XIX.sort_values('XIX',ascending=False)
XIX = XIX.head().T
XIX = XIX.drop(XIX.columns[[1,2,3,4]], axis='columns')
XIX = str(XIX.to_json(orient="index")).replace('{','')
XIX = XIX.replace(':"','{"')
XIX = XIX.replace('}}','}')
XIX = XIX.replace('":','" ')
XIX = XIX.replace('"XIX"{"','"GANADOR":"')
XIX = XIX.split()
XIX = XIX[0]
XIX = '"XIX":{'+XIX+"}"

XX = pd.DataFrame(df['XX'])
XX = XX.sort_values('XX',ascending=False)
XX = XX.head().T
XX = XX.drop(XX.columns[[1,2,3,4]], axis='columns')
XX = str(XX.to_json(orient="index")).replace('{','')
XX = XX.replace(':"','{"')
XX = XX.replace('}}','}')
XX = XX.replace('":','" ')
XX = XX.replace('"XX"{"','"GANADOR":"')
XX = XX.split()
XX = XX[0]
XX = '"XX":{'+XX+"}"

XXI = pd.DataFrame(df['XXI'])
XXI = XXI.sort_values('XXI',ascending=False)
XXI = XXI.head().T
XXI = XXI.drop(XXI.columns[[1,2,3,4]], axis='columns')
XXI = str(XXI.to_json(orient="index")).replace('{','')
XXI = XXI.replace(':"','{"')
XXI = XXI.replace('}}','}')
XXI = XXI.replace('":','" ')
XXI = XXI.replace('"XXI"{"','"GANADOR":"')
XXI = XXI.split()
XXI = XXI[0]
XXI = '"XXI":{'+XXI+"}"

result = '{'+I+','+II+','+III+','+IV+','+V+','+VI+','+VII+','+VIII+','+IX+','+X+','+XI+','+XII+','+XIII+','+XIV+','+XV+','+XVI+','+XVII+','+XVIII+','+XIX+','+XX+','+XXI+'}'

result = result.replace(':{"GANADOR":',':')
result = result.replace('"}','"')
data = json.loads(result)
df = pd.json_normalize(data)
df = pd.DataFrame(df).T

PT = df[0].str.contains('PT').value_counts()[True]
PVEM = df[0].str.contains('PVEM').value_counts()[True]
MC = df[0].str.contains('MC').value_counts()[True]
MOR = df[0].str.contains('MOR').value_counts()[True]
PES = df[0].str.contains('PES').value_counts()[True]
RSP = df[0].str.contains('RSP').value_counts()[True]
FM = df[0].str.contains('FM').value_counts()[True]
PAN_PRI_PRD = df[0].str.contains('PAN_PRI_PRD').value_counts()[True]
result = '{"PT":'+str(PT)+',"PVEM":'+str(PVEM)+',"MC":'+str(MC)+',"MOR":'+str(MOR)+',"PES":'+str(PES)+',"RSP":'+str(RSP)+',"FM":'+str(FM)+',"PAN_PRI_PRD":'+str(PAN_PRI_PRD)+'}'

print (result)
