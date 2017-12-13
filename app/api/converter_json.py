from datetime import datetime
import json


def __converter_data(date):
    if isinstance(date, datetime):
        return date.strftime('%d.%m.%Y')


def converter(js):

    return json.dumps(js, default=__converter_data) if isinstance(js, dict) \
        else json.loads(js)
