"""Contains unitest for path_handler moudle"""
###### Python Packges ######
import pytest

###### My Packges ######
from Libs.path_handler import path_check


def test_path_check():
    """test for basic use of path_check"""
    assert path_check("engine.py") == "engine.py"
    assert path_check("", "engine.py") == "engine.py"

    with pytest.raises(FileNotFoundError) as _:
        path_check("")
