from flask import redirect
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from flask_login import logout_user, current_user
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath('CongNghePhanMen1'))))
from models import User
from CongNghePhanMen1 import db, admin


class InformationView(BaseView):
    @expose('/')
    def index(self):
        return redirect('Admin/information.html')

    def is_accessible(self):
        return current_user.is_authenticated


class UserManagerView(BaseView):
    @expose('/')
    def index(self):
        return redirect('Admin/user_manager.html')

    def is_accessible(self):
        return current_user.is_authenticated


class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')

    def is_accessible(self):
        return current_user.is_authenticated


# class InformationView(BaseView):
#     @expose('/')
#     def index(self):
#         return self.render('Admin/information.html')
#
#     def is_accessible(self):
#         return current_user.is_authenticated
#
#
# class UserManagernView(BaseView):
#     @expose('/')
#     def index(self):
#         return self.render('Admin/user_manager.html')
#
#     def is_accessible(self):
#         return current_user.is_authenticated


class AuthenticatedView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


# admin.add_view(AuthenticatedView(Category, db.session))
# admin.add_view(AuthenticatedView(Tickets, db.session))
admin.add_view(LogoutView(name='Đăng xuất'))
admin.add_view(InformationView())
admin.add_view(UserManagerView())
