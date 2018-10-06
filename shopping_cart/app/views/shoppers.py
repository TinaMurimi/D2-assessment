import datetime
import json
import logging.config
import os
import re

from flask_restful import Api, Resource, reqparse

from app import config
from app.models.shopper_model import Shoppers, db
from app.schemas import ShopperSchema
from app.utils.helpers import encrpt_password, sql

shopper_schema = ShopperSchema()
shoppers_schema = ShopperSchema(many=True)


class ShopperAPI(Resource):
    def __init__(self):
        super().__init__()

        print("\nlog_config.ini")
        print(os.path.join(config.ROOT_DIR, "logging.ini"))
        logging.config.fileConfig(os.path.join(
            config.ROOT_DIR, "logging.ini"))
        self.logger = logging.getLogger()

        self.reqparse = reqparse.RequestParser(bundle_errors=True)
        self.reqparse.add_argument(
            "username", type=str, required=True, help='username used for login')
        self.reqparse.add_argument("email", type=str, required=True,
                                   help='Email Address')
        self.reqparse.add_argument("password", type=str, required=True,
                                   help='User login password')

    def post(self):
        args = self.reqparse.parse_args()
        username = args['username'].strip()
        email = args['email'].strip()
        password = args['password'].strip()

        if not username or not email or not password:
            return {'Error': 'All fields are required'}, 400

        email_regex = re.compile(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

        if not email_regex.match(email):
            return {'Error': 'Not a valid email'}, 400

        if len(password) < 8 or len(password) > 15:
            return {'Message': 'Password should have 8-15 characters'}, 400

        try:
            # Check if a user exists with the given email or username
            query = (
                "SELECT EXISTS("
                f"SELECT email, username FROM shoppers WHERE email='{email}' "
                "UNION "
                f"SELECT email, username FROM shoppers WHERE username='{username}');"
            )
            args = {"email": email, "username": username}
            shoppers = sql(db.session, query, args).first()
            if shoppers[0]:
                msg = f"User with the email '{email}' or username '{username}' already exists"
                return {'Error': msg}, 409

            # Create a new shopper
            self.logger.info("Creating a new shopper account")
            query = (
                "INSERT INTO shoppers (username, email, password) "
                "VALUES (:username, :email, :password);")
            args["password"] = encrpt_password(password)
            shoppers = sql(db.session, query, args)

            self.logger.info(f"Created a new shopper account for {username}")
            return {'Message': 'New user registered successfully'}, 201

        except Exception as error:
            db.session.rollback()
            return {'Error': str(error)}, 400
