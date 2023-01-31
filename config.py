import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    SSL_REDIRECT = True
    TESTING = False
    CSRF_ENABLED = True
    USE_DEV_DB = True
    DB_NAME = "dev_SOMETHING"


class ProductionConfig(Config):
    DEBUG = False
    USE_DEV_DB = False
    DB_NAME = "SOMETHING"


class LocalProductionConfig(Config):
    DEBUG = False
    USE_DEV_DB = False
    DB_NAME = "SOMETHING"
    SSL_REDIRECT = False


class DevelopmentConfig(Config):
    DEBUG = True
    SSL_REDIRECT = False

