#  -*- coding: utf-8 -*-
"""
Author: loong
Time: 2024/3/27 20:23
File: __init__.py.py
Software: PyCharm
"""

import sys
import os
from flask import Flask
from flask_script import Manager,Command
from weather.settings.dev import DevConfig
from weather.settings.prod import ProdConfig
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

config_dict = {
    'dev':DevConfig,
    'prod':ProdConfig,
}

db = SQLAlchemy(engine_options={"isolation_level":"READ UNCOMMITTED"})


def init_app(config_name):#manage.py中调用传入dev或者prod
    '''项目初始化函数'''
    #创建app应用
    app = Flask(__name__)

    db = SQLAlchemy(app)
    #根据选项获取配置类
    print(config_name)
    Config = config_dict.get(config_name)
    print(Config)
    #加载配置
    app.config.from_object(Config)#当运行这句代码时 那么dev或者prod中的配置就会运行 他们中都继承了Config


    #初始化数据库
    db.init_app(app)



    # 初始化终端脚本
    app.manage = Manager(app)

    # 解决跨域问题
    CORS(app,resources=r'/*')

    #配置视图的存储目录默认导包路径
    sys.path.insert(0,Config.BASE_DIR)
    sys.path.insert(0,os.path.join(Config.BASE_DIR,'apps'))

    from apps.api import backend_blu
    app.register_blueprint(backend_blu)

    return app
if os.getenv("prod") == "prod":
    config_name = 'prod'
else:
    config_name = 'dev'

app = init_app(config_name)
from flasgger import Swagger
Swagger(app)
