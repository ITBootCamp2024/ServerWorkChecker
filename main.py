import time
import requests

while True:
    timing = time.time()
    if time.time() - timing > 100.0:
        timing = time.time()
        response = requests.get('https://itclusterpython.onrender.com')
        response = requests.get('https://itclusterpython2024.onrender.com')
        response = requests.get('https://itclusterjava.onrender.com/teacher')