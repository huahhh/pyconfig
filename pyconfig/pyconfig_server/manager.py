# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    manager.py
   Description :
   Author :       huahng
   date：          2019/5/4
-------------------------------------------------
"""
__author__ = 'huahng'

from pyconfig.pyconfig_server.app import create_app

app = create_app('pyconfig')

app.run()