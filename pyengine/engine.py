"""Project start point"""
###### Python Packages ######
import sys
import pygame

# pylint: disable=E1101
###### My Packages ######
from pyengine.window import win_obj, CONFIG_PATH
from pyengine.libs.eventer.eventer import Eventer
from pyengine.libs.designer.designer import Designer
from pyengine.libs.designer.py_attributes import Text
from pyengine.libs.devtools.devtools import DevTools
from pyengine.libs.devtools.debug_tools import Debugger
from pyengine.libs.mixer import Sound, Music

from pyengine.utils.json_handler import read_json

# from pyengine.utils.path_handler import walk_search
# from pyengine.utils.errors_handler.data_checker import config_check, ui_check


class PyEngine:
    """Main class that works as a connector for all packages"""

    @staticmethod
    def mainloop(debug: bool = False) -> None:
        """
        Game mainloop

        Arguments:
            debug: Display debugging tools
        """
        while True:
            PyEngine.trigger_events(debug)

            Designer.draw_groups()
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
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and debug:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            Eventer.trigger_events(event)

    @staticmethod
    def load_data() -> None:
        """Loads game data"""
        # config_check(CONFIG_PATH)

        # for file in walk_search("UiData"):
        #     ui_check(file, CONFIG_PATH)

        game_config = read_json(CONFIG_PATH)

        fonts_data = game_config.get("fonts_data")
        devtools_data = game_config.get("devtools_data")
        events_data = game_config.get("events_data")
        sounds_data = game_config.get("sounds_data")
        music_data = game_config.get("music_data")

        Text.load_fonts(fonts_data)
        Debugger.load_debugger_config(devtools_data)
        Eventer.load_global_events(events_data)
        Sound.load_sounds(sounds_data)
        Music.load_music(music_data)
