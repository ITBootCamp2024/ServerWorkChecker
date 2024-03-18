import time
import requests
from flask import Flask
import schedule

app = Flask(__name__)

def make_requests1():
    return requests.get('https://itclusterpython.onrender.com').content

def make_requests2():
    return requests.get('itclusterjava.onrender.com/teacher').content

def make_requests3():
    return requests.get('https://itclusterpython2024.onrender.com').content
    
@app.route('/')
def hello_world():
   return str(make_requests1()) + str(make_requests2()) + str(make_requests3())

