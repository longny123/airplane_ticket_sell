from flask import redirect
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from flask_login import logout_user, current_user
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath('CongNghePhanMen1'))))
# from models import Category, Tickets
from CongNghePhanMen1 import db, admin

class ContactView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html')


class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')

    def is_accessible(self):
        return current_user.is_authenticated


class AuthenticatedView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


# admin.add_view(AuthenticatedView(Category, db.session))
# admin.add_view(AuthenticatedView(Tickets, db.session))
admin.add_view(ContactView(name='Liên hệ'))
admin.add_view(LogoutView(name='Đăng xuất'))
