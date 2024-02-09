"""Unittest for designer file"""

###### Python Built-in Packages ######
import os

###### Type Hinting ######

###### Python Packages ######

###### My Packages ######
from pyengine.libs.designer.designer import Designer
from pyengine.libs.designer.py_elements import PyRect, PyCircle, PyButton
from pyengine.libs.designer.py_attributes import Text
from pyengine.libs.designer.py_base import PyImageBase
from pyengine.libs.designer.py_sprite import PyImage

from pyengine.utils.json_handler import read_json
from pyengine.utils.path_handler import walk_search


blueprint = read_json("test/ui_test/blueprint_test.json")
config_data = read_json("test/config_test.json")
sprite_path = config_data.get("path_data").get("sprites_path")
fonts = config_data.get("fonts_data")

Text.load_fonts(fonts)

for image_path in walk_search(sprite_path):
    image_name = os.path.splitext(os.path.basename(image_path))[0]
    PyImageBase.load_image((image_name, image_path))


def test_create_element():
    """test create_element method in designer class"""

    rect_attr = blueprint.get("rect")
    circle_attr = blueprint.get("circle")
    button_attr = blueprint.get("button")
    image_attr = blueprint.get("image")

    Designer.create_element(rect_attr)
    Designer.create_element(circle_attr)
    Designer.create_element(button_attr)
    Designer.create_element(image_attr)

    elements_group = Designer.game_elements.get("test_group")
    rect_element = elements_group.get("rect")
    circle_element = elements_group.get("circle")
    button_element = elements_group.get("button")
    image_element = elements_group.get("image")

    assert elements_group is not None
    assert rect_element is not None
    assert circle_element is not None
    assert button_element is not None
    assert image_element is not None

    assert isinstance(elements_group, dict)
    assert isinstance(rect_element, PyRect)
    assert isinstance(circle_element, PyCircle)
    assert isinstance(button_element, PyButton)
    assert isinstance(image_element, PyImage)

    assert Designer.exclude_groups.get("test_group") is not None
    assert isinstance(Designer.exclude_groups.get("test_group"), int)
    assert Designer.exclude_groups.get("test_group") == 1


def test_create_from_file():
    """test create_from_file method in designer class"""
    Designer.create_from_file("test/ui_test/blueprint_test.json")

    elements_group = Designer.game_elements.get("test_group")
    rect_element = elements_group.get("rect")
    circle_element = elements_group.get("circle")
    button_element = elements_group.get("button")
    image_element = elements_group.get("image")

    assert elements_group is not None
    assert rect_element is not None
    assert circle_element is not None
    assert button_element is not None
    assert image_element is not None

    assert isinstance(elements_group, dict)
    assert isinstance(rect_element, PyRect)
    assert isinstance(circle_element, PyCircle)
    assert isinstance(button_element, PyButton)
    assert isinstance(image_element, PyImage)

    assert Designer.exclude_groups.get("test_group") is not None
    assert isinstance(Designer.exclude_groups.get("test_group"), int)
    assert Designer.exclude_groups.get("test_group") == 1


def test_get_element():
    """test get_element method in designer class"""
    rect_attr = blueprint.get("rect")

    Designer.create_element(rect_attr)

    assert Designer.get_element("rect") is not None
    assert isinstance(Designer.get_element("rect"), PyRect)
    assert Designer.get_element("test_none") is None


def test_remove_element():
    """test remove_element method in designer class"""
    rect_attr = blueprint.get("rect")

    Designer.create_element(rect_attr)
    Designer.remove_element("rect")

    assert Designer.get_element("rect") is None


def test_toggle_exclude():
    """test toggle_exclude method in designer class"""
    rect_attr = blueprint.get("rect")

    Designer.create_element(rect_attr)
    Designer.toggle_exclude("test_group")

    assert Designer.exclude_groups.get("test_group") == 0
    Designer.toggle_exclude("test_group")
    assert Designer.exclude_groups.get("test_group") == 1
