#! /usr/bin/env python3
# _*_ coding:utf-8 _*_
import asyncio
import orm
from models import User, Blog, Comment, next_id

async def test(loop):
	await orm.create_pool(loop=loop, user='root', password='goo_900_',db='yhc')
	u = User(name='Wang', email='Wang@exa.com', passwd='qweasd', image='about:blank')
	await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.run_forever()

for x in test(loop):
	pass