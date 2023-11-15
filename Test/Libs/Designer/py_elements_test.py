"""Unittest for designer file"""
###### Python Packges ######
# import pytest

###### My Packges ######
from Libs.Designer.py_elements import PyRect
from Libs.Designer.py_attributes import Text
from Libs.json_handler import read_json


element_print = read_json("blueprint.json")


def test_pyrect_init():
    """test init method for PyRect"""
    attrs = element_print.get("box")

    Text.load_fonts()
    obj = PyRect(attrs)

    assert obj.name == attrs.get("name")
    assert obj.group == attrs.get("group")
    assert obj.type == "rect"
