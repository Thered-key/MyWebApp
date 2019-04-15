#! /usr/bin/env python3
# _*_ coding:utf-8 _*_
'url handlers'

import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post

from models import User, Comment, Blog, next_id

@get('/index')
async def index(request):
	users = await User.findAll()
	return {
		'__template__': 'test.html',
		'users':users
	}