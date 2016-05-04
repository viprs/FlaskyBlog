#!/usr/bin/env python
#encoding:utf-8
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors