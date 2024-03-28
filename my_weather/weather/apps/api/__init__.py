#  -*- coding: utf-8 -*-
"""
Author: loong
Time: 2024/3/27 20:40
File: __init__.py.py
Software: PyCharm
"""

from flask import Blueprint
backend_blu= Blueprint('api',__name__,static_folder='static',static_url_path='/statics',url_prefix='/adminapi')

from .view import *