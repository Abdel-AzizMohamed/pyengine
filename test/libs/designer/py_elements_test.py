"""Unittest for py_elements file"""

###### Python Built-in Packages ######

###### Type Hinting ######

###### Python Packages ######

###### My Packages ######
from pyengine.libs.designer.py_elements import PyRect, PyCircle, PyButton
from pyengine.libs.designer.py_attributes import Text
from pyengine.utils.json_handler import read_json


blueprint = read_json("test/ui_test/blueprint_test.json")
config_data = read_json("test/config_test.json")
fonts = config_data.get("fonts_data")

Text.load_fonts(fonts)


def test_py_rect_init():
    """Test init method in PyRect class"""
    rect_attrs = blueprint.get("rect")
    rect_obj = PyRect(rect_attrs)

    assert isinstance(rect_obj, PyRect)

    assert rect_obj.color == rect_attrs.get("obj_data").get("color")
    assert rect_obj.opacity == rect_attrs.get("obj_data").get("opacity")


def test_py_circle_init():
    """Test init method in PyCircle class"""
    circle_attrs = blueprint.get("circle")
    circle_obj = PyCircle(circle_attrs)

    assert isinstance(circle_obj, PyCircle)

    assert circle_obj.radius == circle_attrs.get("obj_data").get("radius")
    assert circle_obj.color == circle_attrs.get("obj_data").get("color")
    assert circle_obj.opacity == circle_attrs.get("obj_data").get("opacity")

    assert (
        circle_obj.rect.size[0]
        == circle_attrs.get("obj_data").get("radius") * 2
    )
    assert (
        circle_obj.rect.size[1]
        == circle_attrs.get("obj_data").get("radius") * 2
    )


def test_py_button_init():
    """Test init method in PyButton class"""
    button_attrs = blueprint.get("button")
    button_obj = PyButton(button_attrs)

    assert isinstance(button_obj, PyButton)

    assert button_obj.active == button_attrs.get("obj_data").get("active")
    assert button_obj.disabled == button_attrs.get("obj_data").get("disabled")
    assert button_obj.active_color == button_attrs.get("obj_data").get(
        "base_color"
    )
    assert button_obj.active_color == button_attrs.get("obj_data").get(
        "base_color"
    )
    assert button_obj.base_color == button_attrs.get("obj_data").get(
        "base_color"
    )
    assert button_obj.hover_color == button_attrs.get("obj_data").get(
        "hover_color"
    )
    assert button_obj.select_color == button_attrs.get("obj_data").get(
        "select_color"
    )
    assert button_obj.disabled_color == button_attrs.get("obj_data").get(
        "disabled_color"
    )
    assert button_obj.opacity == button_attrs.get("obj_data").get("opacity")
