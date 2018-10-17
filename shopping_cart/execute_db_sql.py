
# import pytest
from unittest import mock
import collections

from db_wrapper.tools.wrapper import DBWrapper
from db_wrapper.tools.dmlquery import DMLQuery

from db_wrapper.tools import connect
from app.utils import config

# Create DB Connection
conn = connect.connect(**config.DB_SETTINGS)
print("DB connection successful")
print(conn)

# fk_conn = mock.Mock()
# dml = DMLQuery(fk_conn)
dml = DMLQuery(conn)

# Params = collections.namedtuple('Params', ["email", "username", "password"])
# sql = dml.create(
#     table="shoppers",
#     params = Params("brian@gmail.com", "brian", "brianpwd")
# )


# Params = collections.namedtuple(
#     'Filters', ["email", "username"])
# Filters = collections.namedtuple(
#     'Filters', ["uid", "email", "username"])
# sql = dml.update(
#     table="shoppers",
#     params=Params("briano@gmail.com", "tina"),
#     filters=Filters(None, "brian@gmail.com", None)
# )


Params = collections.namedtuple('Params', ["email", "username"])
Filters = collections.namedtuple(
    'Filters', "uid, email, username")
shoppers = dml.read(
    table="shoppers",
    columns=["uid", "username", "email"],
    filters=Filters(uid=None, username="tina", email=None)
)
print(shoppers)


Filters = collections.namedtuple(
    'Filters', "uid, email, username")
dml.delete(
    table="shoppers",
    filters=Filters(uid=None, username="tina", email=None)
)
