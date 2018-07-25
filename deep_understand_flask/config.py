class Config(object):
    SECRET_KEY = '408eadc9ddefaa9dd3d42bff28bc6daff32f6c659b2026fb7f51f4ac24cab3e5'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'
    # SQLALCHEMY_ECHO = True
