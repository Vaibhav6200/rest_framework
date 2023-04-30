import requests
import json

data = {
    'name':'mukund',
    'roll': 167,
    'city': 'udaipur'
}

json_data = json.dumps(data)
URL = "http://127.0.0.1:8000/createStudent/"
resp = requests.post(url = URL, data=json_data)