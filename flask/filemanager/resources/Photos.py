#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-3-1

from flask import request
from flask_restful import Resource
from Model import db, Photos, PhotosSchema

photos_schema = PhotosSchema(many=True)
photo_schema = PhotosSchema()


class PhotosResource(Resource):

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = photo_schema.load(json_data)
        if errors:
            return errors, 422
        photo = Photos.query.filter_by(url=data['url']).first()
        if photo:
            return {'message': 'Photo already exists'}, 400
        photo = Photos(
            url=json_data['url'],owner=json_data['owner'],node=json_data['node']
        )

        db.session.add(photo)
        db.session.commit()

        result = photo_schema.dump(photo).data

        return {"status": 'success', 'data': result}, 201


