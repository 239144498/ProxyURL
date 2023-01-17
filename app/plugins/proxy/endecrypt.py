#!/usr/bin python3
# -*- coding: utf-8 -*-
import hashlib
from urllib.parse import *
import aiohttp
import asyncio
from loguru import *
from app.plugins.proxy.tools import *
from app.conf.config import *


async def get4gtvurl(fsid):
    _a = now_time()
    url = urljoin(data3['a3'], "?type=v5".format(fsid))
    data = {"t": _a - tx, "fid": fsid, "v": config.VERSION}
    header = {
        "Accept": "*/*",
        "User-Agent": machine,
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "v": hashlib.md5(bytes(str(data) + mdata, 'utf8')).hexdigest(),
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, data=data, headers=header) as res:
            logger.success(f"{fsid} {res.status}")
            try:
                _ = await res.json()
                return res.status, data["xx"], data['xxxxx'], _a, "xxxx"
            except:
                return res.status, None, res.xxx, _a, ""


