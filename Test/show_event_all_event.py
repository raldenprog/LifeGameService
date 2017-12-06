# coding: utf8

from api.event.show_event import all_event

def all_event_ok():
    count = 0
    print(all_event(count))

def all_event_negate_error():
    count = -1
    print(all_event(count))

def all_event_notint_error():
    count_json = {
        "hello":'hi'
    }
    count_str = 'hi'
    count_float = 2.28
    print(all_event(count_json))
    print(all_event(count_str))
    print(all_event(count_float))

all_event_ok()
all_event_negate_error()
all_event_notint_error()

