from logging import debug
from os import name
from flask import Flask, run
from flask_sqlalchemy import SQLAlchemy
from flask import LoginManager
from flask_bootstrap import Bootstrap
# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()



def create_app():
    app = Flask(__name__,  template_folder='templates')
    
    Bootstrap(app)
    login_manager = LoginManager()
    login_manager.init_app(app)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)



    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # blueprint for non-auth parts of app
    from .templates.auth.view import auth as auth_blueprint
    app.register_blueprint(auth_blueprint) 

    # blueprint for non-auth parts of app
    from .templates.Usuario_1.view import Usuario_1 as Usuario_1_blueprint
    app.register_blueprint(Usuario_1_blueprint)

    # blueprint for non-auth parts of app
    from .templates.Usuario_2.view import Usuario_2 as Usuario_2_blueprint
    app.register_blueprint(Usuario_2_blueprint)

    return app


    
"""from project import db, create_app
db.create_all(app=create_app()) # pass the create_app result so Flask-SQLAlchemy gets the configuration."""

 

