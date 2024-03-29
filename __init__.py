from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)
app.secret_key = '^%*&j!^@f^*gsu8ias1^&!*^!8&'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:haiquang123@localhost/SellTicketApp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app=app)
admin = Admin(app=app, base_template="Admin/index.html")
login = LoginManager(app=app)
migrate = Migrate(app, db)


