__author__ = 'ar.chusovitin'
from api.database.connect_db import db_connect_new as db


def SqlQuery(query):
    connect, current_connect = db()
    result = None
    try:
        #print(query)
        current_connect.execute(query)
        connect.commit()
    except:
        return result
    finally:
        try:
            result = current_connect.fetchall()
        except:
            return result
        connect.close()
        return result