from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_user, logout_user
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath('CongNghePhanMen1'))))
from CongNghePhanMen1 import app, login, admin, db, utils, decorator
from admin import *
from models import Tickets


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
    if logout_user():
        return redirect('/SignIn')
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
                return redirect('sign_in')
            else:
                err_msg = "system error"
        else:
            err_msg = "wrong password"
    return render_template('SignInPage.html', err_msg=err_msg)


@app.route('/Logined', methods=['GET'])
def logined():
    return render_template("LogIned.html")


@app.route('/BuyTicket')
def buy_ticket():
    return render_template('ChooseTicket.html', list_ticket=utils.load_tickets())

@app.route('/BuyTicket/Search', methods=['post'])
def search_ticket():
    result = Tickets.query.whoosh_search(request.form.get('starting_place'),
                                         request.form.get('destination_place'),
                                         request.form.get('date_starting'+'month_starting'),
                                         request.form.get('date_return'+'month_return')).all()
    return render_template('ChooseTicket.html', list_ticket=result)


@app.route('/ConfirmTicket/<int:user_id>/<int:ticket_id>', methods=['post'])
def confirm_ticket(user_id, ticket_id):
    ticket = utils.get_tickets_by_id(ticket_id)

    if utils.confirm_ticket(ticket_id=ticket_id, user_id=user_id, quantity=1, price=ticket.price):
        return redirect(url_for('buy_ticket'))


@app.route('/ContactUs', methods=['GET', 'POST'])
def contact_us():
    if request.method == 'POST':
        name = request.form.get('name')
        kind = request.form.get('kind')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        if utils.add_report(name=name,
                            kind=kind,
                            email=email,
                            phone=phone,
                            message=message):
            return redirect('/')
    return render_template("ContactPage.html")


@app.route('/UserManager/<int:user_id>', methods=['GET'])
def user_manager(user_id):
    err_msg = ""
    user = utils.get_user_by_id(user_id)
    if user.user_role == 'admin':
        return render_template("Admin/user_manager.html", user=utils.get_user_by_id(user_id),
                               list_user=utils.get_list_user(), err_msg=err_msg)
    elif user.user_role == 'user':
        err_msg = "You are not permission to here"
        return redirect('/', err_msg=err_msg)


@app.route('/UserManager/<int:user_id>/AddUser', methods=['GET', 'POST'])
@decorator.login_required
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
            return redirect(url_for('user_manager', user_id=current_user.id))
        else:
            err_msg = "something wrong when creating user"
            return redirect(url_for('user_manager', user_id=current_user.id))
    return render_template("Admin/add_user.html", mes=mes, err_msg=err_msg)


@app.route('/Information/<int:user_id>', methods=['GET', 'POST'])
def information(user_id):
    user = utils.get_user_by_id(user_id)
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')
        if new_password == confirm_password:
            user = utils.update_user(user_id=user_id, name=name, username=username, password=new_password)
            if user:
                return redirect(url_for('information', user_id=current_user.id))
    return render_template("Admin/information.html", user=user)


@app.route('/DeleteUser/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    user = utils.delete_user(user_id)
    if user:
        return redirect(url_for('user_manager', user_id=current_user.id))
    return render_template("Admin/information.html")


@app.route('/TicketManager/<int:user_id>', methods=['GET', 'POST'])
def ticket_manager(user_id):
    return render_template("Admin/ticket_manager.html", user=utils.get_user_by_id(user_id),
                           list_tickets=utils.load_tickets())


@app.route('/TicketManager/<int:user_id>/AddOption', methods=['GET', 'POST'])
@decorator.login_required
def add_new_ticket(user_id):
    mes = ""
    err_msg = ""
    if request.method == 'POST':
        name = request.form.get('name')
        starting_place = request.form.get('starting_place')
        destination_place = request.form.get('destination_place')
        date_starting = request.form.get('starting_date')
        date_return = request.form.get('return_date')
        price = request.form.get('price')
        if utils.add_ticket(name=name,
                            starting_place=starting_place,
                            destination_place=destination_place,
                            starting_date=date_starting,
                            return_date=date_return,
                            price=price):
            mes = "Ticket was created"
            return redirect(url_for('ticket_manager', user_id=current_user.id))
        else:
            err_msg = "something wrong when creating user"
            return redirect(url_for('ticket_manager', user_id=current_user.id))
    return render_template("Admin/add_ticket.html", user=utils.get_user_by_id(user_id)
                           , mes=mes, err_msg=err_msg)


@app.route('/EditTicket/<int:ticket_id>', methods=['GET', 'POST'])
def edit_ticket(ticket_id):
    mes = ''
    err_msg = ''
    if request.method == 'POST':
        ticket = utils.get_tickets_by_id(ticket_id)
        name = request.form.get('name')
        starting_place = request.form.get('starting_place')
        destination_place = request.form.get('destination_place')
        date_starting = request.form.get('starting_date')
        date_return = request.form.get('return_date')
        price = request.form.get('price')
        if utils.edit_ticket(ticket_id=ticket.id,
                             name=name,
                             starting_place=starting_place,
                             destination_place=destination_place,
                             starting_date=date_starting,
                             return_date=date_return,
                             price=price):
            mes = "Ticket was created"
            return redirect(url_for('ticket_manager', user_id=current_user.id))
        else:
            err_msg = "something wrong when creating user"
            return redirect(url_for('ticket_manager', user_id=current_user.id))
    return render_template("Admin/edit_ticket.html", ticket=utils.get_tickets_by_id(ticket_id)
                           , mes=mes, err_msg=err_msg)


@app.route('/Delete/<int:user_id>', methods=['POST'])
def delete(user_id):
    user = utils.delete_user(user_id)
    if user:
        return redirect(url_for('ticket_manager', user_id=current_user.id))
    return render_template("Admin/information.html")


@app.route('/Report/<int:user_id>', methods=['GET', 'POST'])
def report(user_id):
    return render_template("Admin/report.html", user=utils.get_user_by_id(user_id), list_report=utils.load_report()
                           )


@login.user_loader
def get_user(user_id):
    return utils.get_user_by_id(user_id=user_id)


if __name__ == '__main__':
    app.run(debug=True)
