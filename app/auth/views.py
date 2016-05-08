#!/usr/bin/env python
#encoding:utf-8
__author__ = 'Samren'
from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_user, login_required, logout_user, \
current_user
from . import auth
from .. import db
from ..models import User
from .forms import LoginForm, RegistrationForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password')
    return render_template('auth/login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        flash('username: %s' % (form.username.data))
        db.session.commit()
        #token = user.generate_confirmation_token()
        flash('You can now login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('main.index'))