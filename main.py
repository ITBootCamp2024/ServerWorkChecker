import time
import requests
from flask import Flask
import schedule

main = Flask(__name__)

@main.route('/')
def index():
    return 'Hello, world!'

def make_requests():
    response = requests.get('https://itclusterpython.onrender.com')
    response = requests.get('https://itclusterpython2024.onrender.com')
    response = requests.get('https://itclusterjava.onrender.com/teacher')

schedule.every(100).seconds.do(make_requests)

if __name__ == '__main__':
    main.run()
