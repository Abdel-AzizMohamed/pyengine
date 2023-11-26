"""Project start point"""
###### Python Packges ######
import sys
import pygame

# pylint: disable=E1101
###### My Packges ######
from window import win_obj
from Libs.eventer import Eventer
from Libs.Designer.py_attributes import Text


class PyEngine:
    """Main class that works as a connector for all packges"""

    def __init__(self):
        """Init engine object"""
        Text.load_fonts()

    def mainloop(self, draw_group):
        """Game mainloop"""
        while True:
            self.trigger_events()
            draw_group()
            pygame.display.update()
            win_obj.clock.tick(win_obj.fps)

    def trigger_events(self):
        """Trigger all game events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            Eventer.trigger_events(event)
