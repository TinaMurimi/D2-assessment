# These are the models for the application

from datetime import datetime

from flask_bcrypt import Bcrypt
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime

from . import db


class Products(db.Model):

    __tablename__ = 'Products'

    code = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    unit_price = db.Column(db.Float, nullable=False)
    unitsInStock = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, product_name, description, unit_price, unitsInStock=0):
        self.product_name = list_name
        self.description = description
        self.unit_price = unit_price
        self.unitsInStock = unitsInStock

    def __repr__(self):
        """Return Product name"""
        return '<Product %r>' % (self.product_name)

    def get_id(self):
        """Return Product id"""
        return self.product_name
