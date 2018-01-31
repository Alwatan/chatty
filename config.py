import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    CHATTY_MAIL_SUBJECT_PREFIX = '[Chatty]'
    CHATTY_MAIL_SENDER = 'Chatty Admin <pugudean@gmail.com>'
    CHATTY_ADMIN = os.environ.get('CHATTY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CHATTY_POSTS_PER_PAGE = 20

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://fazo:kratos@localhost/chatty'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://fazo:kratos@localhost/chatty'

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://fazo:kratos@localhost/test_chatty'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
