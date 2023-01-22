# -*- coding: utf-8 -*-
# @Time    : 2022/10/8
# @Author  : Naihe
# @Email   : 239144498@qq.com
# @File    : proxy.py
# @Software: PyCharm
import asyncio
from base64 import *
from threading import *
from loguru import *
from urllib.parse import *
from fastapi.requests import *
from fastapi import *
from fastapi.background import *
from starlette.responses import *
from app.common.cache_tools import *
from app.plugins.proxy.tools import *
from app.plugins.proxy.utile import *
from app.conf.config import *
from app.scheams.response import *


tv = APIRouter(tags=["流媒体代理"])


@tv.get('/proxy.m3u8')
async def proxy(request: Request,
                url: str = Query(..., regex=config.url_regex)):
    """
        ## 用途/Usage
        - 代理任意链接
    """
    url = dict(request.query_params)
    if url.get("url"):
        url = parse(url)
        _data = get_m3u8_down(url)
        return StreamingResponse(processing(url, iter(_data.split("\n"))), 200, headers=headers2)


@tv.get('/file.ts')
async def file(x: str = Query(...)):
    """
        ## 用途/Usage
        - 下载流视频片
    """
    a = b64decode(x.encode("utf-8")).decode("utf-8")
    return Response(content=download(a), status_code=200, headers=headers, media_type='video/MP2T')


@tv.get('/program.m3u')
async def program_proxy():
    """
        ## 用途/Usage
        - 代理频道列表
    """
    with open("app/assets/channel.m3u", "r", encoding="utf-8") as f:
        data = f.read()
        return Response(content=data, status_code=200)


@tv.get('/about')
async def Stream_Proxy_Pro(request: Request):
    """
        ## 接口文档
    """
    return RedirectResponse("http://proxy.naihe.me/docs")


@tv.get('/ytb.m3u8')
async def ytb(request: Request,
              url: str = Query(..., regex="^[0-9A-Za-z]{11}$")):
    """
        ## 用途/Usage
        - 代理youtube直播链接
        - 输入参数为11位ID，如`https://www.youtube.com/watch?v=abcdEFg12H&ab_channel=SPACE%28Official%29`,ID是`abcdEFg12H`
    """
    url = dict(request.query_params)
    if url.get("url"):
        stream_id = parse(url)
        stream_url = get_ytb(stream_id)
        _data = get_m3u8_down(stream_url)
        return StreamingResponse(processing(stream_url, iter(_data.split("\n"))), 200, headers=headers2)

@tv.get('/ytbproxy', summary="代理youtube m3u8")
async def ytbproxy(request: Request, url: str):
    """
    代理youtube链接
    """
    url = dict(request.query_params)
    if url.get("url"):
        url = url.get("url")
        url = b64decode(url.encode("utf-8")).decode("utf-8")
        url = url.replace('=','%3D')
        url = url.replace(';','%3B')
                             
        _data = get_m3u8_down(url)
        return StreamingResponse(processing(url, iter(_data.split("\n"))), 200, headers=headers2)