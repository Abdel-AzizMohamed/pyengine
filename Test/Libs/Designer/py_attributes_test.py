"""Unittest for designer file"""
###### Python Packges ######
import pytest

###### My Packges ######
from Libs.json_handler import read_json
from Libs.Designer.py_attributes import Rectangle, Text
from window import win_obj


element_print = read_json("blueprint.json")


def test_rectangle_init():
    """test basic of init"""
    attrs = element_print.get("box").get("rect")
    obj = Rectangle(attrs)

    x_pos = round(attrs.get("x_pos") * (win_obj.screen_width / win_obj.y_ceil))
    y_pos = round(attrs.get("y_pos") * (win_obj.screen_height / win_obj.x_ceil))

    x_size = round(attrs.get("x_size") * (win_obj.screen_width / win_obj.y_ceil))
    y_size = round(attrs.get("y_size") * (win_obj.screen_height / win_obj.x_ceil))

    color = attrs.get("color")

    assert obj.rect.x == x_pos
    assert obj.rect.y == y_pos
    assert obj.rect.size[0] == x_size
    assert obj.rect.size[1] == y_size
    assert obj.rect_color == color


def test_rectangle_set_rect_bad_value():
    """test set_rect bad value"""
    no_x_pos = element_print.get("box").get("rect").copy()
    del no_x_pos["x_pos"]

    no_y_pos = element_print.get("box").get("rect").copy()
    del no_y_pos["y_pos"]

    no_x_size = element_print.get("box").get("rect").copy()
    del no_x_size["x_size"]

    no_y_size = element_print.get("box").get("rect").copy()
    del no_y_size["y_size"]

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
    no_int_x_pos = element_print.get("box").get("rect").copy()
    no_int_x_pos["x_pos"] = 1.1

    no_int_y_pos = element_print.get("box").get("rect").copy()
    no_int_y_pos["y_pos"] = 1.1

    no_int_x_size = element_print.get("box").get("rect").copy()
    no_int_x_size["x_size"] = 1.1

    no_int_y_size = element_print.get("box").get("rect").copy()
    no_int_y_size["y_size"] = 1.1

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


def test_text_init():
    """test basic of init"""
    text_attrs = element_print.get("box").get("text")
    rect_attrs = element_print.get("box").get("rect")

    Text.load_fonts()

    rect_obj = Rectangle(rect_attrs)
    text_obj = Text(text_attrs, rect_obj.rect)

    assert isinstance(text_obj, Text)


def test_text_update_text():
    """test basic of text_update method"""
    text_attrs = element_print.get("box").get("text")
    rect_attrs = element_print.get("box").get("rect")
    Text.load_fonts()

    rect_obj = Rectangle(rect_attrs)
    text_obj = Text(text_attrs, rect_obj.rect)
    text_obj.update_text(
        font="pixal_15", text="update", antialias=True, color="#ffffff", align="midleft"
    )

    assert text_obj.font == Text.fonts.get("pixal_15")
    assert text_obj.text == "update"
    assert text_obj.antialias
    assert text_obj.color == "#ffffff"
    assert text_obj.align == "midleft"


def test_text_set_text():
    """test the basics of set_text method"""
    text_attrs = element_print.get("box").get("text")
    rect_attrs = element_print.get("box").get("rect")
    Text.load_fonts()

    rect_obj = Rectangle(rect_attrs)
    text_obj = Text(text_attrs, rect_obj.rect)

    assert text_obj.font == Text.fonts.get("pixal_35")
    assert text_obj.text == "test"
    assert not text_obj.antialias
    assert text_obj.color == "#000000"
    assert text_obj.align == "center"


def test_text_set_algin():
    """test the basics of set_align method"""
    text_attrs = element_print.get("box").get("text")
    rect_attrs = element_print.get("box").get("rect")
    Text.load_fonts()

    rect_obj = Rectangle(rect_attrs)
    text_obj = Text(text_attrs, rect_obj.rect)

    x_text = text_obj.font_size[0]
    y_text = text_obj.font_size[1]
    half_x_text = text_obj.font_size[0] // 2
    half_y_text = text_obj.font_size[1] // 2

    x_rect = text_obj.rect_size[0]
    y_rect = text_obj.rect_size[1]
    half_x_rect = text_obj.rect_size[0] // 2
    half_y_rect = text_obj.rect_size[1] // 2

    text_obj.set_align("top")
    assert text_obj.align == "top"
    assert text_obj.align_x == abs(half_x_text - half_x_rect)
    assert text_obj.align_y == 0

    text_obj.set_align("topleft")
    assert text_obj.align == "topleft"
    assert text_obj.align_x == 0
    assert text_obj.align_y == 0

    text_obj.set_align("topright")
    assert text_obj.align == "topright"
    assert text_obj.align_x == abs(x_text - x_rect)
    assert text_obj.align_y == 0

    text_obj.set_align("center")
    assert text_obj.align == "center"
    assert text_obj.align_x == abs(half_x_text - half_x_rect)
    assert text_obj.align_y == abs(half_y_text - half_y_rect)

    text_obj.set_align("midleft")
    assert text_obj.align == "midleft"
    assert text_obj.align_x == 0
    assert text_obj.align_y == abs(half_y_text - half_y_rect)

    text_obj.set_align("midright")
    assert text_obj.align == "midright"
    assert text_obj.align_x == abs(x_text - x_rect)
    assert text_obj.align_y == abs(half_y_text - half_y_rect)

    text_obj.set_align("bottom")
    assert text_obj.align == "bottom"
    assert text_obj.align_x == abs(half_x_text - half_x_rect)
    assert text_obj.align_y == abs(y_text - y_rect)

    text_obj.set_align("bottomleft")
    assert text_obj.align == "bottomleft"
    assert text_obj.align_x == 0
    assert text_obj.align_y == abs(y_text - y_rect)

    text_obj.set_align("bottomright")
    assert text_obj.align == "bottomright"
    assert text_obj.align_x == abs(x_text - x_rect)
    assert text_obj.align_y == abs(y_text - y_rect)
