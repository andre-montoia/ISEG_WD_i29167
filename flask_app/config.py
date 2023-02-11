import os

# The main configuration class
class Config(object):
    # Set to False in production
    DEBUG = False
    # Set to False in production
    TESTING = False
    # Enable CSRF protection
    CSRF_ENABLED = True
    # Secret key for encrypting user data
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'
    # URI for the database, either from an environment variable or a local SQLite database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')

# Configuration for a production environment
class ProductionConfig(Config):
    # Set to False in production
    DEBUG = False

# Configuration for a staging environment
class StagingConfig(Config):
    # Set to True during development
    DEVELOPMENT = True
    # Set to True during development
    DEBUG = True

# Configuration for a development environment
class DevelopmentConfig(Config):
    # Set to True during development
    DEVELOPMENT = True
    # Set to True during development
    DEBUG = True

# Configuration for testing
class TestingConfig(Config):
    # Set to True during testing
    TESTING = True
