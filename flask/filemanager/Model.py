#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-3-1

from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()
    
class Photos(db.Model):
    __tablename__ = 'photos'
    url = db.Column(db.String(64), nullable=False, primary_key=True)
    owner = db.Column(db.Integer, db.ForeignKey(
        'owners.id', ondelete='CASCADE'), nullable=False)
    node = db.Column(db.Integer, db.ForeignKey(
        'nodes.id', ondelete='CASCADE'), nullable=False)
    creation_date = db.Column(db.TIMESTAMP,
                              server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, url, owner, node):
        self.url = url
        self.owner = owner    
        self.node = node    
    
    
class PhotosSchema(ma.Schema):
    url = fields.String(required=True, validate=validate.Length(1))
    creation_date = fields.DateTime()  
    
class Owners(db.Model):
    __tablename__ = 'owners'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    creation_date = db.Column(db.TIMESTAMP,
                              server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, comment, category_id):
        self.name = name 
    
    
class OwnersSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(1))
    
class Nodes(db.Model):
    __tablename__ = 'nodes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    up = db.Column(db.String(64), nullable=True)
    leaf =db.Column(db.Boolean, nullable=True)
    creation_date = db.Column(db.TIMESTAMP,
                              server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, comment, category_id):
        self.name = name 
    
    
class NodesSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(1))    
    
    
