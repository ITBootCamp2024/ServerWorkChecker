import time
import requests
from flask import Flask
import schedule

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

def make_requests1():
    requests.get('https://itclusterpython.onrender.com')

def make_requests2():
    requests.get('https://itclusterpython2024.onrender.com')

def make_requests3():
    requests.get('https://itclusterjava.onrender.com/teacher')

if __name__ == '__main__':
    schedule.every(100).seconds.do(make_requests1)
    schedule.every(100).seconds.do(make_requests2)
    schedule.every(100).seconds.do(make_requests3)
    
    while True:
        schedule.run_pending()
        time.sleep(1)  # Затримка, щоб програма не використовувала занадто багато CPU
