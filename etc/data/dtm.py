import requests
import datetime
import zipfile
import json
import os
import pandas as pd
from shutil import rmtree
from pytz import timezone


def getDataSet(url):
    # utc = timezone('UTC')
    # loc = utc.localize(datetime.datetime.now())
    # mexico = timezone("America/Mexico_City")
    # now = loc.astimezone(mexico)
    # date = now.strftime('%Y%m%d_%H%M')
    rmtree('./etc/data/files')
    # url = 'https://difusores.prep2021-cam.mx/assets/entregables/55/1/20210601_1852_PREP_CAMP.zip'
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
    carpeta = os.listdir("./etc/data/files/")
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
    df = pd.read_csv('./etc/data/files/'+dirname+'PREP_AYUN_CAMP/CAMP_AYUN_2021.csv', header=None, sep='\n')
    # df = pd.read_csv('./etc/data/files/20210601_1852_PREP_AYUN_CAMP/CAMP_AYUN_2021.csv', header=None, sep='\n')
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
    
    HOPELCHEN = pd.DataFrame(df['HOPELCHEN'])
    HOPELCHEN = HOPELCHEN.sort_values('HOPELCHEN',ascending=False)
    HOPELCHEN = HOPELCHEN.head().T
    HOPELCHEN = HOPELCHEN.drop(HOPELCHEN.columns[[1,2,3,4]], axis='columns')
    HOPELCHEN = str(HOPELCHEN.to_json(orient="index")).replace('{','')
    HOPELCHEN = HOPELCHEN.replace(':"','{"')
    HOPELCHEN = HOPELCHEN.replace('}}','}')
    HOPELCHEN = HOPELCHEN.replace('":','" ')
    HOPELCHEN = HOPELCHEN.replace('"HOPELCHEN"{"','"GANADOR":"')
    HOPELCHEN = HOPELCHEN.split()
    HOPELCHEN = HOPELCHEN[0]
    HOPELCHEN = '"HOPELCHEN":{'+HOPELCHEN+"}"

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

    result = '{'+CALAKMUL+','+CALKINI+','+CAMPECHE+','+CANDELARIA+','+CARMEN+','+CHAMPOTON+','+DZITBALCHE+','+ESCARCEGA+','+HECELCHAKAN+','+HOPELCHEN+','+PALIZADA+','+SEYBAPLAYA+','+TENABO+'}'
    return result

def dataDip():
    carpeta = os.listdir("./etc/data/files/")
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
    df = pd.read_csv('./etc/data/files/'+dirname+'PREP_DIP_LOC_CAMP/CAMP_DIP_LOC_2021.csv', header=None, sep='\n')
    # df = pd.read_csv('./etc/data/files/20210601_1852_PREP_DIP_LOC_CAMP/CAMP_DIP_LOC_2021.csv', header=None, sep='\n')
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
    return result

def dataGob():
    carpeta = os.listdir("./etc/data/files/")
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
    df = pd.read_csv('./etc/data/files/'+dirname+'PREP_GOB_CAMP/CAMP_GOB_2021.csv', header=None, sep='\n')
    # df = pd.read_csv('./etc/data/files/20210601_1852_PREP_GOB_CAMP/CAMP_GOB_2021.csv', header=None, sep='\n')
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
    panP = round(((pan*100)/total),1)
    priP = round(((pri*100)/total),1)
    prdP = round(((prd*100)/total),1)
    ptP = round(((pt*100)/total),1)
    pvemP = round(((pvem*100)/total),1)
    mcP = round(((mc*100)/total),1)
    morP = round(((mor*100)/total),1)
    pesP = round(((pes*100)/total),1)
    rspP = round(((rsp*100)/total),1)
    fmP = round(((fm*100)/total),1)
    pan_pri_prdP = round(((co_pan_pri_prd*100)/total),1)
    pan_priP = round(((pan_pri*100)/total),1)
    pan_prdP = round(((pan_prd*100)/total),1)
    pri_prdP = round(((pri_prd*100)/total),1)
    pt_morP = round(((co_pt_mor*100)/total),1)
    print(total)
    data = { "PVEM":{"Name":"SANDRA GUADALUPE","votes":pvem,"percent":pvemP},"MC":{"Name":"ELISEO FERNANDEZ","votes":mc,"percent":mcP},"PES":{"Name":"NIC-THE-HA AGUILERA","votes":pes,"percent":pesP},"RSP":{"Name":"MARIA MAGDALENA","votes":rsp,"percent":rspP},"FM":{"Name":"LUIS ALONSO","votes":fm,"percent":fmP},"C_PAN_PRI_PRD": {"Name":"CHRISTIAN MISHEL","votes":co_pan_pri_prd,"percent":pan_pri_prdP}, "C_PT_MOR":{"Name":"LAYDA ELENA","votes":co_pt_mor,"percent":pt_morP}}
    result = json.dumps(str(data))
    result = json.loads(result)
    result=result.replace("'", '"')
    return result

def dataGobCand():
    carpeta = os.listdir("./etc/data/files/")
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
    df = pd.read_csv('./etc/data/files/'+dirname+'PREP_GOB_CAMP/CAMP_GOB_CANDIDATURA_2021.csv')
    # df = pd.read_csv('./etc/data/files/20210601_1852_PREP_GOB_CAMP/CAMP_GOB_CANDIDATURA_2021.csv')
    df = df.drop(columns=['ID_ESTADO'])
    df = df.set_index('PARTIDO_CI')
    result = str(df.to_json())
    result = result.replace('{"CANDIDATURA_PROPIETARIA":', '')
    result = result.replace('"}}', '"}')
    result = json.loads(result)
    return result
    
def dataCongreso():
    carpeta = os.listdir("./etc/data/files/")
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
    df = pd.read_csv('./etc/data/files/'+dirname+'PREP_DIP_LOC_CAMP/CAMP_DIP_LOC_2021.csv', header=None, sep='\n')
    # df = pd.read_csv('./etc/data/files/20210601_1852_PREP_DIP_LOC_CAMP/CAMP_DIP_LOC_2021.csv', header=None, sep='\n')
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
    return result

def dataTimeds():
    carpeta = os.listdir("./etc/data/files/")
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
    # content = os.listdir('./etc/data/files')
    df = pd.read_csv('./etc/data/files/'+dirname+'PREP_DIP_LOC_CAMP/CAMP_DIP_LOC_2021.csv', header=None, sep='\n')
    # df = pd.read_csv('./etc/data/files/20210601_1852_PREP_DIP_LOC_CAMP/CAMP_DIP_LOC_2021.csv', header=None, sep='\n')
    df = df[0].str.split(',', expand=True)
    df = df.reset_index()
    result = str(df.loc[1,0]).replace(' (UTC-5)', '') 
    result = result.replace('/',' ')
    result = result.split()
    result = 'Junio ' + result[0] + '       ' + result[3]
    print (result)
    result = {'hora':result}
    result = str(result)
    result=result.replace("'", '"')
    return result

def dataBanner():
    carpeta = os.listdir("./etc/data/files/")
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
    df = pd.read_csv('./etc/data/files/'+dirname+'PREP_AYUN_CAMP/CAMP_AYUN_2021.csv', header=None, sep='\n')
    # df = pd.read_csv('./etc/data/files/20210601_1852_PREP_AYUN_CAMP/CAMP_AYUN_2021.csv', header=None, sep='\n')
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
    return result
    
def direcciones():
    content = os.listdir('./etc/data/files') 
    return content

def removeDS_Store():
    os.remove('./etc/data/files/.DS_Store')
    return ('DS_Store deleted')
