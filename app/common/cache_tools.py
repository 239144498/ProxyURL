# -*- coding: utf-8 -*-
# @Time    : 2023/1/12
# @Author  : Naihe
# @Email   : 239144498@qq.com
# @File    : cache_tools.py
# @Software: PyCharm
import time
from base64 import b64encode
import aiohttp
import itertools
import requests
from loguru import *
from threading import *
from collections import *
from urllib.parse import *
from app.conf.config import *
from app.plugins.proxy.tools import *


async def processing(url, data):
    for _temp in data:
        if ".ts" in _temp:
            if is_url(_temp):
                yield "/file.ts?x=" + b64encode(_temp.encode("utf-8")).decode("utf-8")
            else:
                yield "/file.ts/?x=" + b64encode(urljoin(url, _temp).encode("utf-8")).decode("utf-8")
        else:
            if _temp.startswith("#") or len(_temp)==0:
                yield _temp
            # 如果获取的是m3u8列表，则继续进行代理获取
            elif is_url(_temp):
                if "googlevideo.com" in _temp:
                    yield "/ytbproxy?url="+b64encode(_temp.encode("utf-8")).decode("utf-8")
                else:
                    yield "/proxy.m3u8?url=" + _temp
            else:
                yield "/proxy.m3u8?url=" + urljoin(url, _temp)
        yield "\n"


def download(url):
    if _temp_ts := ts_info.get(url):
        return _temp_ts
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
    }
    with requests.get(url=url, headers=header) as res:
        _data = res.content
        ts_info[url] = _data
        return _data


def get_m3u8_down(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0"
    }
    with requests.get(url=url, headers=headers) as res:
        _data = res.text
        return _data


def get_ytb(stream_id):    
    ytburl = f"https://www.youtube.com/watch?v={stream_id}"
    if ytb_stream.get(stream_id) is not None:
        if ytb_stream[stream_id]["expire"] > time.time()-60:            
            logger.success(f"从缓存加载直播源 {stream_id}")
        else:
            logger.info(f"youtube直播源已过期 {stream_id}")
            update_ytb(ytburl,stream_id)
    else:
        logger.info(f"youtube直播源不存在 {stream_id}")
        update_ytb(ytburl,stream_id)        
    stream_url = ytb_stream[stream_id]['stream_url']
    return stream_url


# 获取YouTube直播源
def update_ytb(url,stream_id):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0"
    }
    print(url)
    response = requests.get(url, headers=headers).text
    
    #20230115有效，直接获取链接
    pattern = re.search(r'hlsManifestUrl.+?(https://.+?m3u8)',response)
    stream_url = pattern.group(1)
    pattern2 = re.search(r'expire/(\d{10})',stream_url)
    expire = int(pattern2.group(1)) 
 
    ytb_stream[stream_id] = {"expire":expire,"url":url,"stream_url":stream_url}
    logger.success(f"youtube直播源已更新 {ytb_stream[stream_id]}")
    logger.success(f"总数 {len(ytb_stream.keys())}")
  