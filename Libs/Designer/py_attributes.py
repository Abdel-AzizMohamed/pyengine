"""Contains all the ui elements attributes and their methods (text, rect, ...)"""
###### Python Packges ######
import pygame

###### My Packges ######
from window import win_obj
from Libs.json_handler import read_json


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

        x_size = round(
            rect_data.get("x_size") * (win_obj.screen_width / win_obj.y_ceil)
        )
        y_size = round(
            rect_data.get("y_size") * (win_obj.screen_height / win_obj.x_ceil)
        )

        return pygame.Rect((x_pos, y_pos), (x_size, y_size))


class Text:
    """Define a pygame Text"""

    fonts = {}

    def __init__(self, text_data):
        """Init new pygame text object"""
        self.font = None
        self.text = None
        self.antialias = None
        self.color = None

        self.text_obj = self.set_text(text_data)

    def set_text(self, text_data):
        """
        creates a new pygame text object

        Attributes:
            text_data: given text data (color, text, font)
        """
        if not isinstance(text_data, dict):
            raise TypeError("text data should be dict")

        font = text_data.get("font")
        text = text_data.get("text")
        antialias = text_data.get("antialias")
        color = text_data.get("color")

        if text is None:
            raise ValueError("Provide text for the given element")
        if not isinstance(text, str):
            raise TypeError("text should be string")

        if antialias is None:
            raise ValueError("Provide antialias for the given element")
        if not isinstance(antialias, bool):
            raise TypeError("antialias should be boolen")

        if color is None:
            raise ValueError("Provide color for the given element")
        if not isinstance(color, str):
            raise TypeError("color should be string")

        if font is None:
            raise ValueError("Provide font for the given element")
        if not isinstance(font, str):
            raise TypeError("font should be string")

        font_obj = self.fonts.get(font)

        if font_obj is None:
            raise ValueError("Provide a valid font")

        self.font = font
        self.text = text
        self.antialias = antialias
        self.color = color

        return font_obj.render(text, antialias, color)

    @staticmethod
    def load_fonts():
        """Loads all game fonts from config file"""
        fonts_file = read_json("defualt_config.json").get("fonts")

        if not isinstance(fonts_file, dict):
            raise TypeError("fonts data should be dict")

        for name, font in fonts_file.items():
            font_path = font.get("font_path")
            size = font.get("size")

            if font_path is None:
                raise ValueError("Provide font path for the given element")
            if not isinstance(font_path, str):
                raise TypeError("font path should be string")

            if size is None:
                raise ValueError("Provide size for the given element")
            if not isinstance(size, int):
                raise TypeError("size should be integer")

            py_font = pygame.font.Font(font_path, size)
            Text.fonts[name] = py_font
