import pytest

from shopping_cart.db_wrapper.tools.wrapper import DBWrapper, DMLQuery


def test_DBWrapper_is_an_abstact_class():
    """Can't instantiate abstract class DBWrapper"""
    with pytest.raises(TypeError):
        DBWrapper("test_conn")


def test_DMLQuery_type():
    assert issubclass(DMLQuery, DBWrapper)


def test_no_conn():
    with pytest.raises(ValueError):
        DMLQuery(None)


def test_read():
    pass