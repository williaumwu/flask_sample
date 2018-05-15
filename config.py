# config.py

import os

class BaseConfig(object):
    SECRET_KEY = os.environ['SECRET_KEY']
    DEBUG = os.environ['DEBUG']
    DB_NAME = os.environ['MYSQL_DB_NAME']
    DB_USER = os.environ['MYSQL_DB_USER']
    DB_PASS = os.environ['MYSQL_DB_PASSWORD']
    DB_HOST = os.environ['MYSQL_HOST']
    DB_PORT = os.environ['MYSQL_PORT']
    SQLALCHEMY_DATABASE_URI = 'mysql://{0}:{1}@{2}:{3}/{4}'.format(
        DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME
    )
