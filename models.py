from sqlalchemy import Column, Integer, Float, String, \
    Boolean, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from enum import Enum as UserEnum
from datetime import datetime
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath('CongNghePhanMen1'))))
from CongNghePhanMen1 import db

class DbBase(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    def __str__(self):
        return self.name


# class Category(DbBase):
#     __tablename__ = 'category'
#     __table_args__ = {'extend_existing': True}
#
#     ticket = relationship('Tickets', backref='categories', lazy=True)
#
#
# class Tickets(DbBase):
#     __tablename__ = 'tickets'
#     __table_args__ = {'extend_existing': True}
#
#
#     starting_place = Column(String(255))
#     destination = Column(String(255))
#     price = Column(Float, default=0)
#     categories_id = Column(Integer, ForeignKey(Category.id),
#                          nullable=False)
#     receipt_details = relationship('ReceiptDetail', backref='tickets', lazy=True)
# user_role = Enum(value='USER_ROLE',
#             names=[
#                 ('user', 'user'),
#                 ('admin', 'admin'),
#                 ('admin_root', 'admin_root')
#             ]
#         )
#

class User(DbBase, UserMixin):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    email = Column(String(100))
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    active = Column(Boolean, default=True)
    user_role = Column(Enum('user', 'admin', name="ValueTypes"), default='user')
#     receipts = relationship('Receipt', backref='users', lazy=True)
#
#
# class Receipt(db.Model):
#     __table_args__ = {'extend_existing': True}
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     created_date = Column(DateTime, default=datetime.today())
#     user_id = Column(Integer, ForeignKey(User.id))
#     details = relationship('ReceiptDetail',
#                            backref='receipts', lazy=True)
#
#
# class ReceiptDetail(db.Model):
#     __table_args__ = {'extend_existing': True}
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     receipt_id = Column(Integer, ForeignKey(Receipt.id), nullable=False)
#     ticket_id = Column(Integer, ForeignKey(Tickets.id), nullable=False)
#     quantity = Column(Integer, default=0)
#     price = Column(Integer, default=0)


if __name__ == '__main__':
    db.create_all()
