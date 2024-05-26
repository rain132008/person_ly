import logging

from sqlalchemy.exc import OperationalError

from wxcloudrun import db
from wxcloudrun.model import Counters, GreenUser

# 初始化日志
logger = logging.getLogger('log')


def query_counterbyid(id):
    """
    根据ID查询Counter实体
    :param id: Counter的ID
    :return: Counter实体
    """
    try:
        return Counters.query.filter(Counters.id == id).first()
    except OperationalError as e:
        logger.info("query_counterbyid errorMsg= {} ".format(e))
        return None


def delete_counterbyid(id):
    """
    根据ID删除Counter实体
    :param id: Counter的ID
    """
    try:
        counter = Counters.query.get(id)
        if counter is None:
            return
        db.session.delete(counter)
        db.session.commit()
    except OperationalError as e:
        logger.info("delete_counterbyid errorMsg= {} ".format(e))


def insert_counter(counter):
    """
    插入一个Counter实体
    :param counter: Counters实体
    """
    try:
        db.session.add(counter)
        db.session.commit()
    except OperationalError as e:
        logger.info("insert_counter errorMsg= {} ".format(e))


def update_counterbyid(counter):
    """
    根据ID更新counter的值
    :param counter实体
    """
    try:
        counter = query_counterbyid(counter.id)
        if counter is None:
            return
        db.session.flush()
        db.session.commit()
    except OperationalError as e:
        logger.info("update_counterbyid errorMsg= {} ".format(e))


def insert_user(user):
    """
    插入一个user实体
    :param user: GreenUser实体
    """
    try:
        db.session.add(user)
        db.session.commit()
    except OperationalError as e:
        logger.info("insert_user errorMsg= {} ".format(e))


def query_userbyid(user_id):
    """
    根据ID查询user实体
    :param user_id: user的ID
    :return: user实体
    """
    try:
        return GreenUser.query.filter(GreenUser.user_id == user_id).first()
    except OperationalError as e:
        logger.info("query_userbyid errorMsg= {} ".format(e))
        return None


def update_user(user):
    """
    根据ID更新user的值
    :param user实体
    """
    try:
        user = query_userbyid(user.user_id)
        if user is None:
            return
        db.session.flush()
        db.session.commit()
    except OperationalError as e:
        logger.info("update_user errorMsg= {} ".format(e))