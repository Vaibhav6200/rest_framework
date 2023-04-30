import requests


url = "http://127.0.0.1:8000/studentList/1"
# url = "http://127.0.0.1:8000/studentList"
resp = requests.get(url=url)
dict = resp.json()

print(dict)
print(type(dict))