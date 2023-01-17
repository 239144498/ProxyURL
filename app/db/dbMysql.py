#!/usr/bin python3

import pymysql
import contextlib

from loguru import *
from pymysql.cursors import *

from app.conf.config import *


class MySQLConnect(object):
    def __init__(self, cursorclass=DictCursor, config=None):
        self.MYSQL_config = config
        self.cursorclass = cursorclass
        self.connection = pymysql.connect(
            host=config['host'],
            port=config['port'],
            user=config['user'],
            password=config['password'],
            db=config['database'],
            cursorclass=cursorclass,
            charset=config['charset'],
        )

    @contextlib.contextmanager
    def cursor(self, cursor=None):
        cursor = self.connection.cursor(cursor)
        try:
            yield cursor
        except Exception as err:
            self.connection.rollback()
            raise err
        finally:
            cursor.close()

    def close(self):
        self.connection.close()

    def fetchone(self, sql=None):
        self.cursor().execute(sql)
        return self.cursor.fetchone()

    def execute(self, sql, value):
        return self.cursor().execute(sql, value)


def get_mysql_conn(cursorclass=DictCursor):
    mysql_config = {
        'host': mysql_cfg['host'],
        'user': mysql_cfg['user'],
        'password': mysql_cfg['password'],
        'port': int(mysql_cfg['port']),
        'database': mysql_cfg['database'],
        'charset': 'utf8'
    }
    return MySQLConnect(cursorclass, mysql_config)



def init_database(cursorclass=DictCursor):
    mysql_config = {
        'host': mysql_cfg['host'],
        'user': mysql_cfg['user'],
        'password': mysql_cfg['password'],
        'port': int(mysql_cfg['port']),
        'database': 'mysql',
        'charset': 'utf8'
    }
    mysql = MySQLConnect(cursorclass, mysql_config)
    sql = "select count(1) cnt from information_schema.TABLE where TABLE_SCHEMA='media' and TABLE_NAME='video'"
    result = mysql.fetchone(sql)

    if result['cnt']:
        logger.info("video表已存在")
    else:
        with mysql.connection.cursor() as cursor:
            cursor.execute('CREATE DATABASE media')
            cursor.execute(
                'create table media.video(vname varchar(100) not null,CONSTRAINT video_pk PRIMARY KEY (vname),vcontent  MEDIUMBLOB NOT NULL,vsize varchar(20) NULL,ctime  timestamp(0) default 1)')
            cursor.execute('SET GLOBAL event_scheduler = ON')
            cursor.execute('DROP event IF EXISTS media.auto_delete')
            cursor.execute('CREATE EVENT media.auto_delete ON SCHEDULE EVERY 30 minute DO TRUNCATE video')

    return '初始化数据库表完成'
