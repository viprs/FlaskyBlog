#!/usr/bin/env python
#encoding:utf-8
__author__ = 'Samren'
"""
数据库表中，多对多的定义方式
"""

registrations = db.Table('registrations',
                        db.Column('student_id', db.Integer, db.ForeignKey('students.id')),
                        db.Column('class_id', db.Integer, db.ForeignKey('classes.id')))


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    classes= db.relationship('Class',
                             secondary=registrations,
                             backref=db.backref('students', lazy='dynamic'),
                             lazy='dynamic')


class Class(db.Model):
    __tablename__ = 'classes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))