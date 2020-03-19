import random

from Utils.Direction import Direction


def fill_steps():
    return random.randint(1, 6)


def ask_move_direction():
    return Direction(int(input()))


def click_on_rect(x, y, w, h, ex, ey):
    if (x < ex < x + w) and (y < ey < y + h):
        return True
    else:
        return False
