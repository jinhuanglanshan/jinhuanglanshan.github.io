#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   user.py   
@Time    :   2020/1/19 15:59
@Author  :   Shen Zhili 
@Contact :   20161607@cqu.edu.cn
@License :   (C)Copyright 2020
"""
# import lib


from www.orm import Model, StringField, IntegerField, create_pool
import asyncio



class User(Model):
    __table__ = 'user'
    id = IntegerField(primary_key=True)
    name = StringField()


async def init(loop):
    user = User(id=123, name='jinhuang')
    await create_pool(loop, user='root', password='password')
    await user.remove()
    a = await User.findAll()
    print(a)


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))