#  -*- coding: utf-8 -*-
"""
Author: loong
Time: 2024/3/27 20:50
File: view_inc.py
Software: PyCharm
"""
from . import backend_blu
from weather.utils.show import show
from flask import request
from weather.apps.api import view_inc as inc
from flasgger import swag_from
@backend_blu.route("/get_weather_information",methods=["GET"])
@swag_from("../../../swagger_file/yml_file/get_weather.yml")
def get_weather_information():
    ad_code = request.args.get('adCode')

    result = inc.get_weather_base(ad_code)

    return show(200, '查询成功', result)

