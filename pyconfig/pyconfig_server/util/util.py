# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    util.py
   Description :
   Author :       Hu Hang
   date：          2019/4/11
-------------------------------------------------
"""
__author__ = 'huahng'

import time
import datetime

def get_now_time_str():
    return str(datetime.date.today())

def get_now_time_stamp(ms=False):
    time_stamp = int(time.time() * 1000) if ms else int(time.time())
    return time_stamp

def gen_key_path(project, conf, key, ven="master", cluster="master"):
    pass

if __name__ == "__main__":
    print(get_now_time_str())