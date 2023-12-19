"""Define a execption handling Events"""
#### Python Packges ####
from importlib import import_module
import pygame

# pylint: disable=E1101
#### My Packges ####
from pyengine.utils.collision_handler import mouse_collision


class Eventer:
    """Define main event halper"""

    elements_events = {}
    global_events = []

    @staticmethod
    def add_object_event(element, event_data):
        """
        Add event to given element

        Arguments:
            element: element the preform the event
            event_data: element events data
        """
        if not event_data:
            return

        if not Eventer.elements_events.get(element.group):
            Eventer.elements_events[element.group] = []

        for func_path, data in event_data.items():
            moudle_path, str_func = func_path.split(":")

            func = getattr(import_module(moudle_path), str_func)

            Eventer.elements_events[element.group].append((func, data, element))

    @staticmethod
    def load_global_events(events):
        """
        Add a global event

        Arguments:
            event_data: events data
        """
        if not events:
            return

        for func_path, data in events.items():
            moudle_path, str_func = func_path.split(":")

            func = getattr(import_module(moudle_path), str_func)

            Eventer.global_events.append((func, data))

    @staticmethod
    def trigger_events(event):
        """
        Trigger all the elements events

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

        for global_event in Eventer.global_events:
            function = global_event[0]
            event_type = global_event[1].get("event")
            args = global_event[1].get("args").copy()

            if Eventer.check_mouse_event(event, event_type):
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
