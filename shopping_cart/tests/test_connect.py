import psycopg2
import pytest

from shopping_cart.db_wrapper.tools.connect import *
from shopping_cart.app.utils import config


def test_missing_db_cred():
    with pytest.raises(ValueError):
        get_credentials()

    with pytest.raises(ValueError):
        db_credentials = {
            'dbname': None,
            'dbuser': "db_user",
            'dbpass': "",
            'dbhost': "localhost"}
        get_credentials(**db_credentials)


def test_invalid_credentials():
    db_credentials = {
            'database': None,
            'user': "invalid_db_user08585",
            'password': "",
            'host': "localhost"}

    with pytest.raises(psycopg2.OperationalError):
        connect(**db_credentials)


def test_invalid_db():
    db_credentials = {
            'database': "invalid_db_name",
            'user': config.DB_SETTINGS["user"],
            'password': "",
            'host': "localhost"}

    with pytest.raises(psycopg2.OperationalError):
        connect(**db_credentials)


def test_connect():
    conn = connect(**config.DB_SETTINGS)

    print(conn)
    assert conn is not None
    assert conn.closed == 0
