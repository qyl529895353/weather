#  -*- coding: utf-8 -*-
"""
Author: loong
Time: 2024/3/27 20:50
File: view_inc.py
Software: PyCharm
"""
from . import Config
class ProdConfig(Config):#继承初始init中的配置Config
    """生产模式下的配置"""
    DEBUG = False
    SQLALCHEMY_ECHO = False
    JWT_SECRET = 'asdczxfdsaeqwrqewrewqc2@#$%'