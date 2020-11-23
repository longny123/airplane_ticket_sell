from flask_restful import Api
from flask import current_app as app

from server.config import Config
from ..controller.user_controller import UserRegister

api = Api(app)

api.add_resource(UserRegister, Config.ROUTE['USER'])

