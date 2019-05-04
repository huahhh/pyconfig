# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    project.py
   Description :
   Author :       huahng
   date：          2019/5/4
-------------------------------------------------
"""
__author__ = 'huahng'

from flask_restful import Resource

from pyconfig.pyconfig_server.etcd_handler import project_handler_inst

from pyconfig.pyconfig_server.util.path_enum import path_enum


class project(Resource):

    def get(self, project_name):
        ret = project_handler_inst.get_project_info(project_name)
        res = {}
        for v in ret.get(path_enum.project_info.value + "/{project}".format(project=project_name), []):
           res.update({v['key'].split('/')[-1]: v['value']})
        return (res)

    def put(self):
        pass

class get_all_project(Resource):

    def get(self):
        return project_handler_inst.get_all_project()