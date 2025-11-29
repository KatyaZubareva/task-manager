# Flask app factory and configuration
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from .models import User

from .auth import auth as auth_blueprint
from .auth import main as main_blueprint

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '' # To sign session cookies and CSRF tokens
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://db.sqlite' # Points to sqlite db
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Disabled to prevent unnecessary overhead

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)

    return app