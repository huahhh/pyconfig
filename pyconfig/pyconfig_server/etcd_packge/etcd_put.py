# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    etcd_put.py
   Description :
   Author :       huahng
   date：          2019/4/8
-------------------------------------------------
"""
__author__ = 'huahng'

import etcd3

class etcd_get(object):

    def __init__(self):
        self.etcd_clint = etcd3.client()