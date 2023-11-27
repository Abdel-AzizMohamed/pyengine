"""Contains all the ui elements attributes and their methods (text, rect, ...)"""
###### Python Packges ######
import pygame

###### My Packges ######
from Engine.window import win_obj
from Engine.Libs.json_handler import read_json
from Engine.Libs.error_handler import data_check
from Engine.Libs.path_handler import path_check


class Rectangle:
    """Define a pygame Rectangle"""

    def __init__(self, rect_data):
        """Init new pygame rect object"""
        self.rect = self.set_rect(rect_data)

    def set_rect(self, rect_data):
        """
        creates a new pygame rect object

        Arguments:
            rect_data: given rect data (size, postition)
        """
        data_check(rect_data, dict)

        x_pos = rect_data.get("x_pos")
        y_pos = rect_data.get("y_pos")

        x_size = rect_data.get("x_size")
        y_size = rect_data.get("y_size")
        radius = rect_data.get("radius")

        data_check(x_pos, int)
        data_check(y_pos, int)

        x_pos = round(x_pos * (win_obj.screen_width / win_obj.y_ceil))
        y_pos = round(y_pos * (win_obj.screen_height / win_obj.x_ceil))

        if radius:
            x_size = y_size = radius * 2
        else:
            x_size = round(x_size * (win_obj.screen_width / win_obj.y_ceil))
            y_size = round(y_size * (win_obj.screen_height / win_obj.x_ceil))

        return pygame.Rect((x_pos, y_pos), (x_size, y_size))


class Text:
    """Define a pygame Text"""

    fonts = {}

    def __init__(self, text_data, rect):
        """Init new pygame text object"""
        self.font = None
        self.text = None
        self.antialias = None
        self.color = None
        self.align = None

        self.font_size = None
        self.rect_size = rect.size
        self.align_x = 0
        self.align_y = 0

        self.font_render = self.set_text(text_data)

    def update_text(self, font=None, text=None, antialias=None, color=None, align=None):
        """Update font properties"""
        self.font = self.font if font is None else self.fonts.get(font)
        self.text = self.text if text is None else text
        self.antialias = self.antialias if antialias is None else antialias
        self.color = self.color if color is None else color

        align = self.align if align is None else align

        self.font_render = self.font.render(self.text, self.antialias, self.color)
        self.font_size = self.font_render.get_rect().size

        self.set_align(align)

    def set_text(self, text_data):
        """
        creates a new pygame text object

        Arguments:
            text_data: given text data (color, text, font)
        """
        data_check(text_data, dict)

        font = text_data.get("font")
        text = text_data.get("text")
        antialias = text_data.get("antialias")
        color = text_data.get("color")
        align = text_data.get("align")

        data_check(text, str)
        data_check(antialias, bool)
        data_check(color, str)
        data_check(font, str)
        data_check(align, str)

        font_obj = self.fonts.get(font)

        data_check(font_obj, pygame.font.Font)

        self.font = font_obj
        self.text = text
        self.antialias = antialias
        self.color = color

        font_render = font_obj.render(text, antialias, color)
        self.font_size = font_render.get_rect().size

        self.set_align(align)

        return font_render

    def set_align(self, align):
        """
        Calculate the text alignment offest

        Arguments:
            align: text alignment (left, right, ...)
        """
        self.align = align

        x_text_size = self.font_size[0]
        y_text_size = self.font_size[1]
        half_x_text_size = self.font_size[0] // 2
        half_y_text_size = self.font_size[1] // 2

        x_rect_size = self.rect_size[0]
        y_rect_size = self.rect_size[1]
        half_x_rect_size = self.rect_size[0] // 2
        half_y_rect_size = self.rect_size[1] // 2

        if align == "top":
            self.align_x = abs(half_x_text_size - half_x_rect_size)
            self.align_y = 0
        if align == "topleft":
            self.align_x = 0
            self.align_y = 0
        if align == "topright":
            self.align_x = abs(x_rect_size - x_text_size)
            self.align_y = 0

        if align == "bottom":
            self.align_x = abs(half_x_text_size - half_x_rect_size)
            self.align_y = abs(y_text_size - y_rect_size)
        if align == "bottomleft":
            self.align_x = 0
            self.align_y = abs(y_text_size - y_rect_size)
        if align == "bottomright":
            self.align_x = abs(x_text_size - x_rect_size)
            self.align_y = abs(y_text_size - y_rect_size)

        if align == "center":
            self.align_x = abs(half_x_text_size - half_x_rect_size)
            self.align_y = abs(half_y_text_size - half_y_rect_size)
        if align == "midleft":
            self.align_x = 0
            self.align_y = abs(half_y_text_size - half_y_rect_size)
        if align == "midright":
            self.align_x = abs(x_text_size - x_rect_size)
            self.align_y = abs(half_y_text_size - half_y_rect_size)

    @staticmethod
    def load_fonts(fonts):
        """Loads all game fonts from config file"""
        data_check(fonts, dict)

        for name, font in fonts.items():
            font_path = font.get("font_path")
            size = font.get("size")

            data_check(font_path, str)
            data_check(size, int)

            py_font = pygame.font.Font(font_path, size)
            Text.fonts[name] = py_font
