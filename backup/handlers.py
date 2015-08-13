#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jack Li'

'''
This is the url handle file
'''
import re,time,json,logging,hashlib,base64,asyncio

from coroweb import Get,Post

from model import User,Comment,Blog,next_id

@Get('/')
def index(request):
	users = yield from User.findAll()
	return{
		'__template__':'test.html',
		'users':users
	}