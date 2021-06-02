import re
import time
import json
from flask_cors import CORS
from flask import Flask, request, flash, jsonify
from etc.data.dtm import dataAyun, dataDip, dataGob, dataGobCand, dataJuntas, removeDS_Store, direcciones
# from data.dtm import dataAyun, dataDip, dataGob, dataGobCand, dataJuntas

# FLASK Instance my application
app = Flask(__name__)
CORS(app)

@app.route('/datosAyuntamiento',methods=['GET'])
@cross_origin()
def get_dataAyun():
    resp = dataAyun()
    resp = json.loads(resp)
    return resp

@app.route('/datosDiputaciones',methods=['GET'])
@cross_origin()
def get_dataDiputaciones():
    resp = dataDip()
    resp = json.loads(resp)
    return resp

@app.route('/datosGobernatura',methods=['GET'])
@cross_origin()
def get_dataGob():
    resp = dataGob()
    resp = json.loads(resp)
    return resp

@app.route('/candidatosGobernatura',methods=['GET'])
@cross_origin()
def get_dataGobCand():
    resp = dataGobCand()
    resp = json.loads(resp)
    return resp

@app.route('/datosJuntas',methods=['GET'])
@cross_origin()
def get_dataJuntas():
    resp = dataJuntas()
    resp = json.loads(resp)
    return resp

@app.route('/desatoraDatos',methods=['GET'])
@cross_origin()
def get_desatoraDatos():
    removeDS_Store()
    resp = 'DS_Store deleted'
    return resp

@app.route('/directorios',methods=['GET'])
@cross_origin()
def get_direcciones():
    resp = str(direcciones())
    # resp.status_code=200
    return resp