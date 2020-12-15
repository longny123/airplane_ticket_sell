from flask import render_template, request, redirect
from flask_login import current_user, login_user
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath('CongNghePhanMen1'))))
from CongNghePhanMen1 import app, login, admin, db, utils
from models import User


@app.route('/')
def home():
    return render_template("HomePage.html")


@app.route('/SignIn', methods=['GET','POST'])
def sign_in():
    err_msg = ""
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        user = utils.check_login(username=username, password=password)

        if user:
            login_user(user)
            return render_template("LogIned.html")
        else:
            err_msg = "wrong password"
    return render_template('SignInPage.html', err_msg=err_msg)

@app.route


@app.route('/SignUp', methods=['GET', 'POST'])
def sign_up():
    err_msg = ""
    if request.method == 'POST':
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')
        if password == confirm_password:
            name = request.form.get('name')
            username = request.form.get('username')
            email = request.form.get('email')
            if utils.register_user(name, email, username, password):
                return redirect('HomePage.html')
            else:
                err_msg = "system error"
        else:
            err_msg = "wrong password"
    return render_template('SignInPage.html', err_msg=err_msg)


@app.route('/Logined', methods=['GET'])
def logined():
    return render_template("LogIned.html")


@app.route('/ContactUs')
def contact_us():
    return render_template("ContactPage.html")

@app.route('/admin')


@login.user_loader
def get_user(user_id):
    return utils.get_user_by_id(user_id=user_id)


if __name__ == '__main__':
    app.run(debug=True)
