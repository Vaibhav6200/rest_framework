import requests
import json

URL = "http://127.0.0.1:8000/get_student/"

# READ Operation
def getData(id=None):
    data = {}
    if id is not None:
        data = {"id": id}

    json_data = json.dumps(data)
    resp = requests.get(url=URL, data=json_data)
    response_data = resp.json()
    print(response_data)

getData()
# getData(1)


# CREATE Operation
def post_data(data):
    json_data = json.dumps(data)
    resp = requests.post(url=URL, data=json_data)
    print(resp.json())


# create_data = {
#     'name': 'mukund',
#     'roll': 167,
#     'city': 'ahmedabad'
# }
# post_data(create_data)


# UPDATE Operation (PUT)
def put_data(data):
    json_data = json.dumps(data)
    resp = requests.put(url=URL, data=json_data)
    print(resp.json())

# update_data = {
#     'id': 4,
#     'name': 'eshant',
#     'roll': 39,
#     'city': 'ahmedabad'
# }

# put_data(update_data)


def delete_data(data):
    json_data = json.dumps(data)
    resp = requests.delete(url=URL, data=json_data)
    print(resp.json())


# del_data = {
#     "id": 3
# }
# delete_data(del_data)