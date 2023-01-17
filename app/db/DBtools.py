#!/usr/bin python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/7
# @Author  : Naihe
# @Email   : 239144498@qq.com
# @File    : dbMysql.py
# @Software: PyCharm
import pymysql
import redis
from loguru import *

from app.conf.config import *
from app.db.dbMysql import *

def mysql_connect_test():
    try:
        logger.success("mysql")
        return DBconnect
    except pymysql.err.OperationalError as e:
        logger.error("mysql")
        return DBconnect


if defaultdb == "mysql":
    try:
        logger.success("已创建")
    except pymysql.err.OperationalError as e:
        logger.error("失败")
    DBconnect, sqlState = mysql_connect_test()
else:
    DBconnect = None
    sqlState = False
    logger.warning("mysql")