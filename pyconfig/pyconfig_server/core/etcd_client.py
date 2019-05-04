# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    etcd_client.py
   Description :
   Author :       huahng
   date：          2019/5/4
-------------------------------------------------
"""
__author__ = 'huahng'

import etcd3
from functools import wraps

etcd_inst = etcd3.client('118.24.66.43')


def etcd_put(func):
    @wraps(func)
    def inner(self,*args,**kwargs):
        ret = func(self,*args,**kwargs)
        if isinstance(ret, dict):
            return [_etcd_put(i, str(ret[i])) for i in ret]
    return inner

def _etcd_put(key, value):
    return etcd_inst.put(key, value)

def etcd_get(func):
    @wraps(func)
    def inner(self, *args, **kwargs):
        ret = func(self, *args, **kwargs)
        return {i: _etcd_unpack_(etcd_inst.get(i + '/')) for i in ret}
    return inner

def etcd_get_predict(func):
    @wraps(func)
    def inner(self, *args, **kwargs):
        ret = func(self, *args, **kwargs)
        return {i: [_etcd_unpack_(etcd_res_item) for etcd_res_item in list(etcd_inst.get_prefix(i))] for i in ret}

    return inner


def _etcd_unpack_(etcd_res:tuple) -> dict:
    if any(etcd_res):
        return {
            "key": etcd_res[1].key.decode(),
            "value": etcd_res[0].decode(),
            "version": etcd_res[1].version,
            # "_metadata": etcd_res[1]
        }


if __name__ == "__main__":
    # etcd_res = etcd_inst.get_key('/test/2')
    # etcd_res = etcd_inst.etcd_unpack_(etcd_res)
    # print(etcd_res)
    from tqdm import tqdm
    t_bar  = tqdm(total=8000)
    etcd_i = etcd3.client('118.24.66.43')
    for i in range(8000):
        t_bar.update(1/4)
        res = etcd_i.put('/pyconfig_test/a', '1')
    # res = etcd_i.put('/pyconfig_test/a/name', '1')
    # res = [etcd_inst.etcd_unpack_(i) for i in list(etcd_i.get_prefix('/_pyconfig/metadata/project_info/pyconfig_test/'))]
    # print(res)