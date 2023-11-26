"""Define a path handling moudle"""
from os.path import exists


def path_check(path, alt=""):
    """
    Check if the given path is vaild

    Arguments:
        alt: alternate path if the given path doesn't exists
    """
    if exists(path):
        return path
    if exists(alt):
        return alt
    raise FileNotFoundError(f"No such file or directory: {path}/{alt}")
