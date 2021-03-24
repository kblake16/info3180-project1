import os

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
    SQLALCHEMY_DATABASE_URI = 'postgresql://dsvwfspobuzlqw:331992d2e4bc53183bd3043f65fb799d30c959a6cb8b4c57882ef9bb1f4a2844@ec2-54-198-252-9.compute-1.amazonaws.com:5432/deeqoameknkdrs' or 'postgresql://yourusername:yourpassword@localhost/databasename'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    UPLOAD_FOLDER = 'uploads'
    ICON_FOLDER = 'images'

class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False