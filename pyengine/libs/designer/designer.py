"""
Define the designer package start point

that handle all game graphics in more easier way
"""

# pylint: disable=E1101
###### Python Built-in Packages ######

###### Type Hinting ######
from typing import Union

###### Python Packages ######
import pygame

###### My Packages ######
from pyengine import win_obj, alpha_surface, CONFIG_DATA
from pyengine.libs.designer.py_elements import PyRect, PyCircle, PyButton
from pyengine.libs.designer.py_sprite import PyImage
from pyengine.libs.eventer.eventer import Eventer
from pyengine.libs.transition.transition import Transition

from pyengine.utils.json_handler import read_json


class Designer:
    """
    Define the main graphic helper class

    Attributes:
        elements_classes: Contains all the elements classes
        game_elements: dict of all game elements
    """

    elements_classes = {
        "PyRect": PyRect,
        "PyCircle": PyCircle,
        "PyButton": PyButton,
        "PyImage": PyImage,
    }
    game_elements = {}
    exclude_groups = {}

    @staticmethod
    def create_element(element_attributes: dict) -> None:
        """
        Creates a new element from a given data

        Arguments:
            element_attributes: element data (text, color, ...)
        """

        base_data = element_attributes.get("base_data")
        event_data = element_attributes.get("event_data")

        ele_group = base_data.get("group")
        ele_name = base_data.get("name")
        ele_class = base_data.get("class")

        element = Designer.elements_classes[ele_class](element_attributes)

        if not Designer.game_elements.get(ele_group):
            Designer.game_elements[ele_group] = {}
            Designer.exclude_groups[ele_group] = 1

            Eventer.exclude_groups[ele_group] = 1

            Transition.elements[ele_group] = {}
            Transition.exclude_groups[ele_group] = 1

        Eventer.add_object_event(element, event_data)
        Transition(element, element_attributes.get("transition_data"))

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
    def get_element(element_name: str) -> Union[object, None]:
        """
        Retrieve element object by the given name

        Arguments:
            name: element name

        Returns:
            element object else None if not found
        """

        elements = [
            (name, element)
            for group in Designer.game_elements.values()
            for (name, element) in group.items()
        ]
        for name, element in elements:
            if name == element_name:
                return element
        return None

    @staticmethod
    def remove_element(element_name: str) -> None:
        """
        Remove element by the given name

        Arguments:
            name: element name
        """
        for elements in Designer.game_elements.values():
            if element_name in elements:
                del elements[element_name]
                break

    @staticmethod
    def toggle_exclude(group_name: str) -> None:
        """
        Toggle visibility by the given name

        Arguments:
            group_name: group name
        """
        if Designer.exclude_groups.get(group_name) == 1:
            Designer.exclude_groups[group_name] = 0
            Eventer.exclude_groups[group_name] = 0
        else:
            Designer.exclude_groups[group_name] = 1
            Eventer.exclude_groups[group_name] = 1

    @staticmethod
    def draw_groups() -> None:
        """Draw all active groups"""
        elements = [
            element_data
            for (group_name, elements) in Designer.game_elements.items()
            for element_data in elements.values()
            if Designer.exclude_groups.get(group_name)
        ]

        for element in elements:
            surface = (
                alpha_surface
                if element.opacity
                and CONFIG_DATA.get("window_data").get("alpha")
                else win_obj.screen
            )

            if element.type == "PyRect" and element.color != "transparent":
                pygame.draw.rect(surface, element.color, element.rect)

            elif element.type == "PyCircle":
                pygame.draw.circle(
                    surface,
                    element.color,
                    element.rect.center,
                    element.radius,
                )
            elif (
                element.type == "PyButton"
                and element.base_color != "transparent"
            ):
                pygame.draw.rect(surface, element.active_color, element.rect)
            elif element.type == "PyImage":
                surface.blit(element.image, element.rect)

            if getattr(element, "font_render"):
                x_pos = element.rect.x + element.align_x
                y_pos = element.rect.y + element.align_y
                surface.blit(element.font_render, (x_pos, y_pos))

        if CONFIG_DATA.get("window_data").get("alpha"):
            win_obj.screen.blit(alpha_surface, (0, 0))
