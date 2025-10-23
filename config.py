import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Bruk miljøvariabel hvis satt, ellers fallback
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Bruk ekstern database hvis tilgjengelig, ellers SQLite lokalt
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Slår av unødvendig overhead

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or None # Tillat tomt passord
    ADMINS = ['geirolar@hotmail.com']  # Liste over admin-e-poster