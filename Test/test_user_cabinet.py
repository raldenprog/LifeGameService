# coding: utf8
from api.user_cabinet.cabinet import user_cabinet

def test_user_cabinet(data):
    k = user_cabinet({names.ID_USER : data})
    if (k[names.ANSWER] == names.SUCCESS):
        print("Ok")
    else:
        print("No")