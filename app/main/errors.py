#!/usr/bin/env python
#encoding:utf-8
from flask import render_template
from . import main

"""
注意，不能用errorhandler修饰器，那样只有蓝本中的错误才能触发处理程序，
要想注册程序全局的错误处理程序，必须使用app_errorhandler
"""
@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500