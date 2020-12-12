from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
import sys,os

db = SQLAlchemy()
# app = Flask(__name__)
# app.secret_key = '3^@&@&!&(@*UGUIEIU&@^!*(@&*(SS'
# app.config.from_object('config.Config')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:haiquang123@localhost/saledbv2?charset=utf8'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
from .config import Config

def create_app():
    app = Flask(__name__, instance_relative_config=False, template_folder='templates')
    app.config.from_object(Config)

    db.init_app(app)
    with app.app_context():
        # from . import routes  # Import routes
        from server.api.route import user_route
        db.create_all()  # Create sql tables for our data models

        return app

# db = SQLAlchemy(app=app)
# admin = Admin(app=app, name='IT82 SHOP 2',
#               template_mode="bootstrap4")
