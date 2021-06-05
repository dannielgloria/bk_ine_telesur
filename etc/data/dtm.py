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
    return json.dumps(parsed, indent=4)

def dataDip():
    content = os.listdir('./etc/data/files')
    # df = pd.read_csv('./etc/data/files/'+content[3]+'/CAMP_DIP_LOC_2021.csv', header=None, sep='\n')
    df = pd.read_csv('./etc/data/files/20210601_1852_PREP_DIP_LOC_CAMP/CAMP_DIP_LOC_2021.csv', header=None, sep='\n')
    df = df[0].str.split(',', expand=True)
    df = df.drop(df.index[[0,1,2,3,4,5]])
    df = df.fillna(0)
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
    co_pan_pri_prd = pan + pri + prd + pan_pri_prd
    pan_pri = pd.to_numeric(df[27]).sum()
    pan_prd = pd.to_numeric(df[28]).sum()
    pri_prd = pd.to_numeric(df[29]).sum()
    no_reg = pd.to_numeric(df[30]).sum()
    data = { "PT":pt,"PVEM":pvem,"MC":mc,"MOR":mor,"PES":pes,"RSP":rsp,"FM":fm,"C_PAN_PRI_PRD": co_pan_pri_prd }
    result = json.dumps(str(data))
    result = json.loads(result)
    result=result.replace("'", '"')
    return result
    

def dataGob():
    content = os.listdir('./etc/data/files')
    # df = pd.read_csv('./etc/data/files/'+content[0]+'/CAMP_GOB_2021.csv', header=None, sep='\n')
    df = pd.read_csv('./etc/data/files/20210601_1852_PREP_GOB_CAMP/CAMP_GOB_2021.csv', header=None, sep='\n')
    df = df[0].str.split(',', expand=True)
    df = df.fillna(0)
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
    data = { "PVEM":{"Name":"SANDRA GUADALUPE","votes":pvem,"percent":pvemP},"MC":{"Name":"ELISEO FERNANDEZ","votes":mc,"percent":mcP},"PES":{"Name":"NIC-THE-HA AGUILERA","votes":pes,"percent":pesP},"RSP":{"Name":"MARIA MAGDALENA","votes":rsp,"percent":rspP},"FM":{"Name":"LUIS ALONSO","votes":fm,"percent":fmP},"C_PAN_PRI_PRD": {"Name":"CHRISTIAN MISHEL","votes":co_pan_pri_prd,"percent":pan_pri_prdP}, "C_PT_MOR":{"Name":"LAYDA ELENA","votes":co_pt_mor,"percent":pt_morP}}
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
    
def dataCongreso():
    content = os.listdir('./etc/data/files')
    # df = pd.read_csv('./etc/data/files/'+content[2]+'/CAMP_DIP_LOC_2021.csv', header=None, sep='\n')
    df = pd.read_csv('./etc/data/files/20210601_1852_PREP_DIP_LOC_CAMP/CAMP_DIP_LOC_2021.csv', header=None, sep='\n')
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
    result = df.to_json(orient="index")
    parsed = json.loads(result)
    a = json.dumps(parsed, indent=4)
    return a

def dataTimeds():
    content = os.listdir('./etc/data/files')
    # df = pd.read_csv('./etc/data/files/'+content[2]+'/CAMP_DIP_LOC_2021.csv', header=None, sep='\n')
    df = pd.read_csv('./etc/data/files/20210601_1852_PREP_DIP_LOC_CAMP/CAMP_DIP_LOC_2021.csv', header=None, sep='\n')
    df = df[0].str.split(',', expand=True)
    df = df.reset_index()
    result = str(df.loc[1,0]).replace(' (UTC-5)', '') 
    result = {'hora':result}
    result = str(result)
    result=result.replace("'", '"')
    return result

def direcciones():
    content = os.listdir('./etc/data/files')
    return content

def removeDS_Store():
    os.remove('./etc/data/files/.DS_Store')
    return ('DS_Store deleted')

print (dataTimeds())