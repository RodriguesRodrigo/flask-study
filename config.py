from os import getenv


class BaseConfig:
    SECRET_KEY = getenv('SECRET_KEY', b'\xa1\x86\x0b\x97\xe6\x9f\x1d\x9f6\xd4\xcc-w\n&B')
    APP_PORT = int(getenv('APP_PORT'))


class DevelopmentConfig(BaseConfig):
    FLASK_ENV = 'development'
    DEBUG = True


class TestingConfig(BaseConfig):
    FLASK_ENV = 'testing'
    TESTING = True


class ProductionConfig(BaseConfig):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False


config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
