import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath('CongNghePhanMen1'))))
import hashlib
from CongNghePhanMen1.models import User
from CongNghePhanMen1 import db
from


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


# def get_product_by_id(product_id):
#     return Tickets.query.get(product_id)
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
    password1 = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    u = User(name=name,
             email=email,
             username=username,
             password=password1,
             user_role='user')
    try:
        db.session.add(u)
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
