# coding: utf-8
import logging
from api.service import GameService as gs
import api.base_name as names
logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s',
                    level=logging.INFO)


def all_users(count):
    """
    Метод возвращает список пользователей из 10 начиная с переданного параметра
    :param count: int Номер с которого начинать вывод пользователей
    :return: {names.ANSWER: names.SUCCESS, names.DATA: result}
    """
    # TODO: Добавить в базу users количество очков и добавить это поле в SELECT
    sql = "SELECT Name, id_user FROM Users LIMIT 10 OFFSET {}".format(count)
    try:
        if count and isinstance(count, int) and count >= 0:
            result = gs.SqlQuery(sql)
        else:
            logging.error(names.ERROR_EXECUTE_DATABASE)
            return {names.ANSWER: names.ERROR}
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: names.ERROR}
    return {names.ANSWER: names.SUCCESS, names.DATA: result}


def event_users(count, event):
    # TODO: Добавить в базу users количество очков и добавить это поле в SELECT
    # TODO: Добавить условие WHERE для фильтрации по event'ам
    sql = "SELECT Name, id_user FROM Users WHERE id_event={} LIMIT 10 OFFSET {}".format(event, count)
    try:
        result = gs.SqlQuery(sql)
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: names.ERROR}
    return {names.ANSWER: names.SUCCESS, names.DATA: result}


def get_scoreboard(id_event=None):
    """
    Метод выводит текущую таблицу очков
    :return:
    """
    #TODO: Временное решение. Номер события
    id_event = id_event or 2
    sql = """with
user_participation_event as (
  select us.id_user
  , us.name 
  from users us
  inner join participation part 
    on part.id_user = us.id_user
),
sumit_acc as (
  select upe.*
  , sum(tacc.point) as point
  , max(tacc.time) as time
  from task_acc tacc, 
  user_participation_event upe
  where tacc.id_event = {id_event}
  and tacc.id_user = upe.id_user
  group by upe.id_user, upe.name
)

select * from sumit_acc order by point desc, time desc""".format(id_event=id_event)
    try:
        result = gs.SqlQuery(sql)
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: names.ERROR}
    return {names.ANSWER: names.SUCCESS, names.DATA: result}


def get_top_task(id_event=None):
    """
    Метод выводит для каждого таска события топ 3 сдавших флаги
    :return:
    """
    sql = """with
get_task as (
  select id_task, task_name, task_point, task_category 
  from task
  where id_event = {id_event}
),
get_stat as (
  select distinct tacc.id_task
    , array(
    select acc
    from task_acc acc
    where acc.id_event = {id_event}
      and tacc.id_task = acc.id_task
    --order by acc.time
    limit 3
   ) as d
  from task_acc tacc
),
arr_inf_stat as (
  select id_task
    , unnest(d.d) as result
  from (select * from get_stat) as d
),
extract_arr as (
 select (result).id_task 
  , t.task_name as task_name
  , us.name as user_name
  , (result).point as task_point
  , (result).time as task_time
 from arr_inf_stat stat
inner join users us 
    on us.id_user = (result).id_user
inner join task t 
    on t.id_task = (result).id_task
 order by (result).id_task, (result).time
)
select * from extract_arr stat""".format(id_event=id_event)
    try:
        result = gs.SqlQuery(sql)
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: names.ERROR}
    return {names.ANSWER: names.SUCCESS, names.DATA: result}


def get_stat_task(id_task=None, id_event=None):
    """
    Метод выводит для каждого таска события топ 3 сдавших флаги
    :return:
    """
    sql = """with
get_task_acc as (
  select id_task, id_user, time
  from task_acc
  where id_event = {id_event}
    and id_task = {id_task}
  order by time
),
main as (
 select t.task_name as task_name
  , us.name as user_name 
  , tc.id_user 
  , tc.time 
 from get_task_acc tc
inner join users us 
    on us.id_user = tc.id_user
inner join task t 
    on t.id_task = tc.id_task
)
select * from main""".format(id_task=id_task, id_event=id_event)
    try:
        result = gs.SqlQuery(sql)
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: names.ERROR}
    return {names.ANSWER: names.SUCCESS, names.DATA: result}