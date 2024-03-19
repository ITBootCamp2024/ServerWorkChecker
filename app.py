import threading
import time
import requests
from flask import Flask

app = Flask(__name__)

def make_requests1():
    return requests.get('https://itclusterpython.onrender.com').content

def make_requests2():
    return requests.get('https://itclusterjava.onrender.com/teacher').content

def make_requests3():
    return requests.get('https://itclusterpython2024.onrender.com').content

def checker_thread():
    while True:
        print(str(make_requests1()) + str(make_requests2()) + str(make_requests3()))
        time.sleep(5)

@app.route('/')
def hello_world():
    return 'Server is running'

if __name__ == '__main__':
    x = threading.Thread(target=checker_thread)
    x.daemon = True
    x.start()
    app.run(debug=True)
