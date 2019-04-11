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

from pyconfig.pyconfig_server.util.path_enum import path_enum
from pyconfig.pyconfig_server.util.util import get_now_time_stamp, get_now_time_str
from pyconfig.pyconfig_server.etcd_packge.etcd_packge import etcd_put, etcd_get, etcd_get_predict

class admin_server_handler(object):


    def __init__(self):
        pass


class config_key_handler(object):

    def __init__(self):
        self.key_dict = {
            '/{key}': '',
            '/{key}-des': '',
            '/{key}-last_changer': '',
            '/{key}-last_change_date': '',
        }


    @etcd_get_predict
    def get_key(self, project, conf, key, ven="master", cluster="master"):
        return {path_enum.key.value.format(project=project, conf=conf, ven=ven, cluster=cluster) +
                '/{key}'.format(key=key): None}

    @etcd_get_predict
    def get_all_key(self, project, conf, ven="master", cluster="master"):
        return {path_enum.key.value.format(project=project, conf=conf, ven=ven, cluster=cluster): None}

    @etcd_put
    def set_key(self, project, conf, key, value, ven="master", cluster="master", des="", changer=""):
        key_prefix = path_enum.key.value.format(project=project, conf=conf, ven=ven, cluster=cluster)
        ret = {
            key_prefix + '/{key}'.format(key=key) : value,
            key_prefix + '/{key}_des'.format(key=key) : des,
            key_prefix + '/{key}_last_changer'.format(key=key): changer,
            key_prefix + '/{key}_last_change_date'.format(key=key): get_now_time_stamp()
        }
        return ret




class config_conf_handler(object):


    def __init__(self):
        self.conf_info_base_dict = {
            'conf_name': '',
            'conf_des': '',
            'conf_build_date_str': '',
            'conf_build_date_stamp': ''

        }

    @etcd_put
    def register_conf(self, project, conf, ven='master', cluster="master"):
        return {path_enum.conf_register.value.format(project=project) + '/{conf_name}_{ven}_{cluster}'.format(
                                                     conf_name = conf,
                                                     ven=ven,
                                                     cluster=cluster): '1'}

    @etcd_put
    def change_conf_info(self, project, conf, **kwargs):
        kwargs.update({'conf_name': conf})
        return {
            path_enum.conf_info.value.format(project=project, conf_name=conf) + "/{base_key}".format(base_key=base_key):
                self.conf_info_base_dict[base_key]
                if base_key not in kwargs else kwargs[base_key]
            for base_key in self.conf_info_base_dict
        }

    def init_conf_info(self, project, conf, **kwargs):
        kwargs['conf_build_date_str'] = kwargs.get('conf_build_date_str') \
            if kwargs.get('conf_build_date_str') else get_now_time_str()
        kwargs['conf_build_date_stamp'] = kwargs.get('conf_build_date_stamp') \
            if kwargs.get('conf_build_date_stamp') else get_now_time_stamp()
        return self.change_conf_info(project, conf, **kwargs)


    @etcd_get_predict
    def get_all_conf(self, project):
        return {path_enum.conf_register.value.format(project=project): None}

    @etcd_get_predict
    def get_conf_info(self, project, conf):
        return {path_enum.conf_info.value.format(project=project, conf_name=conf): None}

class config_project_handler(object):

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

if __name__ == "__main__":
    a = config_key_handler()
    # a.register_conf('xiaoming_spider', 'run_config')
    # a.init_conf_info('xiaoming_spider', 'run_config')
    # a.get_all_conf('xiaoming_spider')
    # a.register_project('xiaoming_cleaner')
    # a.init_project_info('xiaoming_cleaner')
    # from tqdm import tqdm
    # t_ = tqdm(total=2000)
    # for i in range(2000):
    #     t_.update()
    #     a.set_key('xiaoming_spider', 'run_config', 'spider_%s' % i, '%s' % i)
    import time
    now = time.time()
    res = a.get_all_key('xiaoming_spider', 'run_config')
    print(len(res['/xiaoming_spider/run_config/master/master']))
    print(res)
    print(time.time()-now)
    # a.init_project_info()
    # import time
    # for i in range(10):
    #     now_time = time.time()
    #     print(a.get_project_info('pyconfig_test'))
    #     print(time.time() - now_time)