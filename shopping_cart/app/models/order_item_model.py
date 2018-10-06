# These are the models for the application

from datetime import datetime

from flask_bcrypt import Bcrypt
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime

from . import db


class OrderItems(db.Model):

    __tablename__ = 'OrderItems'

    id = db.Column(db.Integer, primary_key=True)
    oid = db.Column(db.Integer, nullable=False)
    cid = db.Column(db.Integer, nullable=False)
    pid = db.Column(db.Integer, nullable=False)
    qty = db.Column(db.Integer, nullable=False, default=1)

    def __init__(self, oid, cid, pid, qty=1):
        self.oid = oid
        self.cid = cid
        self.pid = pid
        self.qty = qty
