# These are the models for the application

from datetime import datetime

from flask_bcrypt import Bcrypt
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime

from . import db

auth = HTTPBasicAuth()
bcrypt = Bcrypt()


class Shoppers(db.Model):
    """Model for the Shoppers table"""

    __tablename__ = 'Shoppers'

    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password.encode('utf8'), 12).decode('utf8')

    def __repr__(self):
        return '<User %r>' % (self.username)

    def get_id(self):
        """Return username to satisfy Flask-Login's requirements"""
        return self.username

    @auth.verify_password
    def verify_password(self, password):
        if bcrypt.check_password_hash(self.password, password):
            return True

        return False
