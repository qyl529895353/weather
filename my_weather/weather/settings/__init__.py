#  -*- coding: utf-8 -*-
"""
Author: loong
Time: 2024/3/27 20:27
File: __init__.py.py
Software: PyCharm
"""

import os
class Config(object):
    # 当前项目主应用目录
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 配置类
    # 调试模式
    DEBUG = True


    """密钥"""
    # 密钥，可以通过 base64.b64encode(os.urandom(48)) 来生成一个指定长度的随机字符串
    SECRET_KEY = "ghhBljAa0uzw2afLqJOXrukORE4BlkTY/1vaMuDh6opQ3uwGYtsDUyxcH62Aw3ju"

    '''数据库'''
    # mysql数据库的配置信息
    SQLALCHEMY_DATABASE_URI = ''
    # 动态追踪修改设置,如未设置只会提示警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 查询时会显示原始SQL语句
    SQLALCHEMY_ECHO = False