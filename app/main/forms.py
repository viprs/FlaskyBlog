#!/usr/bin/env python
#encoding:utf-8
__author__ = 'Samren'
from flask import Flask, render_template, session, redirect, url_for, flash
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    #msg = StringField('What is your msg?', validators=[Required()])
    submit = SubmitField('Submit')