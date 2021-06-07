import requests
import datetime
import zipfile
import json
import os
import pandas as pd
from shutil import rmtree
from pytz import timezone

# carpeta = os.listdir("./files/")
# dirname = carpeta[0] 
# dirname =  dirname[:14]
# dirname2 = carpeta[2] 
# dirname2 =  dirname2[:14]
# dirname3 = carpeta[1] 
# dirname3 =  dirname3[:14]
# if (dirname != dirname2):
#     print('si fue distinto')
#     dirname = dirname3
# else:
#     print('no fue distinto')
#     dirname = dirname3
# df = pd.read_csv('./files/'+dirname+'PREP_DIP_LOC_CAMP/CAMP_DIP_LOC_2021.csv', header=None, sep='\n')
# # df = pd.read_csv('./etc/data/files/20210601_1852_PREP_DIP_LOC_CAMP/CAMP_DIP_LOC_2021.csv', header=None, sep='\n')
# df = df[0].str.split(',', expand=True)
# df = df.drop(df.index[[0,1,2,3,4,5]])
# df = df.reset_index()
# df = df.drop(['index', 0, 1,2,3,5,6,7,8,9,10,11,12,13,14,15,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45], axis=1)
# cols = df.columns.drop(4)
# df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')
# df = df.groupby([4]).agg(
#     {16:'sum',
#     17:'sum',
#     18:'sum',
#     19:'sum',
#     20:'sum',
#     21:'sum',
#     22:'sum',
#     23:'sum',
#     24:'sum',
#     25:'sum',
#     26:'sum',
#     }).reset_index()
# df = df.rename(columns={
#     4: 'CONGRESO',
#     16:'PAN',
#     17:'PRI',
#     18:'PRD',
#     19:'PT',
#     20:'PVEM',
#     21:'MC',
#     22:'MOR',
#     23:'PES',
#     24:'RSP',
#     25:'FM',
#     26:'PAN_PRI_PRD_a',
#     })
# df = df.rename(index={0: 'I',1: 'II',2: 'III',3: 'IV',4: 'V',5: 'VI',6: 'VII',7: 'VIII',8: 'IX',9: 'X',10: 'XI',11: 'XII',12: 'XIII',13: 'XIV',14: 'XV',15: 'XVI',16: 'XVII',17: 'XVIII',18: 'XIX',19: 'XX',20: 'XXI'})
# rc = ['PAN','PRI','PRD','PAN_PRI_PRD_a']
# df['PAN_PRI_PRD'] = df[rc].sum(axis=1)
# df = df.drop(['CONGRESO','PAN','PRI','PRD','PAN_PRI_PRD_a'], axis=1)
# df = df.T
# I = pd.DataFrame(df['I'])
# I = I.sort_values('I',ascending=False)
# I = I.head().T
# I = I.drop(I.columns[[1,2,3,4]], axis='columns')
# I = str(I.to_json(orient="index")).replace('{','')
# I = I.replace(':"','{"')
# I = I.replace('}}','}')
# I = I.replace('":','" ')
# I = I.replace('"I"{"','"GANADOR":"')
# I = I.split()
# I = I[0]
# I = '"I":{'+I+"}"

# II = pd.DataFrame(df['II'])
# II = II.sort_values('II',ascending=False)
# II = II.head().T
# II = II.drop(II.columns[[1,2,3,4]], axis='columns')
# II = str(II.to_json(orient="index")).replace('{','')
# II = II.replace(':"','{"')
# II = II.replace('}}','}')
# II = II.replace('":','" ')
# II = II.replace('"II"{"','"GANADOR":"')
# II = II.split()
# II = II[0]
# II = '"II":{'+II+"}"

# III = pd.DataFrame(df['III'])
# III = III.sort_values('III',ascending=False)
# III = III.head().T
# III = III.drop(III.columns[[1,2,3,4]], axis='columns')
# III = str(III.to_json(orient="index")).replace('{','')
# III = III.replace(':"','{"')
# III = III.replace('}}','}')
# III = III.replace('":','" ')
# III = III.replace('"III"{"','"GANADOR":"')
# III = III.split()
# III = III[0]
# III = '"III":{'+III+"}"

# IV = pd.DataFrame(df['IV'])
# IV = IV.sort_values('IV',ascending=False)
# IV = IV.head().T
# IV = IV.drop(IV.columns[[1,2,3,4]], axis='columns')
# IV = str(IV.to_json(orient="index")).replace('{','')
# IV = IV.replace(':"','{"')
# IV = IV.replace('}}','}')
# IV = IV.replace('":','" ')
# IV = IV.replace('"IV"{"','"GANADOR":"')
# IV = IV.split()
# IV = IV[0]
# IV = '"IV":{'+IV+"}"

# V = pd.DataFrame(df['V'])
# V = V.sort_values('V',ascending=False)
# V = V.head().T
# V = V.drop(V.columns[[1,2,3,4]], axis='columns')
# V = str(V.to_json(orient="index")).replace('{','')
# V = V.replace(':"','{"')
# V = V.replace('}}','}')
# V = V.replace('":','" ')
# V = V.replace('"V"{"','"GANADOR":"')
# V = V.split()
# V = V[0]
# V = '"V":{'+V+"}"


# VI = pd.DataFrame(df['VI'])
# VI = VI.sort_values('VI',ascending=False)
# VI = VI.head().T
# VI = VI.drop(VI.columns[[1,2,3,4]], axis='columns')
# VI = str(VI.to_json(orient="index")).replace('{','')
# VI = VI.replace(':"','{"')
# VI = VI.replace('}}','}')
# VI = VI.replace('":','" ')
# VI = VI.replace('"VI"{"','"GANADOR":"')
# VI = VI.split()
# VI = VI[0]
# VI = '"VI":{'+VI+"}"

# VII = pd.DataFrame(df['VII'])
# VII = VII.sort_values('VII',ascending=False)
# VII = VII.head().T
# VII = VII.drop(VII.columns[[1,2,3,4]], axis='columns')
# VII = str(VII.to_json(orient="index")).replace('{','')
# VII = VII.replace(':"','{"')
# VII = VII.replace('}}','}')
# VII = VII.replace('":','" ')
# VII = VII.replace('"VII"{"','"GANADOR":"')
# VII = VII.split()
# VII = VII[0]
# VII = '"VII":{'+VII+"}"

# VIII = pd.DataFrame(df['VIII'])
# VIII = VIII.sort_values('VIII',ascending=False)
# VIII = VIII.head().T
# VIII = VIII.drop(VIII.columns[[1,2,3,4]], axis='columns')
# VIII = str(VIII.to_json(orient="index")).replace('{','')
# VIII = VIII.replace(':"','{"')
# VIII = VIII.replace('}}','}')
# VIII = VIII.replace('":','" ')
# VIII = VIII.replace('"VIII"{"','"GANADOR":"')
# VIII = VIII.split()
# VIII = VIII[0]
# VIII = '"VIII":{'+VIII+"}"

# IX = pd.DataFrame(df['IX'])
# IX = IX.sort_values('IX',ascending=False)
# IX = IX.head().T
# IX = IX.drop(IX.columns[[1,2,3,4]], axis='columns')
# IX = str(IX.to_json(orient="index")).replace('{','')
# IX = IX.replace(':"','{"')
# IX = IX.replace('}}','}')
# IX = IX.replace('":','" ')
# IX = IX.replace('"IX"{"','"GANADOR":"')
# IX = IX.split()
# IX = IX[0]
# IX = '"IX":{'+IX+"}"

# X = pd.DataFrame(df['X'])
# X = X.sort_values('X',ascending=False)
# X = X.head().T
# X = X.drop(X.columns[[1,2,3,4]], axis='columns')
# X = str(X.to_json(orient="index")).replace('{','')
# X = X.replace(':"','{"')
# X = X.replace('}}','}')
# X = X.replace('":','" ')
# X = X.replace('"X"{"','"GANADOR":"')
# X = X.split()
# X = X[0]
# X = '"X":{'+X+"}"

# XI = pd.DataFrame(df['XI'])
# XI = XI.sort_values('XI',ascending=False)
# XI = XI.head().T
# XI = XI.drop(XI.columns[[1,2,3,4]], axis='columns')
# XI = str(XI.to_json(orient="index")).replace('{','')
# XI = XI.replace(':"','{"')
# XI = XI.replace('}}','}')
# XI = XI.replace('":','" ')
# XI = XI.replace('"XI"{"','"GANADOR":"')
# XI = XI.split()
# XI = XI[0]
# XI = '"XI":{'+XI+"}"

# XII = pd.DataFrame(df['XII'])
# XII = XII.sort_values('XII',ascending=False)
# XII = XII.head().T
# XII = XII.drop(XII.columns[[1,2,3,4]], axis='columns')
# XII = str(XII.to_json(orient="index")).replace('{','')
# XII = XII.replace(':"','{"')
# XII = XII.replace('}}','}')
# XII = XII.replace('":','" ')
# XII = XII.replace('"XII"{"','"GANADOR":"')
# XII = XII.split()
# XII = XII[0]
# XII = '"XII":{'+XII+"}"

# XIII = pd.DataFrame(df['XIII'])
# XIII = XIII.sort_values('XIII',ascending=False)
# XIII = XIII.head().T
# XIII = XIII.drop(XIII.columns[[1,2,3,4]], axis='columns')
# XIII = str(XIII.to_json(orient="index")).replace('{','')
# XIII = XIII.replace(':"','{"')
# XIII = XIII.replace('}}','}')
# XIII = XIII.replace('":','" ')
# XIII = XIII.replace('"XIII"{"','"GANADOR":"')
# XIII = XIII.split()
# XIII = XIII[0]
# XIII = '"XIII":{'+XIII+"}"

# XIV = pd.DataFrame(df['XIV'])
# XIV = XIV.sort_values('XIV',ascending=False)
# XIV = XIV.head().T
# XIV = XIV.drop(XIV.columns[[1,2,3,4]], axis='columns')
# XIV = str(XIV.to_json(orient="index")).replace('{','')
# XIV = XIV.replace(':"','{"')
# XIV = XIV.replace('}}','}')
# XIV = XIV.replace('":','" ')
# XIV = XIV.replace('"XIV"{"','"GANADOR":"')
# XIV = XIV.split()
# XIV = XIV[0]
# XIV = '"XIV":{'+XIV+"}"

# XV = pd.DataFrame(df['XV'])
# XV = XV.sort_values('XV',ascending=False)
# XV = XV.head().T
# XV = XV.drop(XV.columns[[1,2,3,4]], axis='columns')
# XV = str(XV.to_json(orient="index")).replace('{','')
# XV = XV.replace(':"','{"')
# XV = XV.replace('}}','}')
# XV = XV.replace('":','" ')
# XV = XV.replace('"XV"{"','"GANADOR":"')
# XV = XV.split()
# XV = XV[0]
# XV = '"XV":{'+XV+"}"

# XVI = pd.DataFrame(df['XVI'])
# XVI = XVI.sort_values('XVI',ascending=False)
# XVI = XVI.head().T
# XVI = XVI.drop(XVI.columns[[1,2,3,4]], axis='columns')
# XVI = str(XVI.to_json(orient="index")).replace('{','')
# XVI = XVI.replace(':"','{"')
# XVI = XVI.replace('}}','}')
# XVI = XVI.replace('":','" ')
# XVI = XVI.replace('"XVI"{"','"GANADOR":"')
# XVI = XVI.split()
# XVI = XVI[0]
# XVI = '"XVI":{'+XVI+"}"

# XVII = pd.DataFrame(df['XVII'])
# XVII = XVII.sort_values('XVII',ascending=False)
# XVII = XVII.head().T
# XVII = XVII.drop(XVII.columns[[1,2,3,4]], axis='columns')
# XVII = str(XVII.to_json(orient="index")).replace('{','')
# XVII = XVII.replace(':"','{"')
# XVII = XVII.replace('}}','}')
# XVII = XVII.replace('":','" ')
# XVII = XVII.replace('"XVII"{"','"GANADOR":"')
# XVII = XVII.split()
# XVII = XVII[0]
# XVII = '"XVII":{'+XVII+"}"

# XVIII = pd.DataFrame(df['XVIII'])
# XVIII = XVIII.sort_values('XVIII',ascending=False)
# XVIII = XVIII.head().T
# XVIII = XVIII.drop(XVIII.columns[[1,2,3,4]], axis='columns')
# XVIII = str(XVIII.to_json(orient="index")).replace('{','')
# XVIII = XVIII.replace(':"','{"')
# XVIII = XVIII.replace('}}','}')
# XVIII = XVIII.replace('":','" ')
# XVIII = XVIII.replace('"XVIII"{"','"GANADOR":"')
# XVIII = XVIII.split()
# XVIII = XVIII[0]
# XVIII = '"XVIII":{'+XVIII+"}"

# XIX = pd.DataFrame(df['XIX'])
# XIX = XIX.sort_values('XIX',ascending=False)
# XIX = XIX.head().T
# XIX = XIX.drop(XIX.columns[[1,2,3,4]], axis='columns')
# XIX = str(XIX.to_json(orient="index")).replace('{','')
# XIX = XIX.replace(':"','{"')
# XIX = XIX.replace('}}','}')
# XIX = XIX.replace('":','" ')
# XIX = XIX.replace('"XIX"{"','"GANADOR":"')
# XIX = XIX.split()
# XIX = XIX[0]
# XIX = '"XIX":{'+XIX+"}"

# XX = pd.DataFrame(df['XX'])
# XX = XX.sort_values('XX',ascending=False)
# XX = XX.head().T
# XX = XX.drop(XX.columns[[1,2,3,4]], axis='columns')
# XX = str(XX.to_json(orient="index")).replace('{','')
# XX = XX.replace(':"','{"')
# XX = XX.replace('}}','}')
# XX = XX.replace('":','" ')
# XX = XX.replace('"XX"{"','"GANADOR":"')
# XX = XX.split()
# XX = XX[0]
# XX = '"XX":{'+XX+"}"

# XXI = pd.DataFrame(df['XXI'])
# XXI = XXI.sort_values('XXI',ascending=False)
# XXI = XXI.head().T
# XXI = XXI.drop(XXI.columns[[1,2,3,4]], axis='columns')
# XXI = str(XXI.to_json(orient="index")).replace('{','')
# XXI = XXI.replace(':"','{"')
# XXI = XXI.replace('}}','}')
# XXI = XXI.replace('":','" ')
# XXI = XXI.replace('"XXI"{"','"GANADOR":"')
# XXI = XXI.split()
# XXI = XXI[0]
# XXI = '"XXI":{'+XXI+"}"

# result = '{'+I+','+II+','+III+','+IV+','+V+','+VI+','+VII+','+VIII+','+IX+','+X+','+XI+','+XII+','+XIII+','+XIV+','+XV+','+XVI+','+XVII+','+XVIII+','+XIX+','+XX+','+XXI+'}'
# result = result.replace('PT','NULL')
# result = result.replace(':{"GANADOR":',':')
# result = result.replace('"}','"')
# data = json.loads(result)
# df = pd.json_normalize(data)
# df = pd.DataFrame(df).T
# print (df)
# PT = 0
# PVEM = 0
# MC = df[0].str.contains('MC').value_counts()[True]
# MOR = df[0].str.contains('MOR').value_counts()[True]
# PES = 0
# RSP =0
# FM = 0
# PAN_PRI_PRD = df[0].str.contains('PAN_PRI_PRD').value_counts()[True]
# result = '{"PT":'+str(PT)+',"PVEM":'+str(PVEM)+',"MC":'+str(MC)+',"MOR":'+str(MOR)+',"PES":'+str(PES)+',"RSP":'+str(RSP)+',"FM":'+str(FM)+',"PAN_PRI_PRD":'+str(PAN_PRI_PRD)+'}'
# print (result)
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
df = pd.read_csv('./files/'+dirname+'PREP_GOB_CAMP/CAMP_GOB_2021.csv', header=None, sep='\n')
    # df = pd.read_csv('./etc/data/files/20210601_1852_PREP_GOB_CAMP/CAMP_GOB_2021.csv', header=None, sep='\n')
df = df[0].str.split(',', expand=True)
df = df.fillna(0)
print (df[34])
df = df.drop(df.index[[0,1,2,3,4,5,1195,1196,1197]])
total = pd.to_numeric(df[32]).sum()
print (total)
# print (perro)