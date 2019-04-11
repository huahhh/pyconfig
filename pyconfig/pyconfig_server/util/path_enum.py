# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    path_enum.py
   Description :
   Author :       Hu Hang
   date：          2019/4/11
-------------------------------------------------
"""
__author__ = 'huahng'

from enum import Enum


class path_enum(Enum):
    project_info = '/_pyconfig/metadata/project_info'
    project_meta = '/_pyconfig/metadata/project'

    conf_register = '/{project}/_metadata/conf'

    conf_info = '/{project}/_metadata/{conf_name}'

    key = '/{project}/{conf}/{ven}/{cluster}'