#!/usr/bin python3
# -*- coding: utf-8 -*-

import time
from loguru import *
from app.conf import *


class Vfile():
    def __init__(self):
        self.datadir = config.datadir

    def file_get(self, subpath):
        self.filepath = self.datadir
        with open(self.filepath, 'rx') as f:
            content = f.read()
            return content

    def file_store(self, subpath, content):
        self.filepath = self.datadir
        with open(self.filepath, 'w') as f:
            f.write(content)

vfile = Vfile()
