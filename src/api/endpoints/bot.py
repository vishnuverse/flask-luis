import json
from flask import request
from flask_restx import Resource
from api.namespaces import bot_ns
from api.model.bot import common_header_args
from actions.bot_action import ms_luis_connect
from constants.constants import SUCCESS, CODE_SUCCESS, MESSAGE_FETCHED


@bot_ns.route("/ms_bot", methods=["GET"])
class HelloWorld(Resource):
    @staticmethod
    @bot_ns.expect(common_header_args)
    def get():
        return {
            "status": SUCCESS,
            "code": CODE_SUCCESS,
            "message": MESSAGE_FETCHED,
            "result": ms_luis_connect(json.loads(request.data).get("user_query"))
        }
