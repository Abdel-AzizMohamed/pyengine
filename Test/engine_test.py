###### Python Packges ######
import pytest

###### My Packges ######
from window import Window
from engine import PyEngine


def test_engine_init():
    eng_obj = PyEngine()
    assert type(eng_obj.window) == Window
