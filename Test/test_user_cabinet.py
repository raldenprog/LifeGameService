# coding: utf8
from api.user_cabinet.cabinet import user_cabinet

def test_user_cabinet(data):
    k = user_cabinet({"id_user" : data})
    if (k["Answer"] == "Success"):
        print("Ok")
    else:
        print("No")