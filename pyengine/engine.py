"""Project start point"""
# pylint: disable=E1101
# pylint: disable=W0511
###### Python Packages ######
import sys
import pygame

###### My Packages ######
from pyengine import win_obj, CONFIG_PATH
from pyengine.libs.mixer import Sound, Music

from pyengine.libs.eventer.eventer import Eventer

from pyengine.libs.designer.designer import Designer
from pyengine.libs.designer.py_attributes import Text

from pyengine.libs.devtools.devtools import DevTools
from pyengine.libs.devtools.debug_tools import Debugger


from pyengine.utils.json_handler import read_json
from pyengine.utils.collision_handler import object_collision
from pyengine.utils.path_handler import walk_search

# from pyengine.utils.errors_handler.data_checker import config_check, ui_check
#### Type Hinting ####


class PyEngine:
    """Main class that works as a connector for all packages"""

    none_events = []

    @staticmethod
    def run(debug: bool = False):
        """
        Run the app

        Arguments:
            debug: Display debugging tools
        """
        PyEngine.load_data()
        PyEngine.mainloop(debug)

    @staticmethod
    def mainloop(debug: bool) -> None:
        """
        game mainloop

        Arguments:
            debug: Display debugging tools
        """
        while True:
            PyEngine.check_events(debug)

            for global_event in PyEngine.none_events:
                function = global_event[0]
                event_type = global_event[1].get("event")
                args = global_event[1].get("args").copy()

                if event_type == "rectin":
                    rect_1 = args.pop(0).rect
                    rect_2 = args.pop(0).rect
                    if object_collision(rect_1, rect_2):
                        function(*args)
                else:
                    function(*args)

            Designer.draw_groups()
            if debug:
                DevTools.display_tools()

            pygame.display.update()
            win_obj.clock.tick(win_obj.fps)

    @staticmethod
    def check_events(debug: bool) -> None:
        """
        Check all game events

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
        # TODO: Fix the data check and add it here before loading the data
        # config_check(CONFIG_PATH)

        # for file in walk_search("UiData"):
        #     ui_check(file, CONFIG_PATH)

        game_config = read_json(CONFIG_PATH)

        fonts_data = game_config.get("fonts_data")
        devtools_data = game_config.get("devtools_data")
        events_data = game_config.get("events_data")
        sounds_data = game_config.get("sounds_data")
        music_data = game_config.get("music_data")
        groups_data = game_config.get("groups_data")
        default_data = game_config.get("default_data")
        path_data = game_config.get("path_data")

        Text.load_fonts(fonts_data)
        Debugger.load_debugger_config(devtools_data)
        Sound.load_sounds(sounds_data)

        Music.load_music(music_data)
        if default_data.get("default_music"):
            Music.play_music(default_data.get("default_music"))

        for file in walk_search(path_data.get("ui_data_path")):
            Designer.create_from_file(file)

        for group, value in groups_data.items():
            Designer.exclude_groups[group] = value

        PyEngine.none_events = Eventer.load_global_events(
            events_data, Designer.get_element
        )
