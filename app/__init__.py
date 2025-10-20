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

    from app import models  # sørger for at modellene er lastet inn

    return app

# 🔧 Viktig: denne må stå utenfor create_app()
from app.models import User

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
