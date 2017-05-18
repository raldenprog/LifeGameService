import pymysql
import logging


logging.basicConfig(filename='logger.log',
                    format='%(asctime)s %(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s',
                    level=logging.INFO)

def empty_task_data():
    return { "id" :             "Unchecked",
            "task_category" :   "Unchecked",
            "task_name" :       "Unchecked",
            "task_flag" :       "Unchecked",
            "task_description" :"Unchecked",
            "task_point" :      "Unchecked",
            "task_hint" :       "Unchecked",
            "task_solve" :      "Unchecked",
            "task_link" :       "Unchecked",
            "database" :        "Unchecked"
            }


def create_one_task(data):
    check_data = empty_task_data()
    try:
        if data["id"] is None:
            logging.info('Incorrect parameter \'id\' - None')
            check_data["id"] = "Empty"
            return {"answer": "Error",
                    "data" : check_data}
        else:
            check_data["id"] = "Checked"
    except:
        logging.error('Fatal error in function \'create_one_task\', param \'id\'')
        return {"answer": "Error",
                "data": check_data}

    try:
        if data["task_category"] is None:
            logging.info('Incorrect parameter \'task_category\'- None')
            check_data["task_category"] = "Empty"
            return {"answer": "Error",
                    "data": check_data}
        else:
            check_data["task_category"] = "Checked"
    except:
        logging.error('Fatal error in function \'create_one_task\', param \'task_category\'')
        return {"answer": "Error",
                "data": check_data}

    try:
        if data["task_name"] is None:
            logging.info('Incorrect parameter \'task_name\'- None')
            check_data["task_name"] = "Empty"
            return {"answer": "Error",
                    "data": check_data}
        else:
            check_data["task_name"] = "Checked"
    except:
        logging.error('Fatal error in function \'create_one_task\', param \'task_name\'')
        return {"answer": "Error",
                "data": check_data}

    try:
        if data["task_flag"] is None:
            logging.info('Incorrect parameter \'task_flag\'- None')
            check_data["task_flag"] = "Empty"
            return {"answer": "Error",
                    "data": check_data}
        else:
            check_data["task_flag"] = "Checked"
    except:
        logging.error('Fatal error in function \'create_one_task\', param \'task_flag\'')
        return {"answer": "Error",
                "data": check_data}

    try:
        if data["task_description"] is None:
            logging.info('Incorrect parameter \'task_description\'- None')
            check_data["task_description"] = "Empty"
            return {"answer": "Error",
                    "data": check_data}
        else:
            check_data["task_description"] = "Checked"
    except:
        logging.error('Fatal error in function \'create_one_task\', param \'task_description\'')
        return {"answer": "Error",
                "data": check_data}

    try:
        if data["task_point"] is None:
            logging.info('Incorrect parameter \'task_point\'- None')
            check_data["task_point"] = "Empty"
            return {"answer": "Error",
                    "data": check_data}
        else:
            check_data["task_point"] = "Checked"
    except:
        logging.error('Fatal error in function \'create_one_task\', param \'task_point\'')
        return {"answer": "Error",
                "data": check_data}

    try:
        if data["task_hint"] is None:
            logging.info('Incorrect parameter \'task_hint\'- None')
            check_data["task_hint"] = "Empty"
            return {"answer": "Error",
                    "data": check_data}
        else:
            check_data["task_hint"] = "Checked"
    except:
        logging.error('Fatal error in function \'create_one_task\', param \'task_hint\'')
        return {"answer": "Error",
                "data": check_data}

    try:
        if data["task_solve"] is None:
            logging.info('Incorrect parameter \'task_solve\'- None')
            check_data["task_solve"] = "Empty"
            return {"answer": "Error",
                    "data": check_data}
        else:
            check_data["task_solve"] = "Checked"
    except:
        logging.error('Fatal error in function \'create_one_task\', param \'task_solve\'')
        return {"answer": "Error",
                "data": check_data}

    try:
        if data["task_link"] is None:
            logging.info('Incorrect parameter \'task_link\'- None')
            check_data["task_link"] = "Empty"
            return {"answer": "Error",
                    "data": check_data}
        else:
            check_data["task_link"] = "Checked"
    except:
        logging.error('Fatal error in function \'create_one_task\', param \'task_link\'')
        return {"answer": "Error",
                "data": check_data}

    try:
        connect = pymysql.connect(host='5.137.232.44',
                                  user='dev_life_user',
                                  password='pinlox123',
                                  db='life_game_service_database',
                                  cursorclass=pymysql.cursors.DictCursor)
        current_connect = connect.cursor()
        check_data["database"] = "Connected"
    except:
        check_data["database"] = "Disconnected"
        logging.error('Fatal error in function \'create_one_task\', param \'database\' disconnected')
        return {"answer": "Error",
                "data": check_data}
    else:
        try:
            sql = "INSERT INTO task" \
                " VALUES (null,\"{id}\",\"{task_category}\",\"{task_name}\"," \
                "\"{task_flag}\",\"{task_description}\",\"{task_point}\",\"{task_hint}\"," \
                "\"{task_solve}\",\"{task_link}\")".format(**data)
            print(sql)
            current_connect.execute(sql)
            connect.commit()
            connect.close()
            check_data["database"] = "Recorded"
        except:
            print('aaa')
            logging.error('Fatal error in function \'create_one_task\', param \'sql\' can\'t create new record')
            check_data["database"] = "Unrecorded"
            return {"answer": "Error",
                    "data": check_data}

    return {"answer": "Ok",
            "data": check_data}

def create_few_tasks(batch_data):
    answers = []
    try:
        if len(batch_data) <= 0:
            print (len(batch_data))
            return {"answer": "Error",
                    "data": empty_task_data(),
                    "number": 0}
    except:
        print "Except 1"
        logging.error('Fatal error in function \'create_few_tasks\', param \'batch_data\'')
        return {"answer": "Error",
                "data": empty_task_data(),
                "number": 0}

    try:
        counter = 0
        for data in batch_data:
            answer = create_one_task(data)
            answers.append(answer)
            if answer["answer"] is not "Ok":
                return {"answer": "Error",
                        "data": answer,
                        "number":counter + 1}
            counter = counter + 1
    except:
        print "Except 2"
        logging.error('Fatal error in function \'create_few_tasks\', param \'data\'')
        return {"answer": "Error",
                "data": empty_task_data(),
                "number": 0}

    return {"answer": "Ok",
            "data": answers,
            "number": len(batch_data)}

json = {    "id" :              "1",
            "task_category" :   2,
            "task_name" :       3,
            "task_flag" :       4,
            "task_description" :5,
            "task_point" :      6,
            "task_hint" :       7,
            "task_solve" :      8,
            "task_link" :       9
        },{    "id" :              "11",
            "task_category" :   21,
            "task_name" :       31,
            "task_flag" :       41,
            "task_description" :51,
            "task_point" :      62,
            "task_hint" :       73,
            "task_solve" :      84,
            "task_link" :       95
            }

print create_few_tasks(json)