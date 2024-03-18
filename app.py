import time
import requests
from flask import Flask
import schedule

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
    
def make_requests1():
    response = requests.get('https://itclusterpython.onrender.com')
    app.logger.info('Request to itclusterpython.onrender.com: %s', response.status_code)
    
def make_requests2():
    response = requests.get('https://itclusterpython2024.onrender.com')
    app.logger.info('Request to itclusterpython2024.onrender.com: %s', response.status_code)
    
def make_requests3():
    response = requests.get('https://itclusterjava.onrender.com/teacher')
    app.logger.info('Request to itclusterjava.onrender.com/teacher: %s', response.status_code)

schedule.every(100).seconds.do(make_requests1)
schedule.every(100).seconds.do(make_requests2)
schedule.every(100).seconds.do(make_requests3)

if __name__ == '__main__':
    app.run()
