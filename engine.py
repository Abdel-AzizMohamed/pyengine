"""Define Engine file that contains the main logic"""
###### Python Packges ######
import sys
import pygame

# pylint: disable=E1101
###### My Packges ######
from window import win_obj
from Libs.eventer import Eventer
from Libs.Designer.py_attributes import Text


class PyEngine:
    """the main class that that works as a connector for all packges"""

    def __init__(self):
        """Init Engine Object"""
        Text.load_fonts()

    def mainloop(self, draw_group):
        """Game Mainloop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                Eventer.trigger_events(event)
            draw_group()
            pygame.display.update()
            win_obj.clock.tick(win_obj.fps)

    def load_assets(self):
        """Load game assets that includes (audio, images, ui data, ...)"""

    def trigger_events(self):
        """trigger all game events"""
