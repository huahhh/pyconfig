# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    admin_server_handler.py
   Description :
   Author :       Hu Hang
   date：          2019/4/10
-------------------------------------------------
"""
__author__ = 'HuHang'

from pyconfig.pyconfig_server.etcd_packge.etcd_packge import etcd_put, etcd_get

class admin_server_handler(object):


    def __init__(self):
        pass

    def project_init(self, project_name):
        pass


class config_project_handler(object):

    @etcd_get
    def get_project(self, project_name):
        return {'key': project_name}

    @etcd_put
    def register_project(self, project_name):
        return {"put_key":"/_pyconfig/metadata/project/{project_name}".format(project_name=project_name),
                "value": '1'}

    def gen_project_info(self, **kwargs):
        pass

if __name__ == "__main__":
    a = config_project_handler()
    print(a.get_project('test_project'))