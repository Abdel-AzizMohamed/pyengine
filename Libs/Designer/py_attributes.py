"""Contains all the ui elements attributes and their methods (text, rect, ...)"""
import pygame
from window import win_obj


class Rectangle:
    """Define a pygame Rectangle"""

    def __init__(self, rect_data):
        self.rect = self.set_rect(rect_data)

    def set_rect(self, rect_data):
        """
        creates a new pygame rect object

        Attributes:
            rect_data: given rect data (size, postition)
        """
        x_pos = rect_data.get("x_pos") * (win_obj.screen_width / win_obj.y_ceil)
        y_pos = rect_data.get("y_pos") * (win_obj.screen_height / win_obj.x_ceil)

        x_size = rect_data.get("x_size") * (win_obj.screen_width / win_obj.y_ceil)
        y_size = rect_data.get("y_size") * (win_obj.screen_height / win_obj.x_ceil)

        return pygame.Rect((x_pos, y_pos), (x_size, y_size))
