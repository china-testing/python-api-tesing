#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-3-1

from flask import Blueprint
from flask_restful import Api
from resources.Photos import PhotosResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes
api.add_resource(PhotosResource, '/Photos')
