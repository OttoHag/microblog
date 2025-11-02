import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Bruk miljøvariabel hvis satt, ellers fallback
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # Bruk ekstern database hvis tilgjengelig, ellers SQLite lokalt
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Slår av unødvendig overhead

    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.office365.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', '1', 'yes']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'geirolar@hotmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'pzppdmrhilorvbrc'
    ADMINS = ['geirolar@hotmail.com']

    POSTS_PER_PAGE = 25
