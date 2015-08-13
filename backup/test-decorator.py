#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jack Li'

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            print(args)
            print(kw)
            return func(*args, **kw)
        return wrapper
    return decorator

@log('jacklog')
def now(param, **kw):
	print('12321312321'+param)

print now.__name__

now('++++++', a=0)

# log('jacklog')(now('++++++'))