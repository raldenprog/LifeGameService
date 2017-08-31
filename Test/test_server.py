import requests
import json

data = requests.post('http://127.0.0.1:5000/auth', data={'data': json.dumps({'Login': 'Anton', 'Password': 'PassAnton'})})
print(data.text)
