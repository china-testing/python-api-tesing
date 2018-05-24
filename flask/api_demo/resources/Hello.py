#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-1-10

from flask_restful import Resource


class Hello(Resource):
    def get(self):
        return {"message": "Hello, World!"}

    def post(self):
        return {"message": "Hello, World!"}
