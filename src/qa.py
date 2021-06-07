#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 本地调试
# uwsgi --http 127.0.0.1:8000  --wsgi-file qa.py --check-static ../


import web
import gc
from config.url import urls

app = web.application(urls, globals())
application = app.wsgifunc()

gc.set_threshold(300,5,5)


#if __name__ == "__main__":
#    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
#    app.run()
