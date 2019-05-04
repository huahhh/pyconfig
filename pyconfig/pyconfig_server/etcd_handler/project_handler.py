# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    project_handler.py
   Description :
   Author :       huahng
   date：          2019/5/4
-------------------------------------------------
"""
__author__ = 'huahng'

from pyconfig.pyconfig_server.core.etcd_client import etcd_put, etcd_get, etcd_get_predict

from pyconfig.pyconfig_server.util.path_enum import path_enum

from pyconfig.pyconfig_server.util.util import get_now_time_str, get_now_time_stamp


class project_handler(object):

    def __init__(self):
        self.project_info_base_dict = {
            "project_name": "",
            "project_des": "",
            "project_build_date_str": "",
            "project_build_date_stamp": "",
            "project_user": "",
            "project_dept": ""
        }

    @etcd_get_predict
    def get_all_project(self):
        return {path_enum.project_meta.value: None}

    @etcd_put
    def register_project(self, project):
        return {path_enum.project_meta.value + "/{project}".format(project=project): '1'}

    @etcd_get_predict
    def get_project_info(self, project):
        return {path_enum.project_info.value + '/{project}'.format(project=project): None}


    @etcd_put
    def change_project_info(self, project, **kwargs):
        kwargs.update({'project_name': project})
        return {
            path_enum.project_info.value + "/{project}/{base_key}".format(base_key=base_key, project=project):
                self.project_info_base_dict[base_key]
                if base_key not in kwargs else kwargs[base_key]
            for base_key in self.project_info_base_dict
        }

    def init_project_info(self, project, **kwargs):
        kwargs['project_build_date_str'] = kwargs.get('project_build_date_str') \
            if kwargs.get('project_build_date_str') else get_now_time_str()
        kwargs['project_build_date_stamp'] = kwargs.get('project_build_date_stamp') \
            if kwargs.get('project_build_date_stamp') else get_now_time_stamp()
        return self.change_project_info(project, **kwargs)