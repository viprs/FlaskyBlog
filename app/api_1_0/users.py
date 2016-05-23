#!/usr/bin/env python
#encoding:utf-8
__author__ = 'Samren'
from flask import jsonify, request, current_app, url_for
from . import api
from ..models import User, Post


@api.route('/users/')
def get_users():
    page = request.args.get('page', 1, type=int)
    pagination = User.query.paginate(page,
        per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
    users = pagination.items
    prev_page = None
    if pagination.has_prev:
        prev_page = url_for('api.get_users', page=page-1, _external=True)
    next_page = None
    if pagination.has_next:
        next_page = url_for('api.get_users', page=page+1, _external=True)
    user_list = [user.to_json() for user in users]
    return jsonify({
        'users': user_list,
        'prev_page': prev_page,
        'next_page': next_page,
        'total_count': pagination.total,
        'page_count': user_list.__len__()
    })


@api.route('/users/<int:id>')
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_json())


@api.route('/users/<int:id>/posts/')
def get_user_posts(id):
    user = User.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    pagination = user.posts.order_by(Post.timestamp.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    prev_page = None
    if pagination.has_prev:
        prev_page = url_for('api.get_posts', page=page-1, _external=True)
    next_page = None
    if pagination.has_next:
        next_page = url_for('api.get_posts', page=page+1, _external=True)
    return jsonify({
        'posts': [post.to_json() for post in posts],
        'prev_page': prev_page,
        'next_page': next_page,
        'count': pagination.total
    })