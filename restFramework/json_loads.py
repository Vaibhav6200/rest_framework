# json.loads(data): used to parse json string

import json

dict = {
    'name': 'vaibhav',
    'roll no': 308
}

jsonString = json.dumps(dict)
jsonLoads = json.loads(jsonString)

print(type(jsonString))
print(type(jsonLoads))