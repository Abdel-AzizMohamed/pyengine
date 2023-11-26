"""Define a execption handling Events"""
#### Python Packges ####
from importlib import import_module
import pygame

# pylint: disable=E1101
#### My Packges ####
from Libs.collision_handler import mouse_collision


class Eventer:
    """Define main event halper"""

    elements_events = {}

    @classmethod
    def add_object_event(cls, element, event_data):
        """
        Add event to given element

        Arguments:
            element: element the preform the event
            event_data: element events data
        """
        if not event_data:
            return

        if not cls.elements_events.get(element.group):
            cls.elements_events[element.group] = []

        for func_path, data in event_data.items():
            moudle_path, str_func = func_path.split(":")

            func = getattr(import_module(moudle_path), str_func)

            cls.elements_events[element.group].append((func, data, element))

    @classmethod
    def trigger_events(cls, event):
        """
        Trigger all the elements events

        Arguments:
            event: event object from pygame to check for events
        """
        elements = [
            element for group in cls.elements_events.values() for element in group
        ]

        for element in elements:
            function = element[0]
            event_type = element[1].get("event")
            args = element[1].get("args").copy()
            args.insert(0, element[2])
            rect = element[2].rect

            if Eventer.check_mouse_event(event, event_type) and mouse_collision(rect):
                function(*args)

    @staticmethod
    def check_mouse_event(event, event_type):
        """Check for mouse event"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event_type == "click":
                return True
            if event.button == 1 and event_type == "leftclick":
                return True
            if event.button == 2 and event_type == "middleclick":
                return True
            if event.button == 3 and event_type == "rightclick":
                return True
        return False
