# -*- coding: utf-8 -*-
# @Time    : 2022/10/22
# @Author  : Naihe
# @Email   : 239144498@qq.com
# @File    : api_model.py
# @Software: PyCharm
from enum import *


class y(str, Enum):
    f = "1"
    s = "2"
    c = "3"
    h = "4"


class x(str, Enum):
    a = "1"
    b = "2"
    c = "3"
    d = "4"


class z(str, Enum):
    yes = "y"
    no = "n"
