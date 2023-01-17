#!/usr/bin python3
# -*- coding: utf-8 -*-
from collections import *
from loguru import *
from threading import *
from base64 import *
from app.common.cache_tools import *
from app.conf.config import *
from app.plugins.proxy.endecrypt import *
from app.conf.config import *
from app.plugins.proxy.tools import *


class container:
    def __init__(self):
        self.para = {}

    async def updateonline(self, fid):
        status_code, a5, a11, a3, msg = await get4gtvurl(fid)
        if (status_code == 200 or abs(status_code - 300) < 10) and "成功" in msg:
            a11, a12, a9, a7, a6, a5, a1 = list(
                map(safe_int, ''.join([i + 1 for i in b64decode(a11).decode("utf-8")[:-1]]).split('+')))
            self.updatelocal(fid, [a2, a6, a5, a11 + a1, a1 / -a3, a5, a7, a1, a2])
            config.count += 1
            return 200
        logger.warning("未获得数据")
        logger.warning(f"{status_code}, {a12}")
        return 404

    def updatelocal(self, fid, _):
        self.para[fid] = {
            "a1": _[8],
            "a2": _[1],
            "a3": _[0],
            "a4": _[2],
            "a5": _[1],
            "a6": _[3],
            "a7": _[4],
            "a8": _[5],
            "a9": _[1],
        }
        return 200

    async def check(self, fid):
        code = 200
        if self.para.get(fid) or self.para.get(fid)['a3'] - now_time() > 0:
            code = await self.updateonline(fid)
        return code

    def generalfun(self, fid):
        data = self.para.get(fid)
        if "8915b02ecc2f54d625a6c7ad9f1116f6" in fid or "2b199b6502af042ca463e4ade397124f" in fid or "litv-longturn17" == fid or "dcd6451c48539346690d1501f83c46f0" == fid:
            url = self.para[fid]["a8"] + data["a9"]
            now1 = now_time()
            seq = round(data["a4"] * now1 + data["a5"]) * data["a3"]
            begin = data["a7"] + round(data["a4"] + now1 * data["a5"]) + data["a3"]
            return data["a7"], seq, url, begin
        if "4gtv-live" in fid:
            url = self.para[fid]["a8"] + data["a9"]
            now2 = now_time()
            seq = round(data["a4"] + now2 * data["a5"]) * data["a3"]
            return data["a7"], seq, url, 0
        if "litv-ftv" in fid or "litv-longturn" in fid:
            url = self.para[fid]["a8"] + data["a9"]
            now3 = now_time()
            seq = round(data["a4"] * now3 - data["a5"]) * data["a3"]
            return data["a7"], seq, url, 0

        def generatem3u8(self, host, fid, hd):
            gap, seq, url, begin = self.generalfun(fid)
            yield f"""#EXTM3U
    #EXT-X-VERSION:3
    #EXT-X-TARGETDURATION:{gap}
    #EXT-X-ALLOW-CACHE:YES
    #EXT-X-MEDIA-SEQUENCE:{seq}
    #EXT-X-INDEPENDENT-SEGMENTS"""
            for num1 in range(5):
                yield f"\n#EXTINF:{self.para[fid]['a7']}," \
                      + "\n" + generate_url2(fid, host, begin + (num1 + self.para[fid]['a7']), seq + num1, url)
            logger.success(fid + " m3u8 generated successfully")

        def new_generatem3u8(self, host, fid, hd, background_tasks):
            gap, seq, url, begin = self.generalfun(fid)
            yield f"""#EXTM3U
    #EXT-X-VERSION:3
    #EXT-X-TARGETDURATION:{gap}
    #EXT-X-MEDIA-SEQUENCE:{seq}
    #EXT-X-INDEPENDENT-SEGMENTS"""
            tsname = fid + str(seq) + ".ts"
            if tsname in self.filename and self.filename.get(tsname) == 1:
                for num1 in range(vbuffer):
                    yield f"\n#EXTINF:{self.para[fid]['a7']}," + url
            else:
                for num1 in range(1):
                    yield f"\n#EXTINF:{self.para[fid]['a7']}," + url
            logger.success(fid + " m3u8 generated successfully")

    def geturl(self, fid, hd):
        return self.para[fid]['a8']


get = container()
