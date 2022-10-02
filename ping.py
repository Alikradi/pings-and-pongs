import json
from multiprocessing import reduction
import requests, random
from flask import Flask, jsonify, request 
from requests.auth import HTTPDigestAuth
from flask_httpauth import HTTPDigestAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key here'
auth = HTTPDigestAuth()

users={ "vcu" : "rams"}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/ping', methods=['GET'])
@auth.login_required
def ping():
    a = requests.get('http://127.0.0.1:5000/pong', auth= ('vcu', 'rams'))
    b = a.elapsed.total_seconds()
    c = b * 1000
    return jsonify(c)