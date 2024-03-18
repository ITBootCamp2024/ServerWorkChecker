import time
import requests
from flask import Flask
import schedule

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
    
def make_requests1():
    return str(requests.get('https://itclusterpython.onrender.com').text)
def make_requests2():
    return str(requests.get('https://itclusterpython2024.onrender.com').text)
def make_requests3():
    return str(requests.get('https://itclusterjava.onrender.com/teacher').text)

schedule.every(100).seconds.do(make_requests1)
schedule.every(100).seconds.do(make_requests2)
schedule.every(100).seconds.do(make_requests3)

if __name__ == '__main__':
    app.run()
