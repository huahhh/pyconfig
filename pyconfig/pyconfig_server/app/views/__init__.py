# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    __init__.py.py
   Description :
   Author :       huahng
   date：          2019/5/4
-------------------------------------------------
"""
__author__ = 'huahng'

from flask import Blueprint
from .project import project,get_all_project
from flask_restful import Api

api = Blueprint('project', __name__, url_prefix='/project')
res = Api(api)
res.add_resource(project, '/<project_name>')
res.add_resource(get_all_project, '/get_all')