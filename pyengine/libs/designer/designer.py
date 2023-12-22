"""Define the designer package start point"""
###### Python Packages ######
from typing import Union
import pygame

###### My Packages ######
from pyengine.window import win_obj
from pyengine.libs.eventer.eventer import Eventer
from pyengine.libs.designer.py_elements import PyRect, PyCircle, PyButton

from pyengine.utils.json_handler import read_json


class Designer:
    """
    Define the main graphic helper

    Attributes:
            elements_classes: Contains all the elements classes
            game_elements: dict of all game elements
    """

    elements_classes = {"PyRect": PyRect, "PyCircle": PyCircle, "PyButton": PyButton}
    game_elements = {}

    @staticmethod
    def create_element(element_attributes) -> None:
        """
        creates a new element

        Arguments:
            element_attributes: element attributes (text, color, ...)
        """

        base_data = element_attributes.get("base_data")

        ele_group = base_data.get("group")
        ele_name = base_data.get("name")
        ele_class = base_data.get("class")

        element = Designer.elements_classes[ele_class](element_attributes)

        Eventer.add_object_event(element, element_attributes.get("event_data"))

        if not Designer.game_elements.get(ele_group):
            Designer.game_elements[ele_group] = {}

        Designer.game_elements.get(ele_group)[ele_name] = element

    @staticmethod
    def create_from_file(file_path: str) -> None:
        """
        Create all elements in a given ui file

        Arguments:
            file_path: ui file path
        """
        ui_data = read_json(file_path)

        for element_data in ui_data.values():
            Designer.create_element(element_data)

    @staticmethod
    def get_element(name: str) -> Union[object, None]:
        """
        Returns element with the given name else None if not found

        Arguments:
            name: wanted element name
        """

        elements = [
            (key, item)
            for group in Designer.game_elements.values()
            for (key, item) in group.items()
        ]
        for key, item in elements:
            if key == name:
                return item
        return None

    @staticmethod
    def draw_groups() -> None:
        """Draw all the groups elements"""
        elements = [
            item for group in Designer.game_elements.values() for item in group.values()
        ]

        for element in elements:
            if element.type == "PyRect":
                pygame.draw.rect(win_obj.screen, element.color, element.rect)

            elif element.type == "PyCircle":
                pygame.draw.circle(
                    win_obj.screen,
                    element.color,
                    element.rect.center,
                    element.radius,
                )
            elif element.type == "PyButton":
                pygame.draw.rect(win_obj.screen, element.active_color, element.rect)

            if getattr(element, "font_render"):
                x_pos = element.rect.x + element.align_x
                y_pos = element.rect.y + element.align_y
                win_obj.screen.blit(element.font_render, (x_pos, y_pos))
