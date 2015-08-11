#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jack Li'

'''
This is for testing the ORM and Model running
'''

import orm,asyncio
from model import User , Blog, Comment

def test(loop):
	yield from orm.create_pool(loop=loop,user='root',passwd='355itu11',database='awesome')

	u = User(name='Test',email='test@example.com',passwd='1234',image='about:blank')

	yield from u.save()


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()