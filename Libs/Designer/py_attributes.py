"""Contains all the ui elements attributes and their methods (text, rect, ...)"""
###### Python Packges ######
import pygame

###### My Packges ######
from window import win_obj
from Libs.json_handler import read_json
from Libs.error_handler import data_check
from Libs.path_handler import path_check


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
        data_check(rect_data, dict)

        x_pos = rect_data.get("x_pos")
        y_pos = rect_data.get("y_pos")
        x_size = rect_data.get("x_size")
        y_size = rect_data.get("y_size")

        data_check(x_pos, int)
        data_check(y_pos, int)
        data_check(x_size, int)
        data_check(y_size, int)

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
        data_check(text_data, dict)

        font = text_data.get("font")
        text = text_data.get("text")
        antialias = text_data.get("antialias")
        color = text_data.get("color")

        data_check(text, str)
        data_check(antialias, bool)
        data_check(color, str)
        data_check(font, str)

        font_obj = self.fonts.get(font)

        data_check(font_obj, pygame.font.Font)

        self.font = font
        self.text = text
        self.antialias = antialias
        self.color = color

        return font_obj.render(text, antialias, color)

    @staticmethod
    def load_fonts():
        """Loads all game fonts from config file"""
        config_path = path_check("config.json", "defualt_config.json")
        fonts_file = read_json(config_path).get("fonts")

        data_check(fonts_file, dict)

        for name, font in fonts_file.items():
            font_path = font.get("font_path")
            size = font.get("size")

            data_check(font_path, str)
            data_check(size, int)

            py_font = pygame.font.Font(font_path, size)
            Text.fonts[name] = py_font
