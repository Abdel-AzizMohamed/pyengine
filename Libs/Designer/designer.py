"""Define the main designer file"""
import pygame
from window import win_obj
from Libs.Designer.py_elements import PyRect


classes = {"PyRect": PyRect}


class Designer:
    """Define the main grahpic helper"""

    def __init__(self):
        """
        init a new Designer object

        Attributes:
            elements: dict of all game elements
        """
        self.elements = {}

    def create_element(self, ele_class, ele_attributes):
        """
        creates a new element

        Arguments:
            ele_class: element class name
            ele_attributes: element attributes (text, color, ...)
            ele_group: element group
        """
        element = classes[ele_class](ele_attributes)
        ele_group = ele_attributes.get("group")

        if not self.elements.get(ele_group):
            self.elements[ele_group] = {}

        self.elements.get(ele_group)[element.name] = element

    def read_ui(self, file_path):
        """read given ui file"""

    def get_element(self, name):
        """gets element by its name"""
        for group in self.elements.values():
            for key, item in group.items():
                if key == name:
                    return item
        return None

    def draw_group(self):
        """draw elements on screen"""
        for group in self.elements.values():
            for item in group.values():
                if item.type == "rect":
                    pygame.draw.rect(win_obj.screen, "#FFFFFF", item.rect)
