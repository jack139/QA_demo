#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web


#####
web.config.debug = True   # Flase - production, True - staging

############# 消息中间件设置

REDIS_CONFIG = {
    'SERVER' : '127.0.0.1',
    'PORT'   : '7480',
    'PASSWD' : 'e18ffb7484f4d69c2acb40008471a71c',
    'REQUEST-QUEUE' : 'cardnum-synchronous-asynchronous-queue',
    'REQUEST-QUEUE-NUM' : 1,
    'MESSAGE_TIMEOUT' : 10, # 结果返回消息超时，单位：秒
}


# dispatcher 中 最大线程数
MAX_DISPATCHER_WORKERS = 8
