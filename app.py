import time
import requests
from flask import Flask
import schedule

app = Flask(__name__)

def make_requests1():
    return requests.get('https://itclusterpython.onrender.com').content

def make_requests2():
    return requests.get('https://itclusterjava.onrender.com/teacher').content

def make_requests3():
    return requests.get('https://itclusterpython2024.onrender.com').content

@app.route('/')
def hello_world():
    return str(make_requests1()) + str(make_requests2()) + str(make_requests3())

if __name__ == '__main__':
    schedule.every(100).seconds.do(make_requests1)
    schedule.every(100).seconds.do(make_requests2)
    schedule.every(100).seconds.do(make_requests3)
    app.run()
