#  -*- coding: utf-8 -*-
"""
Author: loong
Time: 2024/3/27 20:50
File: view_inc.py
Software: PyCharm
"""
from . import Config
class DevConfig(Config):#继承初始init中的配置Config
    """开发模式下的配置"""
    # SQLALCHEMY_ECHO= True
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/zsdb?charset=utf8"

    JWT_SECRET = 'asdczxfdsaeqwrqewrewqc2@#$%'
    JWT_EXPIRE_DAY = 15