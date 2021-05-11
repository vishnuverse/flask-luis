from flask import Blueprint
from flask_restx import Api
from api import endpoints
from api.namespaces import bot_ns


__endpoints__ = endpoints

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint, title='Reflections ChatBot', description='Chatbot using microsoft"s LUIS',
          version='1.0.0')
api.add_namespace(bot_ns)