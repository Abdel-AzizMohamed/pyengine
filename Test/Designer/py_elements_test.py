"""Unittest for designer file"""
###### Python Packges ######
# import pytest

###### My Packges ######
from Libs.Designer.py_elements import PyRect


def test_pyrect_init():
    """test init method for PyRect"""
    attrs = {
        "name": "box1",
        "group": "boxGroup",
        "rect": {"x_pos": 0, "y_pos": 0, "x_size": 1, "y_size": 1},
    }
    obj = PyRect(attrs)

    assert obj.name == attrs.get("name")
    assert obj.group == attrs.get("group")
    assert obj.type == "rect"
