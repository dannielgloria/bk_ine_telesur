import re
import time
import json
from flask import Flask, request, flash, jsonify
from etc.data.dtm import dataAyun, dataDip, dataGob, dataGobCand, dataJuntas, removeDS_Store, direcciones
# from data.dtm import dataAyun, dataDip, dataGob, dataGobCand, dataJuntas

# FLASK Instance my application
app = Flask(__name__)

@app.route('/datosAyuntamiento',methods=['GET'])
def get_dataAyun():
    resp = dataAyun()
    resp.status_code=200
    return resp

@app.route('/datosDiputaciones',methods=['GET'])
def get_dataDiputaciones():
    resp = dataDip()
    resp.status_code=200
    return resp

@app.route('/datosGobernatura',methods=['GET'])
def get_dataGob():
    resp = dataGob()
    resp.status_code=200
    return resp

@app.route('/candidatosGobernatura',methods=['GET'])
def get_dataGobCand():
    resp = dataGobCand()
    resp.status_code=200
    return resp

@app.route('/datosJuntas',methods=['GET'])
def get_dataJuntas():
    resp = dataJuntas()
    resp.status_code=200
    return resp

@app.route('/desatoraDatos',methods=['GET'])
def get_desatoraDatos():
    removeDS_Store()
    resp = 'DS_Store deleted'
    resp.status_code=200
    return resp

@app.route('/directorios',methods=['GET'])
def get_direcciones():
    resp = str(direcciones())
    # resp.status_code=200
    return resp