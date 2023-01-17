# -*- coding: utf-8 -*-
# @Time    : 2022/10/12
# @Author  : Naihe
# @Email   : 239144498@qq.com
# @File    : tasks.py
# @Software: PyCharm
from loguru import *

from app.plugins.proxy.utile import *
from app.db.localfile import *


def gotask():
    get.filename.clear()


def sqltask():
    # 保留最新100条缓存，避免长时间运行内存溢出
    keys = list(get.filename)
    keys.reverse()
    _ = {}
    if len(keys) > 100:
        for index, element in enumerate(keys):
            if index < 100:
                _.update({element: get.filename.get(element)})
        get.filename = _
    logger.success("删除完成")


def filetask():
    cnt = vfile.clean_file()
    logger.success('成功删除文件'+str(cnt)+'个')


if __name__ == '__main__':
    gotask()
