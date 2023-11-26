"""Contains all the basic ui elements (no images only pygame elements)"""
from Engine.Libs.Designer.py_attributes import Rectangle, Text


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
        Text.__init__(self, attributes.get("text"), self.rect)


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
        Text.__init__(self, attributes.get("text"), self.rect)

        self.radius = attributes.get("rect").get("radius")
