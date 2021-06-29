#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web

url = ('/qa/demo')

# 问答 demo
class handler:
    def GET(self):
        render = web.template.render('templates')
        return render.qa_test('')
