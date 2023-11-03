"""Contains all the basic ui elements (no images only pygame elements)"""
from Libs.Designer.py_attributes import Rectangle


class PyRect(Rectangle):
    """Define a basic rect shape"""

    def __init__(self, attributes):
        """
        init a new Rect object

        Attributes:
            attributes: contains all the element data (color, text, ...)
        """
        self.name = attributes.get("name")
        self.group = attributes.get("group")
        self.type = "rect"

        Rectangle.__init__(self, attributes.get("rect"))
