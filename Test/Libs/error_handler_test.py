"""Contains unitest for error_handler moudle"""
###### Python Packges ######
import pytest

###### My Packges ######
from Engine.Libs.error_handler import data_check


def test_data_check():
    """test for basic use of data_check"""
    with pytest.raises(ValueError) as _:
        data_check(None, int)

    with pytest.raises(TypeError) as _:
        data_check(1, str)
