"""Unittest for designer file"""
###### Python Packages ######

###### My Packages ######
from pyengine.window import CONFIG_PATH

from pyengine.libs.designer.designer import Designer
from pyengine.libs.designer.py_elements import PyRect, PyCircle, PyButton
from pyengine.libs.designer.py_attributes import Text

from pyengine.utils.json_handler import read_json


blueprint = read_json("ui_data/blueprint.json")
fonts = read_json(CONFIG_PATH).get("fonts_data")
Text.load_fonts(fonts)


def test_create_element():
    """test create_element method in Designer class"""

    rect_attr = blueprint.get("box")
    circle_attr = blueprint.get("circle")
    button_attr = blueprint.get("button")

    Designer.create_element(rect_attr)
    Designer.create_element(circle_attr)
    Designer.create_element(button_attr)

    assert isinstance(Designer.get_element("box"), PyRect)
    assert isinstance(Designer.get_element("circle"), PyCircle)
    assert isinstance(Designer.get_element("button"), PyButton)


def test_get_element():
    """test get_element method in Designer class"""
    rect_attr = blueprint.get("box")

    Designer.create_element(rect_attr)

    assert Designer.get_element("box").name == "box"
    assert Designer.get_element("unknown") is None
