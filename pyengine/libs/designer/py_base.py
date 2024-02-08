"""Contains base classes for ui elements"""

# pylint: disable=R0903
###### Python Built-in Packages ######
import os

#### Type Hinting ####
from typing import Tuple

###### Python Packages ######
import pygame

###### My Packages ######
from pyengine import win_obj


class PyBase:
    """Define a base class for basic ui data (name, group, ...etc)"""

    def __init__(self, attributes: dict) -> None:
        """
        Init a new base data to element

        Attributes:
            attributes: contains all the base data
        """
        self.name = attributes.get("name")
        self.group = attributes.get("group")
        self.type = attributes.get("class")


class PyImageBase:
    """Define a base class for image data"""

    loaded_images = {}

    def __init__(self, attributes: dict) -> None:
        """
        Init a new image base data to element

        Attributes:
            attributes: contains all the image base data
        """
        self.image = PyImageBase.loaded_images.get(attributes.get("image"))

    @staticmethod
    def load_image(image_data: Tuple[str, str]) -> None:
        """
        Load a given image

        Arguments:
            image_data: tuple contains image (image_name, image_path)
        """
        image_name, image_path = image_data

        if os.path.splitext(image_name)[1] == ".jpg":
            image = pygame.image.load(image_path).convert()
        else:
            image = pygame.image.load(image_path).convert_alpha()

        img_width = image.get_width()
        img_height = image.get_height()

        image = pygame.transform.scale(
            image,
            (
                img_width * win_obj.width_ratio,
                img_height * win_obj.height_ratio,
            ),
        )

        PyImageBase.loaded_images[image_name] = image
