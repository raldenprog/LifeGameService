import json
import os

with open("description.json", 'r') as f:
    data = f.read()
    data = json.loads(data)

event_name = data["event"]
category = data["category"]
task_name = data["name"]
description = data["description"]
points = data["points"]
flag = data["flag"]
links = data["links"]
authors = str('Author is ' + data["authors"][0]["name"] + ', team ' + data["authors"][0]["team"])
file_name = str(task_name + '.' + points)

if os.path.isdir(event_name) == False:
    os.mkdir(event_name)
os.chdir(event_name)

if os.path.isdir(category) == False:
    os.mkdir(category)
os.chdir(category)

if os.path.isdir(file_name) == False:
    os.mkdir(file_name)
os.chdir(file_name)

s = open("Description.md", 'w')
s.write(description)
s.write('\r\n')
s.write(links)
s.write('\r\n')
s.write(authors)
s.close()

print(flag)
s = open("Flag.md", 'w')
s.write(flag)
s.close()
