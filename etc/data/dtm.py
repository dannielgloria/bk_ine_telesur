import requests
import datetime
import zipfile
from pytz import timezone

def getData():
    utc = timezone('UTC')
    loc = utc.localize(datetime.datetime.now())
    mexico = timezone("America/Mexico_City")
    now = loc.astimezone(mexico)
    date = now.strftime('%Y%m%d_%H%M')

    url = 'https://difusores.prep2021-cam.mx/assets/entregables/55/1/'+ date +'_PREP_CAMP.zip'
    myfile = requests.get(url)
    filename = 'data.zip'
    open(filename,'wb')
    filezp = zipfile.ZipFile('data.zip')
    filezp.extractall('\INE_CAMP')

