import requests
import datetime
import zipfile
import os
from shutil import rmtree
from pytz import timezone


utc = timezone('UTC')
loc = utc.localize(datetime.datetime.now())
mexico = timezone("America/Mexico_City")
now = loc.astimezone(mexico)
date = now.strftime('%Y%m%d_%H%M')

rmtree('./files')
# url = 'https://difusores.prep2021-cam.mx/assets/entregables/55/1/'+ date +'_PREP_CAMP.zip'
url = 'https://difusores.prep2021-cam.mx/assets/entregables/55/1/20210601_1852_PREP_CAMP.zip'
myfile = requests.get(url)
# filename = date + '_PREP_CAMP.zip'
filename = '2021.zip'
zfile = open(filename,'wb')
zfile.write(myfile.content)
zfile.close()
content = os.listdir('./')
 # filezp = zipfile.ZipFile( date + '_PREP_CAMP.zip')
filezp = zipfile.ZipFile(content[1])
filezp.extractall('./files')
content = os.listdir('./files')
for n in content:
    filezp = zipfile.ZipFile('./files/'+n)
    file = n.replace('.zip', '') 
    print(file)
    filezp.extractall('./files/'+file)
    os.remove('./files/'+ n)