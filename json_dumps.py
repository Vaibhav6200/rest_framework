# JSON dump converts python object into JSON String

import json

dict = {
    'name': 'vaibhav',
    'roll no': 308
}

json_string = json.dumps(dict)
print(json_string)