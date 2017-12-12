import datetime
import json
def converter_data(date):
    if isinstance(date, datetime.date):
        return date.__str__()

def converter(js):
    return json.dumps(js, default=converter_data)