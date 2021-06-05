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
df = df.drop(['index', 0, 1,2,3,4,6,7,8,9,10,11,12,13,14,15,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46], axis=1)
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
35:'sum'
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
35:'TOTAL'
})
df = df.rename(index={0: 'CALAKMUL',1: 'CALKINI',2: 'CAMPECHE',3: 'CANDELARIA',4: 'CARMEN',5: 'CHAMPOTON',6: 'DZITBALCHE',7: 'ESCARCEGA',8: 'HECELCHAKAN',9: 'HOPELCHEN',10: 'PALIZADA',11: 'SEYBAPLAYA',12: 'TENABO'})
rc = ['PAN','PRI','PRD','PAN_PRI_PRD_a']
df['PAN_PRI_PRD'] = df[rc].sum(axis=1)
df = df.drop(['MUNICIPIO','PAN','PRI','PRD','PAN_PRI_PRD_a'], axis=1)
df = df.T

CALAKMUL = pd.DataFrame(df['CALAKMUL'])
CALAKMUL = CALAKMUL.sort_values('CALAKMUL',ascending=False)
CALAKMUL = CALAKMUL.T
totalCALAKMUL = CALAKMUL.loc['CALAKMUL','TOTAL']
CALAKMUL['PES'] = round(((CALAKMUL.loc['CALAKMUL','PES']*100)/totalCALAKMUL),2)
CALAKMUL['PVEM'] = round(((CALAKMUL.loc['CALAKMUL','PVEM']*100)/totalCALAKMUL),2)
CALAKMUL['CI-1'] = round(((CALAKMUL.loc['CALAKMUL','MOR']*100)/totalCALAKMUL),2)
CALAKMUL['MC'] = round(((CALAKMUL.loc['CALAKMUL','MC']*100)/totalCALAKMUL),2)
CALAKMUL['MOR'] = round(((CALAKMUL.loc['CALAKMUL','MOR']*100)/totalCALAKMUL),2)
CALAKMUL['RSP'] = round(((CALAKMUL.loc['CALAKMUL','RSP']*100)/totalCALAKMUL),2)
CALAKMUL['PT'] = round(((CALAKMUL.loc['CALAKMUL','PT']*100)/totalCALAKMUL),2)
CALAKMUL['PAN_PRI_PRD'] = round(((CALAKMUL.loc['CALAKMUL','PAN_PRI_PRD']*100)/totalCALAKMUL),2)
CALAKMUL['FM'] = round(((CALAKMUL.loc['CALAKMUL','FM']*100)/totalCALAKMUL),2)
CALAKMUL = CALAKMUL.head()
totalCALAKMUL = CALAKMUL.loc['CALAKMUL','TOTAL']
CALAKMUL1 = CALAKMUL.drop(CALAKMUL.columns[[0,2,3,4,5,6,7,8,9]], axis='columns')
CALAKMUL1 = str(CALAKMUL1.to_json(orient="index")).replace('{','')
CALAKMUL1 = CALAKMUL1.replace(':"','{"')
CALAKMUL1 = CALAKMUL1.replace('}}','},')
CALAKMUL1 = CALAKMUL1.replace('":','" ')
CALAKMUL1 = CALAKMUL1.replace('"CALAKMUL"{"','{"PARTIDO":"')
CALAKMUL1 = CALAKMUL1.split()
CALAKMUL1 = CALAKMUL1[0]+',"PORCENTAJE":'+CALAKMUL1[1]
CALAKMUL2 = CALAKMUL.drop(CALAKMUL.columns[[0,1,3,4,5,6,7,8,9]], axis='columns')
CALAKMUL2 = str(CALAKMUL2.to_json(orient="index")).replace('{','')
CALAKMUL2 = CALAKMUL2.replace(':"','{"')
CALAKMUL2 = CALAKMUL2.replace('}}','},')
CALAKMUL2 = CALAKMUL2.replace('":','" ')
CALAKMUL2 = CALAKMUL2.replace('"CALAKMUL"{"','{"PARTIDO":"')
CALAKMUL2 = CALAKMUL2.split()
CALAKMUL2 = CALAKMUL2[0]+',"PORCENTAJE":'+CALAKMUL2[1]
CALAKMUL3 = CALAKMUL.drop(CALAKMUL.columns[[0,1,2,4,5,6,7,8,9]], axis='columns')
CALAKMUL3 = str(CALAKMUL3.to_json(orient="index")).replace('{','')
CALAKMUL3 = CALAKMUL3.replace(':"','{"')
CALAKMUL3 = CALAKMUL3.replace('}}','}')
CALAKMUL3 = CALAKMUL3.replace('":','" ')
CALAKMUL3 = CALAKMUL3.replace('"CALAKMUL"{"','{"PARTIDO":"')
CALAKMUL3 = CALAKMUL3.split()
CALAKMUL3 = CALAKMUL3[0]+',"PORCENTAJE":'+CALAKMUL3[1]
CALAKMUL = '"CALAKMUL":{ "PRIMERO":'+CALAKMUL1+'"SEGUNDO":'+CALAKMUL2+'"TERCERO":'+CALAKMUL3+"}"


CALKINI = pd.DataFrame(df['CALKINI'])
CALKINI = CALKINI.sort_values('CALKINI',ascending=False)
CALKINI = CALKINI.T
totalCALKINI = CALKINI.loc['CALKINI','TOTAL']
CALKINI['PES'] = round(((CALKINI.loc['CALKINI','PES']*100)/totalCALKINI),2)
CALKINI['PVEM'] = round(((CALKINI.loc['CALKINI','PVEM']*100)/totalCALKINI),2)
CALKINI['CI-1'] = round(((CALKINI.loc['CALKINI','MOR']*100)/totalCALKINI),2)
CALKINI['MC'] = round(((CALKINI.loc['CALKINI','MC']*100)/totalCALKINI),2)
CALKINI['MOR'] = round(((CALKINI.loc['CALKINI','MOR']*100)/totalCALKINI),2)
CALKINI['RSP'] = round(((CALKINI.loc['CALKINI','RSP']*100)/totalCALKINI),2)
CALKINI['PT'] = round(((CALKINI.loc['CALKINI','PT']*100)/totalCALKINI),2)
CALKINI['PAN_PRI_PRD'] = round(((CALKINI.loc['CALKINI','PAN_PRI_PRD']*100)/totalCALKINI),2)
CALKINI['FM'] = round(((CALKINI.loc['CALKINI','FM']*100)/totalCALKINI),2)
CALKINI = CALKINI.head()
totalCALKINI = CALKINI.loc['CALKINI','TOTAL']
CALKINI1 = CALKINI.drop(CALKINI.columns[[0,2,3,4,5,6,7,8,9]], axis='columns')
CALKINI1 = str(CALKINI1.to_json(orient="index")).replace('{','')
CALKINI1 = CALKINI1.replace(':"','{"')
CALKINI1 = CALKINI1.replace('}}','},')
CALKINI1 = CALKINI1.replace('":','" ')
CALKINI1 = CALKINI1.replace('"CALKINI"{"','{"PARTIDO":"')
CALKINI1 = CALKINI1.split()
CALKINI1 = CALKINI1[0]+',"PORCENTAJE":'+CALKINI1[1]
CALKINI2 = CALKINI.drop(CALKINI.columns[[0,1,3,4,5,6,7,8,9]], axis='columns')
CALKINI2 = str(CALKINI2.to_json(orient="index")).replace('{','')
CALKINI2 = CALKINI2.replace(':"','{"')
CALKINI2 = CALKINI2.replace('}}','},')
CALKINI2 = CALKINI2.replace('":','" ')
CALKINI2 = CALKINI2.replace('"CALKINI"{"','{"PARTIDO":"')
CALKINI2 = CALKINI2.split()
CALKINI2 = CALKINI2[0]+',"PORCENTAJE":'+CALKINI2[1]
CALKINI3 = CALKINI.drop(CALKINI.columns[[0,1,2,4,5,6,7,8,9]], axis='columns')
CALKINI3 = str(CALKINI3.to_json(orient="index")).replace('{','')
CALKINI3 = CALKINI3.replace(':"','{"')
CALKINI3 = CALKINI3.replace('}}','}')
CALKINI3 = CALKINI3.replace('":','" ')
CALKINI3 = CALKINI3.replace('"CALKINI"{"','{"PARTIDO":"')
CALKINI3 = CALKINI3.split()
CALKINI3 = CALKINI3[0]+',"PORCENTAJE":'+CALKINI3[1]
CALKINI = '"CALKINI":{ "PRIMERO":'+CALKINI1+'"SEGUNDO":'+CALKINI2+'"TERCERO":'+CALKINI3+"}"

CAMPECHE = pd.DataFrame(df['CAMPECHE'])
CAMPECHE = CAMPECHE.sort_values('CAMPECHE',ascending=False)
CAMPECHE = CAMPECHE.T
totalCAMPECHE = CAMPECHE.loc['CAMPECHE','TOTAL']
CAMPECHE['PES'] = round(((CAMPECHE.loc['CAMPECHE','PES']*100)/totalCAMPECHE),2)
CAMPECHE['PVEM'] = round(((CAMPECHE.loc['CAMPECHE','PVEM']*100)/totalCAMPECHE),2)
CAMPECHE['CI-1'] = round(((CAMPECHE.loc['CAMPECHE','MOR']*100)/totalCAMPECHE),2)
CAMPECHE['MC'] = round(((CAMPECHE.loc['CAMPECHE','MC']*100)/totalCAMPECHE),2)
CAMPECHE['MOR'] = round(((CAMPECHE.loc['CAMPECHE','MOR']*100)/totalCAMPECHE),2)
CAMPECHE['RSP'] = round(((CAMPECHE.loc['CAMPECHE','RSP']*100)/totalCAMPECHE),2)
CAMPECHE['PT'] = round(((CAMPECHE.loc['CAMPECHE','PT']*100)/totalCAMPECHE),2)
CAMPECHE['PAN_PRI_PRD'] = round(((CAMPECHE.loc['CAMPECHE','PAN_PRI_PRD']*100)/totalCAMPECHE),2)
CAMPECHE['FM'] = round(((CAMPECHE.loc['CAMPECHE','FM']*100)/totalCAMPECHE),2)
CAMPECHE = CAMPECHE.head()
totalCAMPECHE = CAMPECHE.loc['CAMPECHE','TOTAL']
CAMPECHE1 = CAMPECHE.drop(CAMPECHE.columns[[0,2,3,4,5,6,7,8,9]], axis='columns')
CAMPECHE1 = str(CAMPECHE1.to_json(orient="index")).replace('{','')
CAMPECHE1 = CAMPECHE1.replace(':"','{"')
CAMPECHE1 = CAMPECHE1.replace('}}','},')
CAMPECHE1 = CAMPECHE1.replace('":','" ')
CAMPECHE1 = CAMPECHE1.replace('"CAMPECHE"{"','{"PARTIDO":"')
CAMPECHE1 = CAMPECHE1.split()
CAMPECHE1 = CAMPECHE1[0]+',"PORCENTAJE":'+CAMPECHE1[1]
CAMPECHE2 = CAMPECHE.drop(CAMPECHE.columns[[0,1,3,4,5,6,7,8,9]], axis='columns')
CAMPECHE2 = str(CAMPECHE2.to_json(orient="index")).replace('{','')
CAMPECHE2 = CAMPECHE2.replace(':"','{"')
CAMPECHE2 = CAMPECHE2.replace('}}','},')
CAMPECHE2 = CAMPECHE2.replace('":','" ')
CAMPECHE2 = CAMPECHE2.replace('"CAMPECHE"{"','{"PARTIDO":"')
CAMPECHE2 = CAMPECHE2.split()
CAMPECHE2 = CAMPECHE2[0]+',"PORCENTAJE":'+CAMPECHE2[1]
CAMPECHE3 = CAMPECHE.drop(CAMPECHE.columns[[0,1,2,4,5,6,7,8,9]], axis='columns')
CAMPECHE3 = str(CAMPECHE3.to_json(orient="index")).replace('{','')
CAMPECHE3 = CAMPECHE3.replace(':"','{"')
CAMPECHE3 = CAMPECHE3.replace('}}','}')
CAMPECHE3 = CAMPECHE3.replace('":','" ')
CAMPECHE3 = CAMPECHE3.replace('"CAMPECHE"{"','{"PARTIDO":"')
CAMPECHE3 = CAMPECHE3.split()
CAMPECHE3 = CAMPECHE3[0]+',"PORCENTAJE":'+CAMPECHE3[1]
CAMPECHE = '"CAMPECHE":{ "PRIMERO":'+CAMPECHE1+'"SEGUNDO":'+CAMPECHE2+'"TERCERO":'+CAMPECHE3+"}"

CANDELARIA = pd.DataFrame(df['CANDELARIA'])
CANDELARIA = CANDELARIA.sort_values('CANDELARIA',ascending=False)
CANDELARIA = CANDELARIA.T
totalCANDELARIA = CANDELARIA.loc['CANDELARIA','TOTAL']
CANDELARIA['PES'] = round(((CANDELARIA.loc['CANDELARIA','PES']*100)/totalCANDELARIA),2)
CANDELARIA['PVEM'] = round(((CANDELARIA.loc['CANDELARIA','PVEM']*100)/totalCANDELARIA),2)
CANDELARIA['CI-1'] = round(((CANDELARIA.loc['CANDELARIA','MOR']*100)/totalCANDELARIA),2)
CANDELARIA['MC'] = round(((CANDELARIA.loc['CANDELARIA','MC']*100)/totalCANDELARIA),2)
CANDELARIA['MOR'] = round(((CANDELARIA.loc['CANDELARIA','MOR']*100)/totalCANDELARIA),2)
CANDELARIA['RSP'] = round(((CANDELARIA.loc['CANDELARIA','RSP']*100)/totalCANDELARIA),2)
CANDELARIA['PT'] = round(((CANDELARIA.loc['CANDELARIA','PT']*100)/totalCANDELARIA),2)
CANDELARIA['PAN_PRI_PRD'] = round(((CANDELARIA.loc['CANDELARIA','PAN_PRI_PRD']*100)/totalCANDELARIA),2)
CANDELARIA['FM'] = round(((CANDELARIA.loc['CANDELARIA','FM']*100)/totalCANDELARIA),2)
CANDELARIA = CANDELARIA.head()
totalCANDELARIA = CANDELARIA.loc['CANDELARIA','TOTAL']
CANDELARIA1 = CANDELARIA.drop(CANDELARIA.columns[[0,2,3,4,5,6,7,8,9]], axis='columns')
CANDELARIA1 = str(CANDELARIA1.to_json(orient="index")).replace('{','')
CANDELARIA1 = CANDELARIA1.replace(':"','{"')
CANDELARIA1 = CANDELARIA1.replace('}}','},')
CANDELARIA1 = CANDELARIA1.replace('":','" ')
CANDELARIA1 = CANDELARIA1.replace('"CANDELARIA"{"','{"PARTIDO":"')
CANDELARIA1 = CANDELARIA1.split()
CANDELARIA1 = CANDELARIA1[0]+',"PORCENTAJE":'+CANDELARIA1[1]
CANDELARIA2 = CANDELARIA.drop(CANDELARIA.columns[[0,1,3,4,5,6,7,8,9]], axis='columns')
CANDELARIA2 = str(CANDELARIA2.to_json(orient="index")).replace('{','')
CANDELARIA2 = CANDELARIA2.replace(':"','{"')
CANDELARIA2 = CANDELARIA2.replace('}}','},')
CANDELARIA2 = CANDELARIA2.replace('":','" ')
CANDELARIA2 = CANDELARIA2.replace('"CANDELARIA"{"','{"PARTIDO":"')
CANDELARIA2 = CANDELARIA2.split()
CANDELARIA2 = CANDELARIA2[0]+',"PORCENTAJE":'+CANDELARIA2[1]
CANDELARIA3 = CANDELARIA.drop(CANDELARIA.columns[[0,1,2,4,5,6,7,8,9]], axis='columns')
CANDELARIA3 = str(CANDELARIA3.to_json(orient="index")).replace('{','')
CANDELARIA3 = CANDELARIA3.replace(':"','{"')
CANDELARIA3 = CANDELARIA3.replace('}}','}')
CANDELARIA3 = CANDELARIA3.replace('":','" ')
CANDELARIA3 = CANDELARIA3.replace('"CANDELARIA"{"','{"PARTIDO":"')
CANDELARIA3 = CANDELARIA3.split()
CANDELARIA3 = CANDELARIA3[0]+',"PORCENTAJE":'+CANDELARIA3[1]
CANDELARIA = '"CANDELARIA":{ "PRIMERO":'+CANDELARIA1+'"SEGUNDO":'+CANDELARIA2+'"TERCERO":'+CANDELARIA3+"}"

CARMEN = pd.DataFrame(df['CARMEN'])
CARMEN = CARMEN.sort_values('CARMEN',ascending=False)
CARMEN = CARMEN.T
totalCARMEN = CARMEN.loc['CARMEN','TOTAL']
CARMEN['PES'] = round(((CARMEN.loc['CARMEN','PES']*100)/totalCARMEN),2)
CARMEN['PVEM'] = round(((CARMEN.loc['CARMEN','PVEM']*100)/totalCARMEN),2)
CARMEN['CI-1'] = round(((CARMEN.loc['CARMEN','MOR']*100)/totalCARMEN),2)
CARMEN['MC'] = round(((CARMEN.loc['CARMEN','MC']*100)/totalCARMEN),2)
CARMEN['MOR'] = round(((CARMEN.loc['CARMEN','MOR']*100)/totalCARMEN),2)
CARMEN['RSP'] = round(((CARMEN.loc['CARMEN','RSP']*100)/totalCARMEN),2)
CARMEN['PT'] = round(((CARMEN.loc['CARMEN','PT']*100)/totalCARMEN),2)
CARMEN['PAN_PRI_PRD'] = round(((CARMEN.loc['CARMEN','PAN_PRI_PRD']*100)/totalCARMEN),2)
CARMEN['FM'] = round(((CARMEN.loc['CARMEN','FM']*100)/totalCARMEN),2)
CARMEN = CARMEN.head()
totalCARMEN = CARMEN.loc['CARMEN','TOTAL']
CARMEN1 = CARMEN.drop(CARMEN.columns[[0,2,3,4,5,6,7,8,9]], axis='columns')
CARMEN1 = str(CARMEN1.to_json(orient="index")).replace('{','')
CARMEN1 = CARMEN1.replace(':"','{"')
CARMEN1 = CARMEN1.replace('}}','},')
CARMEN1 = CARMEN1.replace('":','" ')
CARMEN1 = CARMEN1.replace('"CARMEN"{"','{"PARTIDO":"')
CARMEN1 = CARMEN1.split()
CARMEN1 = CARMEN1[0]+',"PORCENTAJE":'+CARMEN1[1]
CARMEN2 = CARMEN.drop(CARMEN.columns[[0,1,3,4,5,6,7,8,9]], axis='columns')
CARMEN2 = str(CARMEN2.to_json(orient="index")).replace('{','')
CARMEN2 = CARMEN2.replace(':"','{"')
CARMEN2 = CARMEN2.replace('}}','},')
CARMEN2 = CARMEN2.replace('":','" ')
CARMEN2 = CARMEN2.replace('"CARMEN"{"','{"PARTIDO":"')
CARMEN2 = CARMEN2.split()
CARMEN2 = CARMEN2[0]+',"PORCENTAJE":'+CARMEN2[1]
CARMEN3 = CARMEN.drop(CARMEN.columns[[0,1,2,4,5,6,7,8,9]], axis='columns')
CARMEN3 = str(CARMEN3.to_json(orient="index")).replace('{','')
CARMEN3 = CARMEN3.replace(':"','{"')
CARMEN3 = CARMEN3.replace('}}','}')
CARMEN3 = CARMEN3.replace('":','" ')
CARMEN3 = CARMEN3.replace('"CARMEN"{"','{"PARTIDO":"')
CARMEN3 = CARMEN3.split()
CARMEN3 = CARMEN3[0]+',"PORCENTAJE":'+CARMEN3[1]
CARMEN = '"CARMEN":{ "PRIMERO":'+CARMEN1+'"SEGUNDO":'+CARMEN2+'"TERCERO":'+CARMEN3+"}"

CHAMPOTON = pd.DataFrame(df['CHAMPOTON'])
CHAMPOTON = CHAMPOTON.sort_values('CHAMPOTON',ascending=False)
CHAMPOTON = CHAMPOTON.T
totalCHAMPOTON = CHAMPOTON.loc['CHAMPOTON','TOTAL']
CHAMPOTON['PES'] = round(((CHAMPOTON.loc['CHAMPOTON','PES']*100)/totalCHAMPOTON),2)
CHAMPOTON['PVEM'] = round(((CHAMPOTON.loc['CHAMPOTON','PVEM']*100)/totalCHAMPOTON),2)
CHAMPOTON['CI-1'] = round(((CHAMPOTON.loc['CHAMPOTON','MOR']*100)/totalCHAMPOTON),2)
CHAMPOTON['MC'] = round(((CHAMPOTON.loc['CHAMPOTON','MC']*100)/totalCHAMPOTON),2)
CHAMPOTON['MOR'] = round(((CHAMPOTON.loc['CHAMPOTON','MOR']*100)/totalCHAMPOTON),2)
CHAMPOTON['RSP'] = round(((CHAMPOTON.loc['CHAMPOTON','RSP']*100)/totalCHAMPOTON),2)
CHAMPOTON['PT'] = round(((CHAMPOTON.loc['CHAMPOTON','PT']*100)/totalCHAMPOTON),2)
CHAMPOTON['PAN_PRI_PRD'] = round(((CHAMPOTON.loc['CHAMPOTON','PAN_PRI_PRD']*100)/totalCHAMPOTON),2)
CHAMPOTON['FM'] = round(((CHAMPOTON.loc['CHAMPOTON','FM']*100)/totalCHAMPOTON),2)
CHAMPOTON = CHAMPOTON.head()
totalCHAMPOTON = CHAMPOTON.loc['CHAMPOTON','TOTAL']
CHAMPOTON1 = CHAMPOTON.drop(CHAMPOTON.columns[[0,2,3,4,5,6,7,8,9]], axis='columns')
CHAMPOTON1 = str(CHAMPOTON1.to_json(orient="index")).replace('{','')
CHAMPOTON1 = CHAMPOTON1.replace(':"','{"')
CHAMPOTON1 = CHAMPOTON1.replace('}}','},')
CHAMPOTON1 = CHAMPOTON1.replace('":','" ')
CHAMPOTON1 = CHAMPOTON1.replace('"CHAMPOTON"{"','{"PARTIDO":"')
CHAMPOTON1 = CHAMPOTON1.split()
CHAMPOTON1 = CHAMPOTON1[0]+',"PORCENTAJE":'+CHAMPOTON1[1]
CHAMPOTON2 = CHAMPOTON.drop(CHAMPOTON.columns[[0,1,3,4,5,6,7,8,9]], axis='columns')
CHAMPOTON2 = str(CHAMPOTON2.to_json(orient="index")).replace('{','')
CHAMPOTON2 = CHAMPOTON2.replace(':"','{"')
CHAMPOTON2 = CHAMPOTON2.replace('}}','},')
CHAMPOTON2 = CHAMPOTON2.replace('":','" ')
CHAMPOTON2 = CHAMPOTON2.replace('"CHAMPOTON"{"','{"PARTIDO":"')
CHAMPOTON2 = CHAMPOTON2.split()
CHAMPOTON2 = CHAMPOTON2[0]+',"PORCENTAJE":'+CHAMPOTON2[1]
CHAMPOTON3 = CHAMPOTON.drop(CHAMPOTON.columns[[0,1,2,4,5,6,7,8,9]], axis='columns')
CHAMPOTON3 = str(CHAMPOTON3.to_json(orient="index")).replace('{','')
CHAMPOTON3 = CHAMPOTON3.replace(':"','{"')
CHAMPOTON3 = CHAMPOTON3.replace('}}','}')
CHAMPOTON3 = CHAMPOTON3.replace('":','" ')
CHAMPOTON3 = CHAMPOTON3.replace('"CHAMPOTON"{"','{"PARTIDO":"')
CHAMPOTON3 = CHAMPOTON3.split()
CHAMPOTON3 = CHAMPOTON3[0]+',"PORCENTAJE":'+CHAMPOTON3[1]
CHAMPOTON = '"CHAMPOTON":{ "PRIMERO":'+CHAMPOTON1+'"SEGUNDO":'+CHAMPOTON2+'"TERCERO":'+CHAMPOTON3+"}"

DZITBALCHE = pd.DataFrame(df['DZITBALCHE'])
DZITBALCHE = DZITBALCHE.sort_values('DZITBALCHE',ascending=False)
DZITBALCHE = DZITBALCHE.T
totalDZITBALCHE = DZITBALCHE.loc['DZITBALCHE','TOTAL']
DZITBALCHE['PES'] = round(((DZITBALCHE.loc['DZITBALCHE','PES']*100)/totalDZITBALCHE),2)
DZITBALCHE['PVEM'] = round(((DZITBALCHE.loc['DZITBALCHE','PVEM']*100)/totalDZITBALCHE),2)
DZITBALCHE['CI-1'] = round(((DZITBALCHE.loc['DZITBALCHE','MOR']*100)/totalDZITBALCHE),2)
DZITBALCHE['MC'] = round(((DZITBALCHE.loc['DZITBALCHE','MC']*100)/totalDZITBALCHE),2)
DZITBALCHE['MOR'] = round(((DZITBALCHE.loc['DZITBALCHE','MOR']*100)/totalDZITBALCHE),2)
DZITBALCHE['RSP'] = round(((DZITBALCHE.loc['DZITBALCHE','RSP']*100)/totalDZITBALCHE),2)
DZITBALCHE['PT'] = round(((DZITBALCHE.loc['DZITBALCHE','PT']*100)/totalDZITBALCHE),2)
DZITBALCHE['PAN_PRI_PRD'] = round(((DZITBALCHE.loc['DZITBALCHE','PAN_PRI_PRD']*100)/totalDZITBALCHE),2)
DZITBALCHE['FM'] = round(((DZITBALCHE.loc['DZITBALCHE','FM']*100)/totalDZITBALCHE),2)
DZITBALCHE = DZITBALCHE.head()
totalDZITBALCHE = DZITBALCHE.loc['DZITBALCHE','TOTAL']
DZITBALCHE1 = DZITBALCHE.drop(DZITBALCHE.columns[[0,2,3,4,5,6,7,8,9]], axis='columns')
DZITBALCHE1 = str(DZITBALCHE1.to_json(orient="index")).replace('{','')
DZITBALCHE1 = DZITBALCHE1.replace(':"','{"')
DZITBALCHE1 = DZITBALCHE1.replace('}}','},')
DZITBALCHE1 = DZITBALCHE1.replace('":','" ')
DZITBALCHE1 = DZITBALCHE1.replace('"DZITBALCHE"{"','{"PARTIDO":"')
DZITBALCHE1 = DZITBALCHE1.split()
DZITBALCHE1 = DZITBALCHE1[0]+',"PORCENTAJE":'+DZITBALCHE1[1]
DZITBALCHE2 = DZITBALCHE.drop(DZITBALCHE.columns[[0,1,3,4,5,6,7,8,9]], axis='columns')
DZITBALCHE2 = str(DZITBALCHE2.to_json(orient="index")).replace('{','')
DZITBALCHE2 = DZITBALCHE2.replace(':"','{"')
DZITBALCHE2 = DZITBALCHE2.replace('}}','},')
DZITBALCHE2 = DZITBALCHE2.replace('":','" ')
DZITBALCHE2 = DZITBALCHE2.replace('"DZITBALCHE"{"','{"PARTIDO":"')
DZITBALCHE2 = DZITBALCHE2.split()
DZITBALCHE2 = DZITBALCHE2[0]+',"PORCENTAJE":'+DZITBALCHE2[1]
DZITBALCHE3 = DZITBALCHE.drop(DZITBALCHE.columns[[0,1,2,4,5,6,7,8,9]], axis='columns')
DZITBALCHE3 = str(DZITBALCHE3.to_json(orient="index")).replace('{','')
DZITBALCHE3 = DZITBALCHE3.replace(':"','{"')
DZITBALCHE3 = DZITBALCHE3.replace('}}','}')
DZITBALCHE3 = DZITBALCHE3.replace('":','" ')
DZITBALCHE3 = DZITBALCHE3.replace('"DZITBALCHE"{"','{"PARTIDO":"')
DZITBALCHE3 = DZITBALCHE3.split()
DZITBALCHE3 = DZITBALCHE3[0]+',"PORCENTAJE":'+DZITBALCHE3[1]
DZITBALCHE = '"DZITBALCHE":{ "PRIMERO":'+DZITBALCHE1+'"SEGUNDO":'+DZITBALCHE2+'"TERCERO":'+DZITBALCHE3+"}"

ESCARCEGA = pd.DataFrame(df['ESCARCEGA'])
ESCARCEGA = ESCARCEGA.sort_values('ESCARCEGA',ascending=False)
ESCARCEGA = ESCARCEGA.T
totalESCARCEGA = ESCARCEGA.loc['ESCARCEGA','TOTAL']
ESCARCEGA['PES'] = round(((ESCARCEGA.loc['ESCARCEGA','PES']*100)/totalESCARCEGA),2)
ESCARCEGA['PVEM'] = round(((ESCARCEGA.loc['ESCARCEGA','PVEM']*100)/totalESCARCEGA),2)
ESCARCEGA['CI-1'] = round(((ESCARCEGA.loc['ESCARCEGA','MOR']*100)/totalESCARCEGA),2)
ESCARCEGA['MC'] = round(((ESCARCEGA.loc['ESCARCEGA','MC']*100)/totalESCARCEGA),2)
ESCARCEGA['MOR'] = round(((ESCARCEGA.loc['ESCARCEGA','MOR']*100)/totalESCARCEGA),2)
ESCARCEGA['RSP'] = round(((ESCARCEGA.loc['ESCARCEGA','RSP']*100)/totalESCARCEGA),2)
ESCARCEGA['PT'] = round(((ESCARCEGA.loc['ESCARCEGA','PT']*100)/totalESCARCEGA),2)
ESCARCEGA['PAN_PRI_PRD'] = round(((ESCARCEGA.loc['ESCARCEGA','PAN_PRI_PRD']*100)/totalESCARCEGA),2)
ESCARCEGA['FM'] = round(((ESCARCEGA.loc['ESCARCEGA','FM']*100)/totalESCARCEGA),2)
ESCARCEGA = ESCARCEGA.head()
totalESCARCEGA = ESCARCEGA.loc['ESCARCEGA','TOTAL']
ESCARCEGA1 = ESCARCEGA.drop(ESCARCEGA.columns[[0,2,3,4,5,6,7,8,9]], axis='columns')
ESCARCEGA1 = str(ESCARCEGA1.to_json(orient="index")).replace('{','')
ESCARCEGA1 = ESCARCEGA1.replace(':"','{"')
ESCARCEGA1 = ESCARCEGA1.replace('}}','},')
ESCARCEGA1 = ESCARCEGA1.replace('":','" ')
ESCARCEGA1 = ESCARCEGA1.replace('"ESCARCEGA"{"','{"PARTIDO":"')
ESCARCEGA1 = ESCARCEGA1.split()
ESCARCEGA1 = ESCARCEGA1[0]+',"PORCENTAJE":'+ESCARCEGA1[1]
ESCARCEGA2 = ESCARCEGA.drop(ESCARCEGA.columns[[0,1,3,4,5,6,7,8,9]], axis='columns')
ESCARCEGA2 = str(ESCARCEGA2.to_json(orient="index")).replace('{','')
ESCARCEGA2 = ESCARCEGA2.replace(':"','{"')
ESCARCEGA2 = ESCARCEGA2.replace('}}','},')
ESCARCEGA2 = ESCARCEGA2.replace('":','" ')
ESCARCEGA2 = ESCARCEGA2.replace('"ESCARCEGA"{"','{"PARTIDO":"')
ESCARCEGA2 = ESCARCEGA2.split()
ESCARCEGA2 = ESCARCEGA2[0]+',"PORCENTAJE":'+ESCARCEGA2[1]
ESCARCEGA3 = ESCARCEGA.drop(ESCARCEGA.columns[[0,1,2,4,5,6,7,8,9]], axis='columns')
ESCARCEGA3 = str(ESCARCEGA3.to_json(orient="index")).replace('{','')
ESCARCEGA3 = ESCARCEGA3.replace(':"','{"')
ESCARCEGA3 = ESCARCEGA3.replace('}}','}')
ESCARCEGA3 = ESCARCEGA3.replace('":','" ')
ESCARCEGA3 = ESCARCEGA3.replace('"ESCARCEGA"{"','{"PARTIDO":"')
ESCARCEGA3 = ESCARCEGA3.split()
ESCARCEGA3 = ESCARCEGA3[0]+',"PORCENTAJE":'+ESCARCEGA3[1]
ESCARCEGA = '"ESCARCEGA":{ "PRIMERO":'+ESCARCEGA1+'"SEGUNDO":'+ESCARCEGA2+'"TERCERO":'+ESCARCEGA3+"}"

HECELCHAKAN = pd.DataFrame(df['HECELCHAKAN'])
HECELCHAKAN = HECELCHAKAN.sort_values('HECELCHAKAN',ascending=False)
HECELCHAKAN = HECELCHAKAN.T
totalHECELCHAKAN = HECELCHAKAN.loc['HECELCHAKAN','TOTAL']
HECELCHAKAN['PES'] = round(((HECELCHAKAN.loc['HECELCHAKAN','PES']*100)/totalHECELCHAKAN),2)
HECELCHAKAN['PVEM'] = round(((HECELCHAKAN.loc['HECELCHAKAN','PVEM']*100)/totalHECELCHAKAN),2)
HECELCHAKAN['CI-1'] = round(((HECELCHAKAN.loc['HECELCHAKAN','MOR']*100)/totalHECELCHAKAN),2)
HECELCHAKAN['MC'] = round(((HECELCHAKAN.loc['HECELCHAKAN','MC']*100)/totalHECELCHAKAN),2)
HECELCHAKAN['MOR'] = round(((HECELCHAKAN.loc['HECELCHAKAN','MOR']*100)/totalHECELCHAKAN),2)
HECELCHAKAN['RSP'] = round(((HECELCHAKAN.loc['HECELCHAKAN','RSP']*100)/totalHECELCHAKAN),2)
HECELCHAKAN['PT'] = round(((HECELCHAKAN.loc['HECELCHAKAN','PT']*100)/totalHECELCHAKAN),2)
HECELCHAKAN['PAN_PRI_PRD'] = round(((HECELCHAKAN.loc['HECELCHAKAN','PAN_PRI_PRD']*100)/totalHECELCHAKAN),2)
HECELCHAKAN['FM'] = round(((HECELCHAKAN.loc['HECELCHAKAN','FM']*100)/totalHECELCHAKAN),2)
HECELCHAKAN = HECELCHAKAN.head()
totalHECELCHAKAN = HECELCHAKAN.loc['HECELCHAKAN','TOTAL']
HECELCHAKAN1 = HECELCHAKAN.drop(HECELCHAKAN.columns[[0,2,3,4,5,6,7,8,9]], axis='columns')
HECELCHAKAN1 = str(HECELCHAKAN1.to_json(orient="index")).replace('{','')
HECELCHAKAN1 = HECELCHAKAN1.replace(':"','{"')
HECELCHAKAN1 = HECELCHAKAN1.replace('}}','},')
HECELCHAKAN1 = HECELCHAKAN1.replace('":','" ')
HECELCHAKAN1 = HECELCHAKAN1.replace('"HECELCHAKAN"{"','{"PARTIDO":"')
HECELCHAKAN1 = HECELCHAKAN1.split()
HECELCHAKAN1 = HECELCHAKAN1[0]+',"PORCENTAJE":'+HECELCHAKAN1[1]
HECELCHAKAN2 = HECELCHAKAN.drop(HECELCHAKAN.columns[[0,1,3,4,5,6,7,8,9]], axis='columns')
HECELCHAKAN2 = str(HECELCHAKAN2.to_json(orient="index")).replace('{','')
HECELCHAKAN2 = HECELCHAKAN2.replace(':"','{"')
HECELCHAKAN2 = HECELCHAKAN2.replace('}}','},')
HECELCHAKAN2 = HECELCHAKAN2.replace('":','" ')
HECELCHAKAN2 = HECELCHAKAN2.replace('"HECELCHAKAN"{"','{"PARTIDO":"')
HECELCHAKAN2 = HECELCHAKAN2.split()
HECELCHAKAN2 = HECELCHAKAN2[0]+',"PORCENTAJE":'+HECELCHAKAN2[1]
HECELCHAKAN3 = HECELCHAKAN.drop(HECELCHAKAN.columns[[0,1,2,4,5,6,7,8,9]], axis='columns')
HECELCHAKAN3 = str(HECELCHAKAN3.to_json(orient="index")).replace('{','')
HECELCHAKAN3 = HECELCHAKAN3.replace(':"','{"')
HECELCHAKAN3 = HECELCHAKAN3.replace('}}','}')
HECELCHAKAN3 = HECELCHAKAN3.replace('":','" ')
HECELCHAKAN3 = HECELCHAKAN3.replace('"HECELCHAKAN"{"','{"PARTIDO":"')
HECELCHAKAN3 = HECELCHAKAN3.split()
HECELCHAKAN3 = HECELCHAKAN3[0]+',"PORCENTAJE":'+HECELCHAKAN3[1]
HECELCHAKAN = '"HECELCHAKAN":{ "PRIMERO":'+HECELCHAKAN1+'"SEGUNDO":'+HECELCHAKAN2+'"TERCERO":'+HECELCHAKAN3+"}"

HOPELCHEN = pd.DataFrame(df['HOPELCHEN'])
HOPELCHEN = HOPELCHEN.sort_values('HOPELCHEN',ascending=False)
HOPELCHEN = HOPELCHEN.T
totalHOPELCHEN = HOPELCHEN.loc['HOPELCHEN','TOTAL']
HOPELCHEN['PES'] = round(((HOPELCHEN.loc['HOPELCHEN','PES']*100)/totalHOPELCHEN),2)
HOPELCHEN['PVEM'] = round(((HOPELCHEN.loc['HOPELCHEN','PVEM']*100)/totalHOPELCHEN),2)
HOPELCHEN['CI-1'] = round(((HOPELCHEN.loc['HOPELCHEN','MOR']*100)/totalHOPELCHEN),2)
HOPELCHEN['MC'] = round(((HOPELCHEN.loc['HOPELCHEN','MC']*100)/totalHOPELCHEN),2)
HOPELCHEN['MOR'] = round(((HOPELCHEN.loc['HOPELCHEN','MOR']*100)/totalHOPELCHEN),2)
HOPELCHEN['RSP'] = round(((HOPELCHEN.loc['HOPELCHEN','RSP']*100)/totalHOPELCHEN),2)
HOPELCHEN['PT'] = round(((HOPELCHEN.loc['HOPELCHEN','PT']*100)/totalHOPELCHEN),2)
HOPELCHEN['PAN_PRI_PRD'] = round(((HOPELCHEN.loc['HOPELCHEN','PAN_PRI_PRD']*100)/totalHOPELCHEN),2)
HOPELCHEN['FM'] = round(((HOPELCHEN.loc['HOPELCHEN','FM']*100)/totalHOPELCHEN),2)
HOPELCHEN = HOPELCHEN.head()
totalHOPELCHEN = HOPELCHEN.loc['HOPELCHEN','TOTAL']
HOPELCHEN1 = HOPELCHEN.drop(HOPELCHEN.columns[[0,2,3,4,5,6,7,8,9]], axis='columns')
HOPELCHEN1 = str(HOPELCHEN1.to_json(orient="index")).replace('{','')
HOPELCHEN1 = HOPELCHEN1.replace(':"','{"')
HOPELCHEN1 = HOPELCHEN1.replace('}}','},')
HOPELCHEN1 = HOPELCHEN1.replace('":','" ')
HOPELCHEN1 = HOPELCHEN1.replace('"HOPELCHEN"{"','{"PARTIDO":"')
HOPELCHEN1 = HOPELCHEN1.split()
HOPELCHEN1 = HOPELCHEN1[0]+',"PORCENTAJE":'+HOPELCHEN1[1]
HOPELCHEN2 = HOPELCHEN.drop(HOPELCHEN.columns[[0,1,3,4,5,6,7,8,9]], axis='columns')
HOPELCHEN2 = str(HOPELCHEN2.to_json(orient="index")).replace('{','')
HOPELCHEN2 = HOPELCHEN2.replace(':"','{"')
HOPELCHEN2 = HOPELCHEN2.replace('}}','},')
HOPELCHEN2 = HOPELCHEN2.replace('":','" ')
HOPELCHEN2 = HOPELCHEN2.replace('"HOPELCHEN"{"','{"PARTIDO":"')
HOPELCHEN2 = HOPELCHEN2.split()
HOPELCHEN2 = HOPELCHEN2[0]+',"PORCENTAJE":'+HOPELCHEN2[1]
HOPELCHEN3 = HOPELCHEN.drop(HOPELCHEN.columns[[0,1,2,4,5,6,7,8,9]], axis='columns')
HOPELCHEN3 = str(HOPELCHEN3.to_json(orient="index")).replace('{','')
HOPELCHEN3 = HOPELCHEN3.replace(':"','{"')
HOPELCHEN3 = HOPELCHEN3.replace('}}','}')
HOPELCHEN3 = HOPELCHEN3.replace('":','" ')
HOPELCHEN3 = HOPELCHEN3.replace('"HOPELCHEN"{"','{"PARTIDO":"')
HOPELCHEN3 = HOPELCHEN3.split()
HOPELCHEN3 = HOPELCHEN3[0]+',"PORCENTAJE":'+HOPELCHEN3[1]
HOPELCHEN = '"HOPELCHEN":{ "PRIMERO":'+HOPELCHEN1+'"SEGUNDO":'+HOPELCHEN2+'"TERCERO":'+HOPELCHEN3+"}"

PALIZADA = pd.DataFrame(df['PALIZADA'])
PALIZADA = PALIZADA.sort_values('PALIZADA',ascending=False)
PALIZADA = PALIZADA.T
totalPALIZADA = PALIZADA.loc['PALIZADA','TOTAL']
PALIZADA['PES'] = round(((PALIZADA.loc['PALIZADA','PES']*100)/totalPALIZADA),2)
PALIZADA['PVEM'] = round(((PALIZADA.loc['PALIZADA','PVEM']*100)/totalPALIZADA),2)
PALIZADA['CI-1'] = round(((PALIZADA.loc['PALIZADA','MOR']*100)/totalPALIZADA),2)
PALIZADA['MC'] = round(((PALIZADA.loc['PALIZADA','MC']*100)/totalPALIZADA),2)
PALIZADA['MOR'] = round(((PALIZADA.loc['PALIZADA','MOR']*100)/totalPALIZADA),2)
PALIZADA['RSP'] = round(((PALIZADA.loc['PALIZADA','RSP']*100)/totalPALIZADA),2)
PALIZADA['PT'] = round(((PALIZADA.loc['PALIZADA','PT']*100)/totalPALIZADA),2)
PALIZADA['PAN_PRI_PRD'] = round(((PALIZADA.loc['PALIZADA','PAN_PRI_PRD']*100)/totalPALIZADA),2)
PALIZADA['FM'] = round(((PALIZADA.loc['PALIZADA','FM']*100)/totalPALIZADA),2)
PALIZADA = PALIZADA.head()
totalPALIZADA = PALIZADA.loc['PALIZADA','TOTAL']
PALIZADA1 = PALIZADA.drop(PALIZADA.columns[[0,2,3,4,5,6,7,8,9]], axis='columns')
PALIZADA1 = str(PALIZADA1.to_json(orient="index")).replace('{','')
PALIZADA1 = PALIZADA1.replace(':"','{"')
PALIZADA1 = PALIZADA1.replace('}}','},')
PALIZADA1 = PALIZADA1.replace('":','" ')
PALIZADA1 = PALIZADA1.replace('"PALIZADA"{"','{"PARTIDO":"')
PALIZADA1 = PALIZADA1.split()
PALIZADA1 = PALIZADA1[0]+',"PORCENTAJE":'+PALIZADA1[1]
PALIZADA2 = PALIZADA.drop(PALIZADA.columns[[0,1,3,4,5,6,7,8,9]], axis='columns')
PALIZADA2 = str(PALIZADA2.to_json(orient="index")).replace('{','')
PALIZADA2 = PALIZADA2.replace(':"','{"')
PALIZADA2 = PALIZADA2.replace('}}','},')
PALIZADA2 = PALIZADA2.replace('":','" ')
PALIZADA2 = PALIZADA2.replace('"PALIZADA"{"','{"PARTIDO":"')
PALIZADA2 = PALIZADA2.split()
PALIZADA2 = PALIZADA2[0]+',"PORCENTAJE":'+PALIZADA2[1]
PALIZADA3 = PALIZADA.drop(PALIZADA.columns[[0,1,2,4,5,6,7,8,9]], axis='columns')
PALIZADA3 = str(PALIZADA3.to_json(orient="index")).replace('{','')
PALIZADA3 = PALIZADA3.replace(':"','{"')
PALIZADA3 = PALIZADA3.replace('}}','}')
PALIZADA3 = PALIZADA3.replace('":','" ')
PALIZADA3 = PALIZADA3.replace('"PALIZADA"{"','{"PARTIDO":"')
PALIZADA3 = PALIZADA3.split()
PALIZADA3 = PALIZADA3[0]+',"PORCENTAJE":'+PALIZADA3[1]
PALIZADA = '"PALIZADA":{ "PRIMERO":'+PALIZADA1+'"SEGUNDO":'+PALIZADA2+'"TERCERO":'+PALIZADA3+"}"

SEYBAPLAYA = pd.DataFrame(df['SEYBAPLAYA'])
SEYBAPLAYA = SEYBAPLAYA.sort_values('SEYBAPLAYA',ascending=False)
SEYBAPLAYA = SEYBAPLAYA.T
totalSEYBAPLAYA = SEYBAPLAYA.loc['SEYBAPLAYA','TOTAL']
SEYBAPLAYA['PES'] = round(((SEYBAPLAYA.loc['SEYBAPLAYA','PES']*100)/totalSEYBAPLAYA),2)
SEYBAPLAYA['PVEM'] = round(((SEYBAPLAYA.loc['SEYBAPLAYA','PVEM']*100)/totalSEYBAPLAYA),2)
SEYBAPLAYA['CI-1'] = round(((SEYBAPLAYA.loc['SEYBAPLAYA','MOR']*100)/totalSEYBAPLAYA),2)
SEYBAPLAYA['MC'] = round(((SEYBAPLAYA.loc['SEYBAPLAYA','MC']*100)/totalSEYBAPLAYA),2)
SEYBAPLAYA['MOR'] = round(((SEYBAPLAYA.loc['SEYBAPLAYA','MOR']*100)/totalSEYBAPLAYA),2)
SEYBAPLAYA['RSP'] = round(((SEYBAPLAYA.loc['SEYBAPLAYA','RSP']*100)/totalSEYBAPLAYA),2)
SEYBAPLAYA['PT'] = round(((SEYBAPLAYA.loc['SEYBAPLAYA','PT']*100)/totalSEYBAPLAYA),2)
SEYBAPLAYA['PAN_PRI_PRD'] = round(((SEYBAPLAYA.loc['SEYBAPLAYA','PAN_PRI_PRD']*100)/totalSEYBAPLAYA),2)
SEYBAPLAYA['FM'] = round(((SEYBAPLAYA.loc['SEYBAPLAYA','FM']*100)/totalSEYBAPLAYA),2)
SEYBAPLAYA = SEYBAPLAYA.head()
totalSEYBAPLAYA = SEYBAPLAYA.loc['SEYBAPLAYA','TOTAL']
SEYBAPLAYA1 = SEYBAPLAYA.drop(SEYBAPLAYA.columns[[0,2,3,4,5,6,7,8,9]], axis='columns')
SEYBAPLAYA1 = str(SEYBAPLAYA1.to_json(orient="index")).replace('{','')
SEYBAPLAYA1 = SEYBAPLAYA1.replace(':"','{"')
SEYBAPLAYA1 = SEYBAPLAYA1.replace('}}','},')
SEYBAPLAYA1 = SEYBAPLAYA1.replace('":','" ')
SEYBAPLAYA1 = SEYBAPLAYA1.replace('"SEYBAPLAYA"{"','{"PARTIDO":"')
SEYBAPLAYA1 = SEYBAPLAYA1.split()
SEYBAPLAYA1 = SEYBAPLAYA1[0]+',"PORCENTAJE":'+SEYBAPLAYA1[1]
SEYBAPLAYA2 = SEYBAPLAYA.drop(SEYBAPLAYA.columns[[0,1,3,4,5,6,7,8,9]], axis='columns')
SEYBAPLAYA2 = str(SEYBAPLAYA2.to_json(orient="index")).replace('{','')
SEYBAPLAYA2 = SEYBAPLAYA2.replace(':"','{"')
SEYBAPLAYA2 = SEYBAPLAYA2.replace('}}','},')
SEYBAPLAYA2 = SEYBAPLAYA2.replace('":','" ')
SEYBAPLAYA2 = SEYBAPLAYA2.replace('"SEYBAPLAYA"{"','{"PARTIDO":"')
SEYBAPLAYA2 = SEYBAPLAYA2.split()
SEYBAPLAYA2 = SEYBAPLAYA2[0]+',"PORCENTAJE":'+SEYBAPLAYA2[1]
SEYBAPLAYA3 = SEYBAPLAYA.drop(SEYBAPLAYA.columns[[0,1,2,4,5,6,7,8,9]], axis='columns')
SEYBAPLAYA3 = str(SEYBAPLAYA3.to_json(orient="index")).replace('{','')
SEYBAPLAYA3 = SEYBAPLAYA3.replace(':"','{"')
SEYBAPLAYA3 = SEYBAPLAYA3.replace('}}','}')
SEYBAPLAYA3 = SEYBAPLAYA3.replace('":','" ')
SEYBAPLAYA3 = SEYBAPLAYA3.replace('"SEYBAPLAYA"{"','{"PARTIDO":"')
SEYBAPLAYA3 = SEYBAPLAYA3.split()
SEYBAPLAYA3 = SEYBAPLAYA3[0]+',"PORCENTAJE":'+SEYBAPLAYA3[1]
SEYBAPLAYA = '"SEYBAPLAYA":{ "PRIMERO":'+SEYBAPLAYA1+'"SEGUNDO":'+SEYBAPLAYA2+'"TERCERO":'+SEYBAPLAYA3+"}"

TENABO = pd.DataFrame(df['TENABO'])
TENABO = TENABO.sort_values('TENABO',ascending=False)
TENABO = TENABO.T
totalTENABO = TENABO.loc['TENABO','TOTAL']
TENABO['PES'] = round(((TENABO.loc['TENABO','PES']*100)/totalTENABO),2)
TENABO['PVEM'] = round(((TENABO.loc['TENABO','PVEM']*100)/totalTENABO),2)
TENABO['CI-1'] = round(((TENABO.loc['TENABO','MOR']*100)/totalTENABO),2)
TENABO['MC'] = round(((TENABO.loc['TENABO','MC']*100)/totalTENABO),2)
TENABO['MOR'] = round(((TENABO.loc['TENABO','MOR']*100)/totalTENABO),2)
TENABO['RSP'] = round(((TENABO.loc['TENABO','RSP']*100)/totalTENABO),2)
TENABO['PT'] = round(((TENABO.loc['TENABO','PT']*100)/totalTENABO),2)
TENABO['PAN_PRI_PRD'] = round(((TENABO.loc['TENABO','PAN_PRI_PRD']*100)/totalTENABO),2)
TENABO['FM'] = round(((TENABO.loc['TENABO','FM']*100)/totalTENABO),2)
TENABO = TENABO.head()
totalTENABO = TENABO.loc['TENABO','TOTAL']
TENABO1 = TENABO.drop(TENABO.columns[[0,2,3,4,5,6,7,8,9]], axis='columns')
TENABO1 = str(TENABO1.to_json(orient="index")).replace('{','')
TENABO1 = TENABO1.replace(':"','{"')
TENABO1 = TENABO1.replace('}}','},')
TENABO1 = TENABO1.replace('":','" ')
TENABO1 = TENABO1.replace('"TENABO"{"','{"PARTIDO":"')
TENABO1 = TENABO1.split()
TENABO1 = TENABO1[0]+',"PORCENTAJE":'+TENABO1[1]
TENABO2 = TENABO.drop(TENABO.columns[[0,1,3,4,5,6,7,8,9]], axis='columns')
TENABO2 = str(TENABO2.to_json(orient="index")).replace('{','')
TENABO2 = TENABO2.replace(':"','{"')
TENABO2 = TENABO2.replace('}}','},')
TENABO2 = TENABO2.replace('":','" ')
TENABO2 = TENABO2.replace('"TENABO"{"','{"PARTIDO":"')
TENABO2 = TENABO2.split()
TENABO2 = TENABO2[0]+',"PORCENTAJE":'+TENABO2[1]
TENABO3 = TENABO.drop(TENABO.columns[[0,1,2,4,5,6,7,8,9]], axis='columns')
TENABO3 = str(TENABO3.to_json(orient="index")).replace('{','')
TENABO3 = TENABO3.replace(':"','{"')
TENABO3 = TENABO3.replace('}}','}')
TENABO3 = TENABO3.replace('":','" ')
TENABO3 = TENABO3.replace('"TENABO"{"','{"PARTIDO":"')
TENABO3 = TENABO3.split()
TENABO3 = TENABO3[0]+',"PORCENTAJE":'+TENABO3[1]
TENABO = '"TENABO":{ "PRIMERO":'+TENABO1+'"SEGUNDO":'+TENABO2+'"TERCERO":'+TENABO3+"}"

result = '{'+CALAKMUL+','+CALKINI+','+CAMPECHE+','+CANDELARIA+','+CARMEN+','+CHAMPOTON+','+DZITBALCHE+','+ESCARCEGA+','+HECELCHAKAN+','+HOPELCHEN+','+PALIZADA+','+SEYBAPLAYA+','+TENABO+'}'
print (result)