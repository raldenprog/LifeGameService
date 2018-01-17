#for other OS


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


def connect_db(data):
    try:
        connect, current_connect = db_connect()
        current_connect.execute("SELECT * FROM users where id = '{}'".format(
                        data['id']
                    ))
        connect.commit()
        connect.close()
        result = current_connect.fetchall()[0]
        return {names.ANSWER: "Ok",
                names.DATA: result}
    except:
        return {names.ANSWER: names.ERROR}

print (connect_db(data))
