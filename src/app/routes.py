from flask import Blueprint
from flask_restful import Api
from app.views import Home

Routes = Blueprint('routes', __name__, cli_group=None)
api = Api(Routes)


api.add_resource(Home, '/home')