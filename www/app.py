#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   app.py
@Time    :   2020/1/19 13:04
@Author  :   Shen Zhili 
@Contact :   20161607@cqu.edu.cn
@License :   (C)Copyright 2020
"""
# import lib


import logging;logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime
from aiohttp import web, web_runner

routes = web.RouteTableDef()


@routes.get('/')
def index(request):
    return web.Response(body='<h1>hello world</h1>', content_type='text/html')


def init():
    app = web.Application()
    app.add_routes([web.get('/', index)])
    logging.info('server started as http://127.0.0.1:8000...')
    web.run_app(app, host='127.0.0.1', port=8000)

init()



