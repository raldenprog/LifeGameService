import json
import pprint
import requests

def all_event_OK():
    dataOK = {'id_event': 0}
    r = requests.get('http://0.0.0.0:13451/event', data=dataOK)
    pprint.pprint(json.loads(r.text))

def all_event_NO():
    dataNO1 = {'user': "Anton"}
    r = requests.get('http://0.0.0.0:13451/event', data=dataNO1)
    pprint.pprint(json.loads(r.text))
    dataNO2 = {'login':'test'}
    r = requests.get('http://0.0.0.0:13451/event', data=dataNO2)
    pprint.pprint(json.loads(r.text))

all_event_OK()
print()
all_event_NO()