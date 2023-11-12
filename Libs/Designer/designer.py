"""Define the designer packge start point"""
###### Python Packges ######
import pygame

###### My Packges ######
from window import win_obj
from Libs.Designer.py_elements import PyRect
from Libs.error_handler import data_check


class Designer:
    """
    Define the main grahpic helper

    Attributes:
            elements_classes: Contains all the elements classes
    """

    elements_classes = {"PyRect": PyRect}

    def __init__(self):
        """
        init a new Designer object

        Attributes:
            game_elements: dict of all game elements
        """
        self.game_elements = {}

    def create_element(self, ele_class, ele_attributes):
        """
        creates a new element

        Arguments:
            ele_class: element class name
            ele_attributes: element attributes (text, color, ...)
        """
        data_check(ele_attributes, dict)

        ele_group = ele_attributes.get("group")
        ele_name = ele_attributes.get("name")

        data_check(ele_name, str)
        data_check(ele_group, str)

        element = self.elements_classes[ele_class](ele_attributes)

        if not self.game_elements.get(ele_group):
            self.game_elements[ele_group] = {}

        self.game_elements.get(ele_group)[ele_name] = element

    def read_ui(self, file_path):
        """read given ui file"""

    def get_element(self, name):
        """
        gets element by its name

        Arguments:
            name: name to search for
        """
        data_check(name, str)

        elements = [
            (key, item)
            for group in self.game_elements.values()
            for (key, item) in group.items()
        ]
        for key, item in elements:
            if key == name:
                return item
        return None

    def draw_group(self):
        """draw elements on screen"""
        elements = [
            item for group in self.game_elements.values() for item in group.values()
        ]
        for item in elements:
            if item.type == "rect":
                pygame.draw.rect(win_obj.screen, "#FFFFFF", item.rect)

            if getattr(item, "text_obj"):
                win_obj.screen.blit(item.text_obj, item.rect)
