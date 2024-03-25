import threading
import time
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    filename = 'images/1618010991_9-p-bushuyushchee-more-fentezi-9.jpg'
    return send_file(filename, mimetype='image/jpg')

if __name__ == '__main__':
    app.run()
