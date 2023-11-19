"""Define a collision handling moudle"""
from pygame.mouse import get_pos as mouse_pos


def mouse_collision(rect):
    """
    Check there is a collision between mouse and rect

    Arguments:
        rect: givent rect to check collision
    """
    if rect.collidepoint(mouse_pos()):
        return True
    return False
