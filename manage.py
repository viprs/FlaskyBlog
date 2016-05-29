#!/usr/bin/env python
#encoding:utf-8
__author__ = 'Samren'
import os
from app import create_app, db
from app.models import User, Role, Post, Permission
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

COV = None
if os.environ.get('FLASKY_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True, include='app/*')
    COV.start()

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Post=Post,
                Permission=Permission)

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test(coverage=False):
    """Run the unit tests."""
    if coverage and not os.environ.get('FLASKY_COVERAGE'):
        import sys
        os.environ['FLASKY_COVERAGE'] = '1'
        os.execvp(sys.executable, [sys.executable] + sys.argv)
    import unittest
    test_suite = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(test_suite)
    if COV:
        COV.stop()
        COV.save()
        print 'Coverage Summary:'
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp', 'coverage')
        COV.html_report(directory=covdir)
        index_file = os.path.join(covdir, 'index.html')
        print 'HTML version: file: %s' % index_file
        COV.erase()


if __name__ == '__main__':
    manager.run()