"""Unittest for designer file"""
###### Python Packges ######
import pytest

###### My Packges ######
from Libs.Designer.designer import Designer
from Libs.Designer.py_elements import PyRect


def test_create_element():
    """test the basic use"""
    designer = Designer()

    rect_attr = {
        "name": "box1",
        "group": "boxGroup",
        "rect": {"x_pos": 0, "y_pos": 0, "x_size": 1, "y_size": 1},
    }

    designer.create_element("PyRect", rect_attr)

    assert isinstance(designer.game_elements.get("boxGroup").get("box1"), PyRect)


def test_create_element_wrong_value():
    """test if a wrong value passed"""
    designer = Designer()

    wrong_name = {
        "name": 1,
        "rect": {"x_pos": 0, "y_pos": 0, "x_size": 1, "y_size": 1},
    }
    wrong_group = {
        "group": 1,
        "rect": {"x_pos": 0, "y_pos": 0, "x_size": 1, "y_size": 1},
    }

    with pytest.raises(ValueError) as _:
        designer.create_element("PyRect", wrong_name)

    with pytest.raises(ValueError) as _:
        designer.create_element("PyRect", wrong_group)


def test_create_element_missing_value():
    """test if a missing value passed"""
    designer = Designer()

    no_name = {
        "group": "boxGroup",
        "rect": {"x_pos": 0, "y_pos": 0, "x_size": 1, "y_size": 1},
    }
    no_group = {
        "name": "box1",
        "rect": {"x_pos": 0, "y_pos": 0, "x_size": 1, "y_size": 1},
    }

    with pytest.raises(ValueError) as _:
        designer.create_element("PyRect", no_name)

    with pytest.raises(ValueError) as _:
        designer.create_element("PyRect", no_group)


def test_create_element_wrong_type():
    """test if a wrong type passed"""
    designer = Designer()

    with pytest.raises(TypeError) as _:
        designer.create_element("PyRect", "")


def test_get_element():
    """test the basic use"""
    designer = Designer()

    rect_attr = {
        "name": "box1",
        "group": "boxGroup",
        "rect": {"x_pos": 0, "y_pos": 0, "x_size": 1, "y_size": 1},
    }

    designer.create_element("PyRect", rect_attr)

    assert designer.game_elements.get("boxGroup").get("box1") == designer.get_element(
        "box1"
    )
    assert designer.get_element("unknown") is None


def test_get_element_wrong_type():
    """test if a wrong type passed"""
    designer = Designer()

    rect_attr = {
        "name": "box1",
        "group": "boxGroup",
        "rect": {"x_pos": 0, "y_pos": 0, "x_size": 1, "y_size": 1},
    }

    designer.create_element("PyRect", rect_attr)

    with pytest.raises(TypeError) as _:
        designer.get_element(1)
