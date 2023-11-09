"""Contains all the ui elements attributes and their methods (text, rect, ...)"""
import pygame
from window import win_obj


class Rectangle:
    """Define a pygame Rectangle"""

    def __init__(self, rect_data):
        """Init new pygame rect object"""
        self.rect = self.set_rect(rect_data)

    def set_rect(self, rect_data):
        """
        creates a new pygame rect object

        Attributes:
            rect_data: given rect data (size, postition)
        """
        if rect_data is None:
            raise ValueError("provide rect data")
        if not isinstance(rect_data, dict):
            raise TypeError("rect data should be dict")

        x_pos = rect_data.get("x_pos")
        y_pos = rect_data.get("y_pos")
        x_size = rect_data.get("x_size")
        y_size = rect_data.get("y_size")

        if x_pos is None or y_pos is None:
            raise ValueError("Provide x_pos & y_pos for the given element")
        if not isinstance(x_pos, int) or not isinstance(y_pos, int):
            raise TypeError("x_pos & y_pos should be integer")

        if x_size is None or y_size is None:
            raise ValueError("Provide x_size & y_size for the given element")
        if not isinstance(x_size, int) or not isinstance(y_size, int):
            raise TypeError("x_size & y_size should be integer")

        x_pos = round(rect_data.get("x_pos") * (win_obj.screen_width / win_obj.y_ceil))
        y_pos = round(rect_data.get("y_pos") * (win_obj.screen_height / win_obj.x_ceil))

        x_size = round(rect_data.get("x_size") * (win_obj.screen_width / win_obj.y_ceil))
        y_size = round(rect_data.get("y_size") * (win_obj.screen_height / win_obj.x_ceil))

        return pygame.Rect((x_pos, y_pos), (x_size, y_size))
