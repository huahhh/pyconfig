# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    config_handle.py
   Description :
   Author :       Hu Hang
   date：          2019/4/10
-------------------------------------------------
"""
__author__ = 'HuHang'

from pyconfig.pyconfig_server.etcd_packge.etcd_packge import etcd_packge


class config_handler(object):

    def __init__(self):
        self.etcd_packge = etcd_packge(host="118.24.66.43")

    def merge_uri(self, project, config_name, key, env="master", clu="master"):
        return "/{project}/{config_name}/{env}/{clu}/{key}".format(
            project=project,
            config_name=config_name,
            env=env,
            clu=clu,
            key=key
        )


if __name__ == "__main__":
    config_handler_inst = config_handler()
    print(config_handler_inst.merge_uri(project='test', config_name='test', key='now'))