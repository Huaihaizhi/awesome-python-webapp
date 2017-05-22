#!/usr/bin/env python
# -*- coding: utf-8 -*-
import orm
from models import User, Blog, Comment
import asyncio

loop=asyncio.get_event_loop()
@asyncio.coroutine
def test():
    yield from orm.create_pool(loop,user='www-data', password='www-data', database='awesome')
    n= User(name='Test2', email='test2@example.com', passwd='1234509876', image='about:blank')
    yield from n.save()

#    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
#    m = User(name='Test1', email='test1@example.com', passwd='0987654321', image='about:blank')
#    yield from u.save()
#    yield from m.save()
#for x in test():
#    pass
loop.run_until_complete(test())
loop.close()