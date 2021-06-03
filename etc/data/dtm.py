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

