"""Unittest for py_attributes file"""
###### Python Packages ######
import pygame

###### My Packages ######
from pyengine import CONFIG_PATH
from pyengine.libs.designer.py_attributes import Rectangle, Text

from pyengine.utils.json_handler import read_json


blueprint = read_json("ui_data/blueprint.json")
fonts = read_json(CONFIG_PATH).get("fonts_data")
Text.load_fonts(fonts)


def test_create_rect():
    """test create_rect method in Rectangle class"""
    box = blueprint.get("box").get("rect_data")
    circle = blueprint.get("circle").get("rect_data")

    box_rect = Rectangle.create_rect(box)
    circle_rect = Rectangle.create_rect(circle)

    assert isinstance(box_rect, pygame.Rect)
    assert circle_rect.size == (0, 0)


def test_update_text():
    """test update_text method in Text class"""
    text_attrs = blueprint.get("box").get("text_data")
    rect_attrs = blueprint.get("box").get("rect_data")

    rect_obj = Rectangle(rect_attrs)
    text_obj = Text(text_attrs, rect_obj.rect)

    text_obj.update_text(
        font="pixal_15", text="update", antialias=True, color="#ffffff", align="midleft"
    )

    assert text_obj._font == Text.fonts.get("pixal_15")
    assert text_obj._text == "update"
    assert text_obj._antialias
    assert text_obj._color == "#ffffff"
    assert text_obj._align == "midleft"


def test_set_text():
    """test set_text method in Text class"""
    text_attrs = blueprint.get("box").get("text_data")
    rect_attrs = blueprint.get("box").get("rect_data")

    rect_obj = Rectangle(rect_attrs)
    text_obj = Text(text_attrs, rect_obj.rect)

    assert text_obj._font == Text.fonts.get("pixal_35")
    assert text_obj._text == ""
    assert not text_obj._antialias
    assert text_obj._color == "#000000"
    assert text_obj._align == "center"


def test_set_algin():
    """test set_align method in Text class"""
    text_attrs = blueprint.get("box").get("text_data")
    rect_attrs = blueprint.get("box").get("rect_data")

    rect_obj = Rectangle(rect_attrs)
    text_obj = Text(text_attrs, rect_obj.rect)

    x_text = text_obj._font_size[0]
    y_text = text_obj._font_size[1]
    half_x_text = text_obj._font_size[0] // 2
    half_y_text = text_obj._font_size[1] // 2

    x_rect = text_obj._rect_size[0]
    y_rect = text_obj._rect_size[1]
    half_x_rect = text_obj._rect_size[0] // 2
    half_y_rect = text_obj._rect_size[1] // 2

    text_obj.set_align("top")
    assert text_obj._align == "top"
    assert text_obj.align_x == abs(half_x_text - half_x_rect)
    assert text_obj.align_y == 0

    text_obj.set_align("topleft")
    assert text_obj._align == "topleft"
    assert text_obj.align_x == 0
    assert text_obj.align_y == 0

    text_obj.set_align("topright")
    assert text_obj._align == "topright"
    assert text_obj.align_x == abs(x_text - x_rect)
    assert text_obj.align_y == 0

    text_obj.set_align("center")
    assert text_obj._align == "center"
    assert text_obj.align_x == abs(half_x_text - half_x_rect)
    assert text_obj.align_y == abs(half_y_text - half_y_rect)

    text_obj.set_align("midleft")
    assert text_obj._align == "midleft"
    assert text_obj.align_x == 0
    assert text_obj.align_y == abs(half_y_text - half_y_rect)

    text_obj.set_align("midright")
    assert text_obj._align == "midright"
    assert text_obj.align_x == abs(x_text - x_rect)
    assert text_obj.align_y == abs(half_y_text - half_y_rect)

    text_obj.set_align("bottom")
    assert text_obj._align == "bottom"
    assert text_obj.align_x == abs(half_x_text - half_x_rect)
    assert text_obj.align_y == abs(y_text - y_rect)

    text_obj.set_align("bottomleft")
    assert text_obj._align == "bottomleft"
    assert text_obj.align_x == 0
    assert text_obj.align_y == abs(y_text - y_rect)

    text_obj.set_align("bottomright")
    assert text_obj._align == "bottomright"
    assert text_obj.align_x == abs(x_text - x_rect)
    assert text_obj.align_y == abs(y_text - y_rect)


def test_load_fonts():
    """test load_fonts method in Text class"""

    assert Text.fonts.get("pixal_35") is not None
    assert isinstance(Text.fonts.get("pixal_35"), pygame.font.Font)
