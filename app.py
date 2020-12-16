from flask import render_template, request, redirect
from flask_login import current_user, login_user, logout_user
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath('CongNghePhanMen1'))))
from CongNghePhanMen1 import app, login, admin, db, utils, decorator
from admin import *


@app.route('/')
def home():
    return render_template("HomePage.html")


@app.route('/SignIn', methods=['GET', 'POST'])
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


@app.route('/LogOut')
def log_out():
    logout_user()
    return render_template("HomePage.html")


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


@app.route('/admin/UserManager/<int:user_id>', methods=['GET'])
def user_manager(user_id):
    err_msg = ""
    user = utils.get_user_by_id(user_id)
    if user.user_role == 'admin':
        return render_template("Admin/user_manager.html", user=utils.get_user_by_id(user_id),
                               list_user=utils.get_list_user(), err_msg=err_msg)
    elif user.user_role == 'user':
        err_msg = "You are not permission to here"
        return redirect('/', err_msg=err_msg)




@app.route('/admin/UserManager/<int:user_id>/AddUser', methods=['GET', 'POST'])
def add_user(user_id):
    user = utils.get_user_by_id(user_id)
    mes = ""
    err_msg = ""
    if request.method == 'POST':
        password = request.form.get('password')
        name = request.form.get('name')
        username = request.form.get('username')
        email = request.form.get('email')
        if utils.register_user(name, email, username, password):
            mes = "User was created"
            return redirect('UserManager')
        else:
            err_msg = "something wrong when creating user"
    return render_template("Admin/add-user.html", mes=mes, err_msg=err_msg)


@app.route('/admin/Information/<int:user_id>', methods=['GET', 'POST'])
def information(user_id):
    user = utils.get_user_by_id(user_id)
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')
        if new_password == confirm_password:
            utils.update_user(name, username, new_password)
            return redirect("Admin/information.html")
    return render_template("Admin/information.html", user=user)


@login.user_loader
def get_user(user_id):
    return utils.get_user_by_id(user_id=user_id)


if __name__ == '__main__':
    app.run(debug=True)
