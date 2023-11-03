"""Contains unitest for window file"""
###### Python Packges ######

###### My Packges ######
from window import FrameRate, Reslution


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
    res_obj = Reslution(None, 2)
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
    res_obj = Reslution(None, 4)
    assert res_obj.x_ceil == 4 * 9
    assert res_obj.y_ceil == 4 * 16
