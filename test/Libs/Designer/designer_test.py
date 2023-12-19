"""Unittest for designer file"""
###### Python Packges ######
import pytest

###### My Packges ######
from Engine.Libs.json_handler import read_json
from Engine.Libs.Designer.designer import Designer
from Engine.Libs.Designer.py_elements import PyRect
from Engine.Libs.Designer.py_attributes import Text


element_print = read_json("blueprint.json")


def test_create_element():
    """test the basic use"""
    designer = Designer()

    rect_attr = element_print.get("box")
    Text.load_fonts()

    designer.create_element("PyRect", rect_attr)

    assert isinstance(designer.game_elements.get("boxGroup").get("box1"), PyRect)


def test_create_element_wrong_type():
    """test if a wrong value passed"""
    designer = Designer()

    wrong_obj = ""
    wrong_name = element_print.get("box").copy()
    wrong_name["name"] = 1

    wrong_group = element_print.get("box").copy()
    wrong_group["group"] = 1

    with pytest.raises(TypeError) as _:
        designer.create_element("PyRect", wrong_obj)
    with pytest.raises(TypeError) as _:
        designer.create_element("PyRect", wrong_name)
    with pytest.raises(TypeError) as _:
        designer.create_element("PyRect", wrong_group)


def test_create_element_wrong_value():
    """test if a missing value passed"""
    designer = Designer()

    no_obj = None
    no_name = element_print.get("box").copy()
    del no_name["name"]

    no_group = element_print.get("box").copy()
    del no_group["group"]

    with pytest.raises(ValueError) as _:
        designer.create_element("PyRect", no_obj)
    with pytest.raises(ValueError) as _:
        designer.create_element("PyRect", no_name)
    with pytest.raises(ValueError) as _:
        designer.create_element("PyRect", no_group)


def test_get_element():
    """test the basic use"""
    designer = Designer()

    rect_attr = element_print.get("box")

    Text.load_fonts()

    designer.create_element("PyRect", rect_attr)

    assert designer.game_elements.get("boxGroup").get("box1") == designer.get_element(
        "box1"
    )
    assert designer.get_element("unknown") is None


def test_get_element_wrong_type():
    """test if a wrong type passed"""
    designer = Designer()

    rect_attr = element_print.get("box")

    Text.load_fonts()

    designer.create_element("PyRect", rect_attr)

    with pytest.raises(TypeError) as _:
        designer.get_element(1)
