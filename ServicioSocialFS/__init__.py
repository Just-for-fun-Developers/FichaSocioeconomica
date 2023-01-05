# ServicioSocialFS/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

#####################################
#### DATABASE SETUP #################
#####################################

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://serviciossocialfichasocioeconomica_user:qa3KLk42N9aXWWVSRlux97KNo4D8iz0q@dpg-ceo5almn6mpoovl1jn10-a.oregon-postgres.render.com:5432/serviciossocialfichasocioeconomica'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


#####################################
#### LOGIN CONFIGS ##################
#####################################

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login_regular'

#####################################

from ServicioSocialFS.users.views import users
from ServicioSocialFS.error_pages.handlers import error_pages
from ServicioSocialFS.services.views import services
from ServicioSocialFS.core.views import core


app.register_blueprint(core)
app.register_blueprint(services)
app.register_blueprint(error_pages)
app.register_blueprint(users)

