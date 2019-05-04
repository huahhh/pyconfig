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

from flask import Flask

from .views import api


def create_app(app_name):
    app = Flask(app_name)
    app.register_blueprint(api)



    return app