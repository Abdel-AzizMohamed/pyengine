"""Contains unitest for window file"""
###### Python Packges ######
import pytest

###### My Packges ######
from Engine.window import FrameRate, Reslution, Window
from Engine.Libs.json_handler import read_json


element_print = read_json("defualt_config.json")


def test_framerate_init():
    """Test framerate init"""
    frame_obj = FrameRate(60)
    assert frame_obj.fps == 60
    assert frame_obj.delta_time is None
    # assert frame_obj.previous_time == time.time()


def test_framerate_set_delta():
    """Test framerate set_delta method"""
    frame_obj = FrameRate(60)
    frame_obj.set_delta()
    assert frame_obj.delta_time is not None


def test_reslution_init():
    """Test reslution init"""
    res_obj = Reslution([0, 0], 2)
    assert res_obj.screen_width == 1366
    assert res_obj.screen_height == 768
    assert res_obj.width_ratio == res_obj.screen_width / 1920
    assert res_obj.height_ratio == res_obj.screen_height / 1080
    assert res_obj.x_ceil == 2 * 9
    assert res_obj.y_ceil == 2 * 16


def test_reslution_set_reslution():
    """Test reslution set_reslution method"""
    res_obj = Reslution((500, 500), 2)
    assert res_obj.screen_width == 500
    assert res_obj.screen_height == 500


def test_reslution_set_grid():
    """Test reslution set_grid method"""
    res_obj = Reslution([0, 0], 4)
    assert res_obj.x_ceil == 4 * 9
    assert res_obj.y_ceil == 4 * 16


def test_window_init():
    """Test window wrong value passed"""
    assert isinstance(Window(element_print.get("window")), Window)


def test_window_bad_value():
    """Test window wrong value passed"""
    no_size = element_print.get("window").copy()
    del no_size["size"]

    no_grid = element_print.get("window").copy()
    del no_grid["grid_div"]

    no_fps = element_print.get("window").copy()
    del no_fps["fps"]

    no_title = element_print.get("window").copy()
    del no_title["title"]

    with pytest.raises(ValueError) as _:
        Window(no_size)
    with pytest.raises(ValueError) as _:
        Window(no_grid)
    with pytest.raises(ValueError) as _:
        Window(no_fps)
    with pytest.raises(ValueError) as _:
        Window(no_title)


def test_window_bad_type():
    """Test window wrong value passed"""
    bad_size = element_print.get("window").copy()
    bad_size["size"] = 2.2

    bad_grid = element_print.get("window").copy()
    bad_grid["grid_div"] = 2.1

    bad_fps = element_print.get("window").copy()
    bad_fps["fps"] = 1.1

    bad_title = element_print.get("window").copy()
    bad_title["title"] = 1

    with pytest.raises(TypeError) as _:
        Window(bad_size)

    with pytest.raises(TypeError) as _:
        Window(bad_grid)

    with pytest.raises(TypeError) as _:
        Window(bad_fps)

    with pytest.raises(TypeError) as _:
        Window(bad_title)
