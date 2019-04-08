# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    etcd_packge.py
   Description :
   Author :       huahng
   date：          2019/4/8
-------------------------------------------------
"""
__author__ = 'huahng'

import etcd3

class etcd_packge(object):

    def __init__(self, *args, **kwargs):
        self.etcd_clint = etcd3.client(*args, **kwargs)


    def get_key(self, key):
        return self.etcd_clint.get(key)

    @staticmethod
    def etcd_unpack_(etcd_res:tuple) -> dict:
        return {
            "key": etcd_res[1].key.decode(),
            "value": etcd_res[0].decode(),
            "version": etcd_res[1].version
        }

if __name__ == "__main__":
    etcd_inst = etcd_packge(host='118.24.66.43')
    etcd_res = etcd_inst.get_key('/test/2')
    etcd_res = etcd_inst.etcd_unpack_(etcd_res)
    print(etcd_res)

