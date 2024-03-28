#  -*- coding: utf-8 -*-
"""
Author: loong
Time: 2024/3/27 20:50
File: view_inc.py
Software: PyCharm
"""

from flask import  jsonify
def show(status,message = 'error',data={},httpStatus = 200):
    result = {
        'status':status,
        'message':message,
        'result':data
    }
    return jsonify(result)