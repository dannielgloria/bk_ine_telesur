import requests
import datetime
import zipfile
import json
import os
import pandas as pd
from shutil import rmtree
from pytz import timezone

df = pd.read_csv('./files/20210601_1852_PREP_GOB_CAMP/CAMP_GOB_2021.csv', header=None, sep='\n')
df = df[0].str.split(',', expand=True)
df = df.drop(df.index[[0,1,2,3,4,5]])
total = pd.to_numeric(df[34]).sum()
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
pt_mor = pd.to_numeric(df[30]).sum()
no_reg = pd.to_numeric(df[31]).sum()
panP = (pan*100)/total
priP = (pri*100)/total
prdP = (prd*100)/total
ptP = (pt*100)/total
pvemP = (pvem*100)/total
mcP = (mc*100)/total
morP = (mor*100)/total
pesP = (pes*100)/total
rspP = (rsp*100)/total
fmP = (fm*100)/total
pan_pri_prdP = (pan_pri_prd*100)/total
pan_priP = (pan_pri*100)/total
pan_prdP = (pan_prd*100)/total
pri_prdP = (pri_prd*100)/total
pt_morP = (pt_mor*100)/total
no_regP = (no_reg*100)/total
print(total)
data = { "PAN":{"Name":"none","votes":pan,"percent":panP},"PRI":{"Name":"none","votes":pri,"percent":priP},"PRD":{"Name":"none","votes":prd,"percent":prdP},"PT":{"Name":"none","votes":pt,"percent":ptP},"PVEM":{"Name":"none","votes":pvem,"percent":pvemP},"MC":{"Name":"ELISEO FERNANDEZ MONTUFAR","votes":mc,"percent":mcP},"MOR":{"Name":"none","votes":mor,"percent":morP},"PES":{"Name":"NIC-THE-HA AGUILERA SILVA","votes":pes,"percent":pesP},"RSP":{"Name":"MARIA MAGDALENA COCOM ARBEZ","votes":rsp,"percent":rspP},"FM":{"Name":"LUIS ALONSO GARCIA HERNANDEZ","votes":fm,"percent":fmP},"C_PAN_PRI_PRD": {"Name":"CHRISTIAN MISHEL CASTRO BELLO","votes":pan_pri_prd,"percent":pan_pri_prdP}, "C_PAN_PRI":{"Name":"none","votes":pan_pri,"percent":pan_priP},"C_PAN_PRD":{"Name":"none","votes":pan_prd,"percent":pan_prdP}, "C_PRI_PRD": {"Name":"none","votes":pri_prd,"percent":pri_prdP}, "C_PT_MOR":{"Name":"LAYDA ELENA SANSORES SAN ROMAN","votes":pt_mor,"percent":pt_morP},"NO_REGISTRADOS": {"Name":"none","votes":no_reg,"percent":no_regP} }
result = json.dumps(str(data))
result = json.loads(result)
result=result.replace("'", '"')
print (result)