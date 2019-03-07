__author__ = 'RaldenProg'

import requests as rq
from random import choice
from string import ascii_uppercase
from api.service import GameService as gs
import json

URL = "http://192.168.1.3:13451"


class MegaTest:
    def __init__(self):
        self.login = ''.join(choice(ascii_uppercase) for i in range(12))
        self.name_event = ''.join(choice(ascii_uppercase) for i in range(12))
        self.task_name = ''.join(choice(ascii_uppercase) for i in range(12))
        self.UUID = None

    def all_event(self):
        try:
            print("all_event: ", end="")
            data = {"UUID": "0fc1d179-1b23-47dc-b83a-b3270b544c3d", "Page": 0}
            data = json.loads(rq.get('{url}/event?data={query}'.format(url=URL, query=data).replace('\'', '%22')).text)
            if data["Answer"] == 'Success' and data["Data"] is not None:
                print("OK")
            else:
                print("NO")
        except:
            print("NO")

    def registration(self):
        try:
            print("registration: ", end="")
            data = {"Login": self.login, "Password": "password", "Name": "new_name", "Email": "new_email",
                    "City": "new_city", "Educational": "new_ed", "Logo_name": "new_logo_name", "Logo": "new_logo",
                    "Sex": "Man"}
            req = json.loads(rq.get('{url}/registration?data={query}'.format(url=URL, query=data).replace('\'', '%22')).text)
            self.UUID = req["Data"]["UUID"]
            if req["Answer"] == 'Success':
                print("OK")
            else:
                print("NO")
        except:
            print("NO")

    def auth(self):
        try:
            print("auth: ", end="")
            data = {"Login": 'raldenprog', "Password": 'raldenprog'}
            req = json.loads(rq.get('{url}/auth?data={query}'.format(url=URL, query=data).replace('\'', '%22')).text)
            if req["Answer"] == 'Success':
                print("OK")
            else:
                print("NO")
        except:
            print("NO")

    def find_event(self):
        try:
            print("find_event: ", end="")
            data = {"Name": "Mostevent", "Page": 0}
            req = json.loads(
                rq.get('{url}/event?param=find&data={query}'.format(url=URL, query=data).replace('\'', '%22')).text)
            if req != 'Error':  # TODO: Возможно могут быть другие варианты ответа
                print("OK")
            else:
                print("NO")
        except:
            print("NO")

    def check_task(self):
        try:
            print("check_task: ", end="")
            data = {"Task_id": "148", "Task_flag": "CTF{test}", "UUID": "0fc1d179-1b23-47dc-b83a-b3270b544c3d",
                    "id_event": "7"}
            req = json.loads(
                rq.get('{url}/task?param=check&data={query}'.format(url=URL, query=data).replace('\'', '%22')).text)
            if req["Answer"] == 'Success':
                print("OK")
            else:
                print("NO")
        except:
            print("NO")

    def get_task_event(self):
        try:
            print("get_task_event: ", end="")
            data = {"id_event": "7", "UUID": "0fc1d179-1b23-47dc-b83a-b3270b544c3d"}
            req = json.loads(rq.get('{url}/task?data={query}'.format(url=URL, query=data).replace('\'', '%22')).text)
            if req["Answer"] == 'Success':
                print("OK")
            else:
                print("NO")
        except:
            print("NO")

    def cabinet(self):
        try:
            print("cabinet: ", end="")
            data = {"UUID": "0fc1d179-1b23-47dc-b83a-b3270b544c3d"}
            req = json.loads(rq.get('{url}/cabinet?data={query}'.format(url=URL, query=data).replace('\'', '%22')).text)
            if req["Answer"] == 'Success':
                print("OK")
            else:
                print("NO")
        except:
            print("NO")

    def edit_cabinet(self):
        try:
            print("edit_cabinet: ", end="")
            data = {"UUID":"0fc1d179-1b23-47dc-b83a-b3270b544c3d","Name":"new_name","Surname":"new_surname",
                    "Email":"new_email","City":"new_city","Educational":"new_ed", "Logo_name":"new_logo_name",
                    "Logo":"new_logo", "Sex":"Man"}
            req = json.loads(rq.get('{url}/cabinet?param=edit&data={query}'.format(url=URL, query=data).replace('\'', '%22')).text)
            if req["Answer"] == 'Success':
                print("OK")
            else:
                print("NO")
        except:
            print("NO")

    def change_password(self):
        try:
            print("change_password: ", end="")
            data = {"UUID":"0fc1d179-1b23-47dc-b83a-b3270b544c3d", "Old_password":"new_password",
                    "New_password":"new_password"}
            req = json.loads(rq.get('{url}/cabinet?param=new_password&data={query}'.format(url=URL, query=data).replace('\'', '%22')).text)
            if req["Answer"] == 'Success':
                print("OK")
            else:
                print("NO")
        except:
            print("NO")

    def registration_event(self):
        try:
            print("registration_event: ", end="")

            data = {"Name":self.name_event,"Description":"test","Logo":"test","Status":"1","Date_start":"2018-04-14","Date_end":"2018-04-15",
                    "Date_stop":"2018-04-14", "Date_continue":"2018-04-14"}
            req = json.loads(rq.get('{url}/event?param=registration&data={query}'.format(url=URL, query=data).replace('\'', '%22')).text)
            if req["Answer"] == 'Success':
                print("OK")
            else:
                print("NO")
        except:
            print("NO")

    def update_event(self):
        try:
            print("update_event: ", end="")
            data = {"id_event": "7", "Name": "test_new_event4", "Description": "test", "Logo": "test", "Status": "1",
                    "Date_start": "2018-04-14", "Date_end": "2018-04-15", "Date_stop": "2018-04-14",
                    "Date_continue": "2018-04-14"}
            req = json.loads(rq.get('{url}/event?param=update&data={query}'.format(url=URL, query=data).replace('\'', '%22')).text)
            if req["Answer"] == 'Success':
                print("OK")
            else:
                print("NO")
        except:
            print("NO")

    def create_one_task(self):
        try:
            print("create_one_task: ", end="")
            data = {"task_category":"crypto","task_name":self.task_name,"task_flag":"CTF{test}","task_description":"test","task_point":"100",
                    "task_hint":"test","task_solve":"0", "task_link":"http:test", "status":"1", "public_status":"1","id_event":"7"}
            req = json.loads(rq.get('{url}/task?param=create&data={query}'.format(url=URL, query=data).replace('\'', '%22')).text)
            if req["Answer"] == 'Success':
                print("OK")
            else:
                print("NO")
        except:
            print("NO")

    def scoreboard(self):
        try:
            print("scoreboard: ", end="")
            data = {"id_event":"7"}
            req = json.loads(rq.get('{url}/scoreboard?data={query}'.format(url=URL, query=data).replace('\'', '%22')).text)
            if req["Answer"] == 'Success':
                print("OK")
            else:
                print("NO")
        except:
            print("NO")

    def reg_user_for_an_event(self):
        try:
            print("reg_user_for_an_event: ", end="")
            data = {"UUID":self.UUID, "id_event":"5"}
            req = json.loads(rq.get('{url}/event?param=reg_user&data={query}'.format(url=URL, query=data).replace('\'', '%22')).text)
            if req["Answer"] == 'Success':
                print("OK")
            else:
                print("NO")
        except:
            print("NO")
    def page_event(self):
        try:
            print("page_event: ", end="")
            data = {"id_event": 7}
            req = json.loads(rq.get('{url}/event?param=descr&data={query}'.format(url=URL, query=data).replace('\'', '%22')).text)
            print(req)
            if req["Answer"] == 'Success':
                print("OK")
            else:
                print("NO")
        except:
            print("NO")

test = MegaTest()
"""test.all_event()
test.registration()
test.auth()
test.find_event()
test.check_task()
test.get_task_event()
test.cabinet()
test.edit_cabinet()
test.change_password()
test.registration_event()
test.update_event()
test.create_one_task()
test.scoreboard()
test.reg_user_for_an_event()
"""
test.auth()
