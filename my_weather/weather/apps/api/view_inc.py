#  -*- coding: utf-8 -*-
"""
Author: loong
Time: 2024/3/27 20:50
File: view_inc.py
Software: PyCharm
"""
import requests
from weather.utils.error import Error
def get_weather_base(city):
    if not city:
        raise Error(-400, "无效编码")
    key = "f15139ee64beed9a73caee184a7e56ca"
    url = "https://restapi.amap.com/v3/weather/weatherInfo?city={}&key={}&extensions={}"
    result = dict()
    for extensions in ["all", "base"]:
        full_url = url.format(city,key,extensions)
        res = requests.get(url=full_url).json()

        if "status" not in res.keys():
            raise Error(-400, "天气查询异常")
        if res["status"] == 0:
            raise Error(-400, "天气查询失败")
        if res["infocode"] != "10000":
            raise Error(-400, "天气查询失败:%s"%res["info"])
        if extensions == "base":
            result.update({"lives":res["lives"]})
        else:
            result.update(res)
    return result



