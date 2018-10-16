
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
#     params = Params("another@gmail.com", "another", "anotherpassword")
# )


# Params = collections.namedtuple(
#     'Filters', ["email", "username"])
# Filters = collections.namedtuple(
#     'Filters', ["uid", "email", "username"])
# sql = dml.update(
#     table="shoppers",
#     params=Params("t@g.com", "tina"),
#     filters=Filters(None, "tm@andela.com", "tinaxx")
# )
# print(sql)


Params = collections.namedtuple('Params', ["email", "username"])
Filters = collections.namedtuple(
    'Filters', "uid, email, username")
shoppers = dml.read(
    table="shoppers",
    columns=["uid", "username", "email"],
    filters=Filters(uid=None, username=None, email="someone@gmail.com")
)
print(shoppers)