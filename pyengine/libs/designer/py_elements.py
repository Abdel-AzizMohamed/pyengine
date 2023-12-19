"""Contains all the basic ui elements (no images only pygame elements)"""
from pyengine.libs.designer.py_attributes import Rectangle, Text


class PyBase:
    """Define a base class for basic shapes"""

    def __init__(self, attributes):
        """
        assign base data to elements

        Attributes:
            attributes: contains all the base data
        """
        self.name = attributes.get("name")
        self.group = attributes.get("group")
        self.type = attributes.get("type")


class PyRect(PyBase, Rectangle, Text):
    """Define a basic rect shape"""

    def __init__(self, attributes):
        """
        init a new Rect object

        Attributes:
            attributes: contains all the rect data
        """
        PyBase.__init__(self, attributes.get("base"))
        Rectangle.__init__(self, attributes.get("rect"))
        Text.__init__(self, attributes.get("text_obj"), self.rect)

        self.color = attributes.get("color")


class PyCircle(PyBase, Rectangle, Text):
    """Define a basic circle shape"""

    def __init__(self, attributes):
        """
        init a new Circle object

        Attributes:
            attributes: contains all the circle data
        """
        PyBase.__init__(self, attributes.get("base"))
        Rectangle.__init__(self, attributes.get("rect"))
        Text.__init__(self, attributes.get("text_obj"), self.rect)

        self.radius = attributes.get("rect").get("radius")
        self.color = attributes.get("color")


class PyButton(PyBase, Rectangle, Text):
    """Define a basic button object"""

    def __init__(self, attributes):
        """
        init a new Button object

        Attributes:
            attributes: contains all the button data
        """
        PyBase.__init__(self, attributes.get("base"))
        Rectangle.__init__(self, attributes.get("rect"))
        Text.__init__(self, attributes.get("text_obj"), self.rect)

        bt_attrs = attributes.get("button")

        self.active = bt_attrs.get("active")
        self.disabled = bt_attrs.get("disabled")

        self.active_color = self.base_color = bt_attrs.get("base_color")
        self.hover_color = bt_attrs.get("hover_color")
        self.select_color = bt_attrs.get("select_color")
        self.disabled_color = bt_attrs.get("disabled_color")
