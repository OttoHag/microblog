import os
from sqlalchemy.pool import StaticPool

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Bruk miljøvariabel hvis satt, ellers fallback
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # Bruk ekstern database hvis tilgjengelig, ellers SQLite lokalt
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Slår av unødvendig overhead
    
    # SQLite connection pooling and timeout settings
    SQLALCHEMY_ENGINE_OPTIONS = {
        'connect_args': {
            'timeout': 30,  # 30 second timeout for database operations
            'check_same_thread': False,
        },
        'pool_size': 10,
        'pool_recycle': 3600,
        'pool_pre_ping': True,
        'max_overflow': 20,
    }

    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', '1', 'yes']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'geirolar@hotmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or None  # Set via environment variable
    ADMINS = ['geirolar@hotmail.com']

    POSTS_PER_PAGE = 25
