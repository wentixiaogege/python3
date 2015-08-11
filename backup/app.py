#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Jack Li'

'''
	ashnc web Application
'''

import logging; logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time
from datetime import datetime

from aiohttp import web

import orm

def index(request):
	return web.Response(body=b'<h1>Awesome</h1>')


##注意aiohttp的初始化函数init()也是一个coroutine，loop.create_server()则利用asyncio创建TCP服务
@asyncio.coroutine
def init(loop):
	yield from orm.create_pool(loop=loop, host='12.7.0.0.1', prot=3306, user='root',password='355itu11',db='awesome')
	app = web.Application(loop=loop)
	app.router.add_route('GET','/',index)
	srv = yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)
	logging.info('server startted')
	return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))

loop.run_forever()