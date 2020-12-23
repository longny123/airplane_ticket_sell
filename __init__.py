from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.secret_key = '^%*&j!^@f^*gsu8ias1^&!*^!8&'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:haiquang123@localhost/SellTicketApp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/static/<path:path>")
def static_dir(path):
    return send_from_directory("static", path)

db = SQLAlchemy(app=app)
admin = Admin(app=app, base_template="Admin/index.html")
login = LoginManager(app=app)
migrate = Migrate(app, db)


