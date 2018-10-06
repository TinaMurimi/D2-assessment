# These are the models for the application

from datetime import datetime

from flask_bcrypt import Bcrypt
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime

from . import db


class Orders(db.Model):

    __tablename__ = 'Orders'

    oid = db.Column(db.Integer, primary_key=True)
    cid = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.DateTime,
                           default=datetime.now().isoformat(
                               sep=' ',
                               timespec='minutes'))

    def __init__(self, cid):
        self.cid = cid
        self.order_date = datetime.now().isoformat(
            sep=' ',
            timespec='minutes')
