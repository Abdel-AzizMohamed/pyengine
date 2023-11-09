"""Unittest for designer file"""
###### Python Packges ######
import pytest

###### My Packges ######
from Libs.Designer.py_attributes import Rectangle
from window import win_obj


def test_rectangle_init():
    """test basic of init"""
    attrs = {"x_pos": 1, "y_pos": 1, "x_size": 1, "y_size": 1}
    obj = Rectangle(attrs)

    x_pos = round(attrs.get("x_pos") * (win_obj.screen_width / win_obj.y_ceil))
    y_pos = round(attrs.get("y_pos") * (win_obj.screen_height / win_obj.x_ceil))

    x_size = round(attrs.get("x_size") * (win_obj.screen_width / win_obj.y_ceil))
    y_size = round(attrs.get("y_size") * (win_obj.screen_height / win_obj.x_ceil))

    assert obj.rect.x == x_pos
    assert obj.rect.y == y_pos
    assert obj.rect.size[0] == x_size
    assert obj.rect.size[1] == y_size


def test_rectangle_set_rect_bad_value():
    """test set_rect bad value"""
    no_rect = {}
    no_x_pos = {"y_pos": 1, "x_size": 1, "y_size": 1}
    no_y_pos = {"x_pos": 1, "x_size": 1, "y_size": 1}
    no_x_size = {"x_pos": 1, "y_pos": 1, "x_size": 1}
    no_y_size = {"x_pos": 1, "y_pos": 1, "y_size": 1}

    with pytest.raises(ValueError) as _:
        Rectangle(no_rect)

    with pytest.raises(ValueError) as _:
        Rectangle(no_x_pos)
    with pytest.raises(ValueError) as _:
        Rectangle(no_y_pos)

    with pytest.raises(ValueError) as _:
        Rectangle(no_x_size)
    with pytest.raises(ValueError) as _:
        Rectangle(no_y_size)


def test_rectangle_set_rect_bad_type():
    """test set_rect bad value"""
    no_dict_rect = 1
    no_int_x_pos = {"x_pos": 1.1, "y_pos": 1, "x_size": 1, "y_size": 1}
    no_int_y_pos = {"x_pos": 1, "y_pos": 1.1, "x_size": 1, "y_size": 1}
    no_int_x_size = {"x_pos": 1, "y_pos": 1, "x_size": 1.1, "y_size": 1}
    no_int_y_size = {"x_pos": 1, "y_pos": 1, "x_size": 1, "y_size": 1.1}

    with pytest.raises(TypeError) as _:
        Rectangle(no_dict_rect)

    with pytest.raises(TypeError) as _:
        Rectangle(no_int_x_pos)
    with pytest.raises(TypeError) as _:
        Rectangle(no_int_y_pos)

    with pytest.raises(TypeError) as _:
        Rectangle(no_int_x_size)
    with pytest.raises(TypeError) as _:
        Rectangle(no_int_y_size)
