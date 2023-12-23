"""Define game events handler"""
#### Python Packages ####
from importlib import import_module
import pygame

# pylint: disable=E1101
#### My Packages ####
from pyengine.utils.collision_handler import mouse_collision


class Eventer:
    """Define main event class"""

    keyboard_keys = {
        "right": 1073741903,
        "left": 1073741904,
        "down": 1073741905,
        "up": 1073741906,
    }

    elements_events = {}
    global_events = []

    @staticmethod
    def add_object_event(element: object, event_data: dict) -> None:
        """
        Add event to given element

        Arguments:
            element: element the preform the event
            event_data: dict contains event_data {event, args}
        """
        if not event_data:
            return

        if not Eventer.elements_events.get(element.group):
            Eventer.elements_events[element.group] = []

        for func_path, data in event_data.items():
            module_path, str_func = func_path.split(":")

            func = getattr(import_module(module_path), str_func)

            Eventer.elements_events[element.group].append((func, data, element))

    @staticmethod
    def load_global_events(events: dict) -> None:
        """
        Load global events from config file

        Arguments:
            event_data: dict contains event_data {event, args}
        """
        if not events:
            return

        for func_path, data in events.items():
            module_path, str_func = func_path.split(":")

            func = getattr(import_module(module_path), str_func)

            Eventer.global_events.append((func, data))

    @staticmethod
    def trigger_events(event: pygame.event) -> None:
        """
        Trigger all global/elements events

        Arguments:
            event: event object from pygame to check for events
        """
        elements = [
            element for group in Eventer.elements_events.values() for element in group
        ]

        for element in elements:
            function = element[0]
            event_type = element[1].get("event")
            args = element[1].get("args").copy()
            args.insert(0, element[2])
            rect = element[2].rect

            if Eventer.check_mouse_event(event, event_type) and mouse_collision(rect):
                function(*args)
            if Eventer.check_keyboard_event(event, event_type):
                function(*args)

        for global_event in Eventer.global_events:
            function = global_event[0]
            event_type = global_event[1].get("event")
            args = global_event[1].get("args").copy()

            if Eventer.check_mouse_event(event, event_type):
                function(*args)
            if Eventer.check_keyboard_event(event, event_type):
                function(*args)

    @staticmethod
    def check_mouse_event(event: pygame.event, event_type: str) -> bool:
        """
        Check for mouse event

        Arguments:
            event: event object from pygame to check for events
            event_type: event type (leftclick, rightclick)
        """
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

    @staticmethod
    def check_keyboard_event(event: pygame.event, event_type: str) -> bool:
        """
        Check for keyboard event

        Arguments:
            event: event object from pygame to check for events
            event_type: event type (leftclick, rightclick)
        """

        key_action, key = event_type.split("_")

        if event.type == pygame.KEYDOWN and key_action == "down":
            if len(key) == 1 and event.key == ord(key):
                return True
            if event.key == Eventer.keyboard_keys.get(key):
                return True
        if event.type == pygame.KEYUP and key_action == "up":
            if len(key) == 1 and event.key == ord(key):
                return True
            if event.key == Eventer.keyboard_keys.get(key):
                return True

        return False
