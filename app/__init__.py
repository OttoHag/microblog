import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'main.login'  # navnet på login-ruten i blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)

    from app.error import bp_error
    app.register_blueprint(bp_error)

    from app import models
    from app.models import User

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

    # Alltid logg til fil
    if not os.path.exists('logs'):
        os.mkdir('logs')

    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')

    # E-postvarsling ved feil (kun i produksjon)
    if not app.debug and app.config.get('MAIL_SERVER'):
        auth = None
        if app.config.get('MAIL_USERNAME') and app.config.get('MAIL_PASSWORD'):
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])

        secure = () if app.config.get('MAIL_USE_TLS') else None

        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'],
            subject='Microblog Failure',
            credentials=auth,
            secure=secure
        )
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    from app import models  # sørger for at modellene er lastet inn
    from app.models import User  # nødvendig for brukerinnlasting

    @login.user_loader
d   ef load_user(id):
        return User.query.get(int(id))

    return app