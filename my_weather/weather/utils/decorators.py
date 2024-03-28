#  -*- coding: utf-8 -*-
"""
Author: loong
Time: 2024/3/27 21:11
File: decorators.py
Software: PyCharm
"""
import show
from error import Error
def resp(func):
    """
    接口响应统一处理装饰器
    1. 捕获异常
    2. 写日志
    3. 规范化返回
    """

    def respWrapper(*arg, **kvargs):
        try:
            result = func(*arg, **kvargs)
        except Exception as err:
            # 代码主动抛出的错误，Error 是自定义的错误
            if isinstance(err, Error):
                return show.show(status=err.status, message=err.message)
            else:
                # 底层代码未捕获到的错误
                return show.show(status=-500, message="服务器异常，请联系管理员")

        # 正常响应的数据
        return show.show(status=200, data=result)

    return respWrapper
