#for other OS
from app.api.database.connect_db import db_connect

#for Linux
'''
import sys
import os
directory_user_cabinet= os.getcwd()
directory_user_cabinet=directory_user_cabinet.split("Test")[0]
directory_user_cabinet+="app/api/database"
print (directory_user_cabinet)
sys.path.insert(0, directory_user_cabinet)
from connect_db import db_connect
'''

data = {
        "id": "1"
        }
current_connect = db_connect().cursor()
current_connect.execute("SELECT * FROM users where id = '{}'".format(
                data['id']
            ))
db_connect().commit()
result = current_connect.fetchall()
print (result)
print ("OK")
