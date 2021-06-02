import re
import time
import json
from flask import Flask, request, flash, jsonify

# FLASK Instance my application
app = Flask(__name__)