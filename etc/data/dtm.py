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
    # df = pd.read_csv('./etc/data/files/'+content[1]+'/CAMP_AYUN_2021.csv', header=None, sep='\n')
    df = pd.read_csv('./etc/data/files/20210601_1852_PREP_AYUN_CAMP/CAMP_AYUN_2021.csv', header=None, sep='\n')
    df = df[0].str.split(',', expand=True)
    df = df.drop(df.index[[0,1,2,3,4,5]])
    df = df.reset_index()
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
    cand_ind = pd.to_numeric(df[26]).sum()
    pan_pri_prd = pd.to_numeric(df[27]).sum()
    pan_pri = pd.to_numeric(df[28]).sum()
    pan_prd = pd.to_numeric(df[29]).sum()
    pri_prd = pd.to_numeric(df[30]).sum()
    no_reg = pd.to_numeric(df[31]).sum()
    data = { "PAN":pan,"PRI":pri,"PRD":prd,"PT":pt,"PVEM":pvem,"MC":mc,"MOR":mor,"PES":pes,"RSP":rsp,"FM":fm,"CAND_IND": cand_ind,"C_PAN_PRI_PRD": pan_pri_prd, "C_PAN_PRI":pan_pri,"C_PAN_PRD": pan_prd, "C_PRI_PRD": pri_prd,"NO_REGISTRADOS": no_reg }
    result = json.dumps(str(data))
    result = json.loads(result)
    result=result.replace("'", '"')
    return result

def dataDip():
    content = os.listdir('./etc/data/files')
    # df = pd.read_csv('./etc/data/files/'+content[3]+'/CAMP_DIP_LOC_2021.csv', header=None, sep='\n')
    df = pd.read_csv('./etc/data/files/20210601_1852_PREP_DIP_LOC_CAMP/CAMP_DIP_LOC_2021.csv', header=None, sep='\n')
    df = df[0].str.split(',', expand=True)
    df = df.drop(df.index[[0,1,2,3,4,5]])
    total = pd.to_numeric(df[33]).sum()
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
    result = json.dumps(str(data))
    result = json.loads(result)
    result=result.replace("'", '"')
    return result
    

def dataGob():
    content = os.listdir('./etc/data/files')
    # df = pd.read_csv('./etc/data/files/'+content[0]+'/CAMP_GOB_2021.csv', header=None, sep='\n')
    df = pd.read_csv('./etc/data/files/20210601_1852_PREP_GOB_CAMP/CAMP_GOB_2021.csv', header=None, sep='\n')
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
    co_pan_pri_prd = pan + pri + prd + pan_pri_prd
    co_pt_mor = pt + mor + pt_mor
    panP = round(((pan*100)/total),2)
    priP = round(((pri*100)/total),2)
    prdP = round(((prd*100)/total),2)
    ptP = round(((pt*100)/total),2)
    pvemP = round(((pvem*100)/total),2)
    mcP = round(((mc*100)/total),2)
    morP = round(((mor*100)/total),2)
    pesP = round(((pes*100)/total),2)
    rspP = round(((rsp*100)/total),2)
    fmP = round(((fm*100)/total),2)
    pan_pri_prdP = round(((co_pan_pri_prd*100)/total),2)
    pan_priP = round(((pan_pri*100)/total),2)
    pan_prdP = round(((pan_prd*100)/total),2)
    pri_prdP = round(((pri_prd*100)/total),2)
    pt_morP = round(((co_pt_mor*100)/total),2)
    print(total)
    data = { "MC":{"Name":"ELISEO FERNANDEZ","votes":mc,"percent":mcP},"RSP":{"Name":"MARIA MAGDALENA","votes":rsp,"percent":rspP},"FM":{"Name":"LUIS ALONSO","votes":fm,"percent":fmP},"C_PAN_PRI_PRD": {"Name":"CHRISTIAN MISHEL","votes":co_pan_pri_prd,"percent":pan_pri_prdP}, "C_PT_MOR":{"Name":"LAYDA ELENA","votes":pt_mor,"percent":pt_morP}}
    result = json.dumps(str(data))
    result = json.loads(result)
    result=result.replace("'", '"')
    return result

def dataGobCand():
    content = os.listdir('./etc/data/files')
    # df = pd.read_csv('./etc/data/files/'+content[0]+'/CAMP_GOB_CANDIDATURA_2021.csv')
    df = pd.read_csv('./etc/data/files/20210601_1852_PREP_GOB_CAMP/CAMP_GOB_CANDIDATURA_2021.csv')
    df = df.drop(columns=['ID_ESTADO'])
    df = df.set_index('PARTIDO_CI')
    result = str(df.to_json())
    result = result.replace('{"CANDIDATURA_PROPIETARIA":', '')
    result = result.replace('"}}', '"}')
    result = json.loads(result)
    return result
    
def dataJuntas():
    content = os.listdir('./etc/data/files')
    # df = pd.read_csv('./etc/data/files/'+content[2]+'/CAMP_JUNTAS_2021.csv', header=None, sep='\n')
    df = pd.read_csv('./etc/data/files/20210601_1852_PREP_JUNTAS_CAMP/CAMP_JUNTAS_2021.csv', header=None, sep='\n')
    df = df[0].str.split(',', expand=True)
    df = df.drop(df.index[[0,1,2,3,4,5]])
    total = pd.to_numeric(df[33]).sum()
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
    result = json.dumps(str(data))
    result = json.loads(result)
    result=result.replace("'", '"')
    return result

def direcciones():
    content = os.listdir('./etc/data/files')
    return content

def removeDS_Store():
    os.remove('./etc/data/files/.DS_Store')
    return ('DS_Store deleted')

