import re
import time
import json
from flask_cors import CORS
from flask import Flask, request, flash, jsonify
from etc.data.dtm import dataAyun, dataDip, dataGob, dataGobCand, dataCongreso, removeDS_Store, direcciones, dataTimeds, dataBanner, getDataSet
# from data.dtm import dataAyun, dataDip, dataGob, dataGobCand, dataJuntas

# FLASK Instance my application
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
# CORS(app)

@app.route('/subirVotos', methods=['PUT'])
def put_votos():
    json_data = request.get_json()
    url = json_data['Url']
    getDataSet(url)
    resp = "Los datos han sido actualizados"
    return resp
    
@app.route('/datosAyuntamiento',methods=['GET'])
def get_dataAyun():
    resp = dataAyun()
    return resp

@app.route('/datosDiputaciones',methods=['GET'])
def get_dataDiputaciones():
    # resp = dataDip()
    resp = '{"PT":0,,"MC":0,"PVEM":0,"MOR":5,"PES":0,"RSP":0,"FM":0,"PAN_PRI_PRD":3}'
    return resp

@app.route('/datosGobernatura',methods=['GET'])
def get_dataGob():
    resp = dataGob()
    return resp

@app.route('/candidatosGobernatura',methods=['GET'])
def get_dataGobCand():
    resp = dataGobCand()
    return resp

@app.route('/datosCongreso',methods=['GET'])
def get_dataCongreso():
    # resp = dataCongreso()
    resp = '{"I":{"GANADOR":""},"II":{"GANADOR":""},"III":{"GANADOR":""},"IV":{"GANADOR":""},"V":{"GANADOR":""},"VI":{"GANADOR":""},"VII":{"GANADOR":""},"VIII":{"GANADOR":""},"IX":{"GANADOR":"MOR"},"X":{"GANADOR":""},"XI":{"GANADOR":"MOR"},"XII":{"GANADOR":""},"XIII":{"GANADOR":"PAN_PRI_PRD"},"XIV":{"GANADOR":"MOR"},"XV":{"GANADOR":""},"XVI":{"GANADOR":""},"XVII":{"GANADOR":""},"XVIII":{"GANADOR":"PAN_PRI_PRD"},"XIX":{"GANADOR":""},"XX":{"GANADOR":"PAN_PRI_PRD"},"XXI":{"GANADOR":"MOR"}}'
    return resp

@app.route('/datosBanner',methods=['GET'])
def get_dataBanner():
    resp = dataBanner()
    return resp

@app.route('/desatoraDatos',methods=['GET'])
def get_desatoraDatos():
    removeDS_Store()
    resp = 'DS_Store deleted'
    return resp

@app.route('/directorios',methods=['GET'])
def get_direcciones():
    resp = str(direcciones())
    # resp.status_code=200
    return resp

@app.route('/horaDatos',methods=['GET'])
def get_dataTime():
    resp = dataTimeds()
    # resp.status_code=200
    return resp