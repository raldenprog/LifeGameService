import requests
import json

data = requests.post('http://127.0.0.1:5000', data={'data': json.dumps({'a': 10, 'b': 15})})
print(data.text)
