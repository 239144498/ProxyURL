#!/usr/bin python3
# -*- coding: utf-8 -*-
# @Author: Naihe
# @Email: 239144498@qq.com
# @Software: Streaming-Media-Server-Pro
import hashlib
import os
import requests

from app.conf.config import *

requests.packages.urllib3.disable_warnings()


class netreq(object):
    """
    对网络请求进行封装，增加了代理功能
    """

    def __init__(self, proxies=None):
        self.request = requests
        self.proxies = None

    def session(self):
        return requests.session()

    def get(self, url, headers=None):
        return self.request.get(url, headers=headers, proxies=self.proxies)

    def post(self, url, data=None, json=None, headers=None):
        return self.request.post(url, data=data, json=json, headers=headers, proxies=self.proxies)

    def put(self, url, data=None, json=None, headers=None):
        return self.request.put(url, data=data, json=json, headers=headers, proxies=self.proxies)

    def delete(self, url, data=None, json=None, headers=None):
        return self.request.delete(url, data=data, json=json, headers=headers, proxies=self.proxies)


request = netreq()

