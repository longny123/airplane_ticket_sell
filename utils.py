import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath('CongNghePhanMen1'))))
import hashlib
from sqlalchemy import update
from models import User, Tickets, Report, Receipt, ReceiptDetail
from CongNghePhanMen1 import db, app
from datetime import datetime


# def read_products(cate_id=None, kw=None, from_price=None, to_price=None):
#     products = Tickets.query
#
#     if cate_id:
#         products = products.filter(Tickets.category_id == cate_id)
#
#     if kw:
#         products = products.filter(Tickets.name.contains(kw))
#
#     if from_price and to_price:
#         products = products.filter(Tickets.price.__gt__(from_price),
#                                    Tickets.price.__lt__(to_price))
#
#     return products.all()

def load_tickets():
    return Tickets.query


def get_tickets_by_id(ticket_id):
    return Tickets.query.get(ticket_id)
    # products = read_data(path='data/products.json')
    # for p in products:
    #     if p["id"] == product_id:
    #         return p


def check_login(username, password):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())

    user = User.query.filter(User.username == username,
                             User.password == password,
                             ).first()

    return user


def get_user_by_id(user_id):
    return User.query.get(user_id)


def register_user(name, email, username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    u = User(name=name,
             email=email,
             username=username,
             password=password,
             user_role='user')
    try:
        db.session.add(u)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        return False


def add_ticket(name, starting_place, destination_place, starting_date, return_date, price):
    t = Tickets(name=name,
                starting_place=starting_place,
                destination_place=destination_place,
                date_starting=starting_date,
                date_return=return_date,
                price=price)
    try:
        db.session.add(t)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        return False


def edit_ticket(ticket_id, name, starting_place, destination_place, starting_date, return_date, price):
    ticket = Tickets.query.get(ticket_id)

    ticket.name = name
    ticket.starting_place = starting_place
    ticket.destination = destination_place
    ticket.date_starting = starting_date
    ticket.date_return = return_date
    ticket.price = price

    try:
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        return False


def delete_ticket(ticket_id):
    ticket = get_tickets_by_id(ticket_id)
    try:
        db.session.delete(ticket)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        return False


def get_list_user():
    return User.query


def confirm_ticket(ticket_id, user_id, quantity, price):
    receipt = Receipt(user_id=user_id)
    db.session.add(receipt)
    db.session.commit()
    # db.session.close()
    # session = db.Session()
    # receipt_created = session.query(Receipt).filter(Receipt.user_id==user_id)
    receipt_detail = ReceiptDetail(receipt_id=receipt.id,
                                   ticket_id=ticket_id,
                                   quantity=quantity,
                                   price=price * quantity)
    db.session.add(receipt_detail)

    try:
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        db.session.rollback()
        return False


def get_all_receipt():
    result = []
    user_receipt = db.session.query(Receipt, User).filter(Receipt.user_id == User.id).all()
    receipt_receipt_detail = db.session.query(Receipt, ReceiptDetail).filter(
        ReceiptDetail.receipt_id == Receipt.id).all()
    receipt_detail_ticket = db.session.query(Tickets, ReceiptDetail).filter(ReceiptDetail.ticket_id == Tickets.id).all()
    for i, j, k in zip(user_receipt, receipt_receipt_detail, receipt_detail_ticket):
        result = result + [i, j, k]
    return user_receipt, receipt_receipt_detail, receipt_detail_ticket


# def read_user(user_id=None, name=None, email=None, username=None, password=None, active=None, user_role=None):
#     list = User.query
#
#     if user_id:
#         list = list.filter(User.id == user_id)
#     if name:
#         list = list.filter(User.name == name)
#     if email:
#         list = list.filter(User.email == email)
#     if username:
#         list = list.filter(User.username == username)
#     if password:
#         list = list.filter(User.email == password)
#     if active:
#         list = list.filter(User.active == active)
#     if user_role:
#         list = list.filter(User.user_role == user_role)
#     return list.all()


def update_user(user_id=None, name=None, username=None, password=None):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

    user = User.query.get(user_id)
    user.name = name
    user.username = username
    user.password = password
    try:
        db.session.commit()
        return user
    except Exception as e:
        print(e)
        db.session.rollback()
        return False


def delete_user(user_id):
    user = get_user_by_id(user_id)
    try:
        db.session.delete(user)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        return False


def load_report():
    return Report.query


def add_report(name, kind, email, phone, message):
    r = Report(name=name,
               kind=kind,
               email=email,
               phone=phone,
               message=message)
    try:
        db.session.add(r)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        return False

# def cart_stats(cart):
#     total_amount, total_quantity = 0, 0
#     if cart:
#         for p in cart.values():
#             total_quantity = total_quantity + p["quantity"]
#             total_amount = total_amount + p["quantity"] * p["price"]
#
#     return total_quantity, total_amount
#
#
# def add_receipt(cart):
#     if cart:
#         receipt = Receipt(customer_id=1)
#         db.session.add(receipt)
#
#         for p in list(cart.values()):
#             detail = ReceiptDetail(receipt=receipt,
#                                    ticket_id=int(p["id"]),
#                                    quantity=p["quantity"],
#                                    price=p["price"])
#             db.session.add(detail)
#
#         try:
#             db.session.commit()
#             return True
#         except Exception as ex:
#             print(ex)
#
#     return False
