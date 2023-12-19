"""Project start point"""
###### Python Packges ######
import sys
import pygame

# pylint: disable=E1101
###### My Packges ######
from Engine.window import win_obj
from Engine.Libs.Eventer.eventer import Eventer
from Engine.Libs.json_handler import read_json
from Engine.Libs.path_handler import alternate_path, walk_search
from Engine.Libs.Designer.designer import Designer
from Engine.Libs.Designer.py_attributes import Text
from Engine.Libs.DevTools.devtools import DevTools
from Engine.Libs.DevTools.debug_tools import Debugger
from Engine.Libs.errors_handler.data_checker import config_check, ui_check


class PyEngine:
    """Main class that works as a connector for all packges"""

    @staticmethod
    def mainloop(debug: bool = False) -> None:
        """
        Game mainloop

        Arguments:
            debug: Display debugging tools
        """
        while True:
            PyEngine.trigger_events(debug)

            Designer.draw_group()
            if debug:
                DevTools.display_tools()

            pygame.display.update()
            win_obj.clock.tick(win_obj.fps)

    @staticmethod
    def trigger_events(debug: bool) -> None:
        """
        Trigger all game events

        Arguments:
            debug: Trigger debugging events if true
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT and debug:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            Eventer.trigger_events(event)

    @staticmethod
    def load_data() -> None:
        """Loads game data"""
        config_path = alternate_path("config.json", "defualt_config.json")
        config_check(config_path)
        game_config = read_json(config_path)

        for file in walk_search("UiData"):
            ui_check(file, config_path)

        fonts_attrs = game_config.get("fonts")
        devtools_attrs = game_config.get("devtools")
        events_attrs = game_config.get("events")

        Text.load_fonts(fonts_attrs)
        Debugger.load_debbuger_config(devtools_attrs)
        Eventer.load_global_events(events_attrs)
