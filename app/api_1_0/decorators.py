#!/usr/bin/env python
#encoding:utf-8
__author__ = 'Samren'
from functools import wraps
from flask import abort, g
from flask.ext.login import current_user
from ..models import Permission
from .errors import forbidden


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not g.current_user.can(permission):
                return forbidden('Insufficient permission')
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)

