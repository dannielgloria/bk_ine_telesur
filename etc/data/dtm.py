import requests
import datetime
import zipfile
import json
import os
import pandas as pd
from shutil import rmtree
from pytz import timezone

def getDataSet():
    # utc = timezone('UTC')
    # loc = utc.localize(datetime.datetime.now())
    # mexico = timezone("America/Mexico_City")
    # now = loc.astimezone(mexico)
    # date = now.strftime('%Y%m%d_%H%M')
    rmtree('./etc/data/files')
    url = 'https://difusores.prep2021-cam.mx/assets/entregables/55/1/20210601_1852_PREP_CAMP.zip'
    myfile = requests.get(url)
    filename = '2021.zip'
    zfile = open(filename,'wb')
    zfile.write(myfile.content)
    zfile.close()
    content = os.listdir('./')
    filezp = zipfile.ZipFile('2021.zip')
    filezp.extractall('./etc/data/files')
    content = os.listdir('./etc/data/files')
    for n in content:
        filezp = zipfile.ZipFile('./etc/data/files/'+n)
        file = n.replace('.zip', '') 
        print(file)
        filezp.extractall('./etc/data/files/'+file)
        os.remove('./etc/data/files/'+ n)

def dataAyun():
    #     os.remove('./etc/data/files/.DS_Store')
    content = os.listdir('./etc/data/files')
    df = pd.read_csv('./etc/data/files/'+content[0]+'/CAMP_AYUN_2021.csv', header=None, sep='\n')
    df = df[0].str.split(',', expand=True)
    df = df.drop(df.index[[0,1,2,3,4]])
    total = df[34].sum()
    pan = df[16].sum()
    pri = df[17].sum()
    prd = df[18].sum()
    pt = df[19].sum()
    pvem = df[20].sum()
    mc = df[21].sum()
    mor = df[22].sum()
    pes = df[23].sum()
    rsp = df[24].sum()
    fm = df[25].sum()
    cand_ind = df[26].sum()
    pan_pri_prd = df[27].sum()
    pan_pri = df[28].sum()
    pan_prd = df[29].sum()
    pri_prd = df[30].sum()
    no_reg = df[31].sum()
    data = { "PAN":pan,"PRI":pri,"PRD":prd,"PT":pt,"PVEM":pvem,"MC":mc,"MOR":mor,"PES":pes,"RSP":rsp,"FM":fm,"CAND_IND": cand_ind,"C_PAN_PRI_PRD": pan_pri_prd, "C_PAN_PRI":pan_pri,"C_PAN_PRD": pan_prd, "C_PRI_PRD": pri_prd,"NO_REGISTRADOS": no_reg }
    result = json.dumps(data)
    return result
    
def dataAyunCand():
    result = "esto no sirve jsjsjsjsjsjs"
    return result

def dataDip():
    content = os.listdir('./etc/data/files')
    df = pd.read_csv('./etc/data/files/'+content[1]+'/CAMP_DIP_LOC_2021.csv', header=None, sep='\n')
    df = df[0].str.split(',', expand=True)
    df = df.drop(df.index[[0,1,2,3,4]])
    total = df[33].sum()
    pan = df[16].sum()
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
    no_reg = df[30].sum()
    data = { "PAN":pan,"PRI":pri,"PRD":prd,"PT":pt,"PVEM":pvem,"MC":mc,"MOR":mor,"PES":pes,"RSP":rsp,"FM":fm,"C_PAN_PRI_PRD": pan_pri_prd, "C_PAN_PRI":pan_pri,"C_PAN_PRD": pan_prd, "C_PRI_PRD": pri_prd,"NO_REGISTRADOS": no_reg }
    result = json.dumps(data)
    return result
    
def dataDipCand():
    result = "esto no sirve jsjsjsjsjsjs"
    return result

def dataGob():
    content = os.listdir('./etc/data/files')
    df = pd.read_csv('./etc/data/files/'+content[2]+'/CAMP_GOB_2021.csv', header=None, sep='\n')
    df = df[0].str.split(',', expand=True)
    df = df.drop(df.index[[0,1,2,3,4]])
    total = df[34].sum()
    pan = df[16].sum()
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
    no_reg = df[31].sum()
    data = { "PAN":pan,"PRI":pri,"PRD":prd,"PT":pt,"PVEM":pvem,"MC":mc,"MOR":mor,"PES":pes,"RSP":rsp,"FM":fm,"C_PAN_PRI_PRD": pan_pri_prd, "C_PAN_PRI":pan_pri,"C_PAN_PRD": pan_prd, "C_PRI_PRD": pri_prd, "C_PT_MOR": pt_mor,"NO_REGISTRADOS": no_reg }
    result = json.dumps(data)
    return result

def dataGobCand():
    content = os.listdir('./etc/data/files')
    df = pd.read_csv('/etc/data/files/'+content[2]+'/CAMP_GOB_CANDIDATURA_2021.csv')
    df = df.drop(columns=['ID_ESTADO'])
    df = df.set_index('PARTIDO_CI')
    result = df.to_json()
    return result
    
def dataJuntas():
    content = os.listdir('./etc/data/files')
    df = pd.read_csv('./etc/data/files/'+content[3]+'/CAMP_JUNTAS_2021.csv', header=None, sep='\n')
    df = df[0].str.split(',', expand=True)
    df = df.drop(df.index[[0,1,2,3,4]])
    total = df[33].sum()
    pan = df[16].sum()
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
    no_reg = df[30].sum()
    data = { "PAN":pan,"PRI":pri,"PRD":prd,"PT":pt,"PVEM":pvem,"MC":mc,"MOR":mor,"PES":pes,"RSP":rsp,"FM":fm,"C_PAN_PRI_PRD": pan_pri_prd, "C_PAN_PRI":pan_pri,"C_PAN_PRD": pan_prd, "C_PRI_PRD": pri_prd,"NO_REGISTRADOS": no_reg }
    return data

def dataJuntasCand():
    result = "esto no sirve jsjsjsjsjsjs"
    return result

def removeDS_Store():
    os.remove('./etc/data/files/.DS_Store')
    return ('DS_Store deleted')

