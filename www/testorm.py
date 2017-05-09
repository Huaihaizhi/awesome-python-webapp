#!/usr/bin/env python
# -*- coding: utf-8 -*-
import orm
from models import User, Blog, Comment
import asyncio

loop=asyncio.get_event_loop()
@asyncio.coroutine
def test():
    yield from orm.create_pool(loop,user='www-data', password='www-data', database='awesome')

    u = User(name='Test', email='test@example.com', password='1234567890', image='about:blank')

    yield from u.save()
    r=yield from User.findAll()
    print(r)
 #   yield from orm.destory_pool()

for x in test():
    pass
loop.run_until_complete(test())
loop.close()