from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

socketio = SocketIO()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SOME_PRIVATE_KEY'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db = SQLAlchemy()
db.init_app(app)
socketio.init_app(app)

login_manager = LoginManager(app)
bcrypt = Bcrypt(app)

from chat.main.routes import main as main_blueprint
from chat.auth.routes import auth as auth_blueprint

app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint)

from .models import *
