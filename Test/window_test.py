"""Contains unitest for window file"""
###### Python Packges ######
import pytest

###### My Packges ######
from window import FrameRate, Reslution, Window


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
    attrs = {"size": [0, 0], "grid_div": 2, "fps": 60, "title": "Engine"}

    assert isinstance(Window(attrs), Window)


def test_window_bad_value():
    """Test window wrong value passed"""
    no_size = {"grid_div": 2, "fps": 60, "title": "Engine"}
    no_grid = {"size": [0, 0], "fps": 60, "title": "Engine"}
    no_fps = {"size": [0, 0], "grid_div": 2, "title": "Engine"}
    no_title = {"size": [0, 0], "grid_div": 2, "fps": 60}

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
    bad_size = {"size": 2.2, "grid_div": 2, "fps": 60, "title": "Engine"}
    bad_grid = {"size": [0, 0], "grid_div": 2.1, "fps": 60, "title": "Engine"}
    bad_fps = {"size": [0, 0], "grid_div": 2, "fps": 1.1, "title": "Engine"}
    bad_title = {"size": [0, 0], "grid_div": 2, "fps": 60, "title": 1}

    with pytest.raises(TypeError) as _:
        Window(bad_size)

    with pytest.raises(TypeError) as _:
        Window(bad_grid)

    with pytest.raises(TypeError) as _:
        Window(bad_fps)

    with pytest.raises(TypeError) as _:
        Window(bad_title)
