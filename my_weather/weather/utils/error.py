#  -*- coding: utf-8 -*-
"""
Author: loong
Time: 2024/3/27 20:50
File: view_inc.py
Software: PyCharm
"""
class Error(Exception):
    def __init__(self, status=0, message=""):
        self.status = status
        self.message = message

    def __str__(self):
        return "status:%d, message:%s" % (self.status, self.message)


class UserError(Error):
    """
    业务逻辑错误，一般直接界面显示给用户即可
    """

    def __init__(self, message=""):
        self.status = -400
        self.message = message

    def __str__(self):
        return "code:%d, msg:%s" % (self.status, self.message)



class ProgramError(Error):
    """
    程序错误，未能预知的程序错误
    """

    def __init__(self, message=""):
        self.status = -500
        self.message = message

    def __str__(self):
        return "code:%d, msg:%s" % (self.status, self.message)
