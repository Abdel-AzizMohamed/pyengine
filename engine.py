"""Define Engine file that contains the main logic"""
###### Python Packges ######
import sys
import pygame

###### My Packges ######
from window import Window


class PyEngine():
    """the main class that that works as a connector for all packges"""
    def __init__(self):
        """Init Engine Object"""
        self.window = Window()

    def mainloop(self):
        """Game Mainloop"""

    def load_assets(self):
        """Load game assets that includes (audio, images, ui data, ...)"""

    def trigger_events(self):
        """trigger all game events"""
