"""Contains base classes for ui elements"""
# pylint: disable=R0903
###### Python Packages ######
###### My Packages ######
#### Type Hinting ####


class PyBase:
    """Define a base class for basic ui data (name, group, ...etc)"""

    def __init__(self, attributes: dict) -> None:
        """
        Init a new base data to elements

        Attributes:
            attributes: contains all the base data
        """
        self.name = attributes.get("name")
        self.group = attributes.get("group")
        self.type = attributes.get("class")
