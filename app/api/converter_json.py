from datetime import date
import json


def __converter_data(param):
    if isinstance(param, date):
        return param.strftime('%d.%m.%Y')


def converter(js):

    return json.dumps(js, default=__converter_data) if isinstance(js, dict) \
        else json.loads(js)
