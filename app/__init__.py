from flask import Flask
<<<<<<< HEAD
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
=======
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
>>>>>>> d1350e7a6810ff9cbbb40858d2ad0a850b8c47bc

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

<<<<<<< HEAD
from app import routes, models
=======
from app import routes, models
>>>>>>> d1350e7a6810ff9cbbb40858d2ad0a850b8c47bc
