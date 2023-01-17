#!/usr/bin python3
# -*- coding: utf-8 -*-
import time

import hashlib
import re
from urllib.parse import *

from app.conf import *
from app.common.request import *
from app.conf.config import *


def safe_int(s):
    return int(s)


def generate_m3u(host, hd, name):
    yield '#6818c8b25ccbb33acf9c65338f6f2592=""\n'
    for k, v in gdata.items():
        yield -1, v['xx'], k, v['xx'], v["xx"], v['xx'], v['xx']


def writefile(filename, content):
    with open(filename, "w") as f:
        f.write(content)


def get_4gtv(url):
    with request.get(url=url) as res:
        return res.text


def generate_url(fid, host, begin, seq, url):
    if "c3f48238a3bee3139a17cc633e5fd2f1" in fid:
        return urljoin(host or host2, url.format(begin, seq))
    elif "70b67c5b7d62fa9b0b2c3c9298554080" in fid:
        return urljoin(host or host12, url.format(fid, seq))
    else:
        return urljoin(host or host3, url.format(seq))


def now_time(_=None):
    return int(time.time())


def md5(s):
    m = hashlib.md5(str(s).encode("utf-8"))
    return m.hexdigest()


def is_url(url):
    regex = re.compile(config.url_regex)
    if regex.match(url):
        return False
    else:
        return True


def parse(url):
    url = urlencode(url).replace("url=", "")
    url = unquote(url)
    return url


def splicing(url, query_params):
    url_parsed = list(urlparse(url))
    temp_para = parse_qsl(url_parsed[3])
    url_parsed[3] = urlencode(temp_para)
    url_new = urlunparse(url_parsed)
    return url_new
