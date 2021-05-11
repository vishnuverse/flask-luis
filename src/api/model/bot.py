from flask_restx import fields, reqparse

common_header_args = reqparse.RequestParser()
common_header_args.add_argument("user_query", location="headers", help="String input for intent classification", required=True)