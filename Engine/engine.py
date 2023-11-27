"""Project start point"""
###### Python Packges ######
import sys
import pygame

# pylint: disable=E1101
###### My Packges ######
from Engine.window import win_obj
from Engine.Libs.Eventer.eventer import Eventer
from Engine.Libs.json_handler import read_json
from Engine.Libs.path_handler import path_check
from Engine.Libs.Designer.designer import Designer
from Engine.Libs.Designer.py_attributes import Text
from Engine.Libs.DevTools.devtools import DevTools
from Engine.Libs.DevTools.debug_tools import Debugger


class PyEngine:
    """Main class that works as a connector for all packges"""

    def __init__(self):
        """Init engine object"""
        config_path = path_check("config.json", "defualt_config.json")
        game_config = read_json(config_path)

        fonts_attrs = game_config.get("fonts")
        devtools_attrs = game_config.get("devtools")
        events_attrs = game_config.get("events")

        Text.load_fonts(fonts_attrs)
        Debugger.load_debbuger_config(devtools_attrs)
        Eventer.load_global_events(events_attrs)

    def mainloop(self, debug=False):
        """Game mainloop"""
        while True:
            self.trigger_events()

            Designer.draw_group()
            if debug:
                DevTools.display_tools()

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
