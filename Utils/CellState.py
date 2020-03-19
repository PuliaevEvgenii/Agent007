from enum import Enum


class CellState(Enum):
    bomb = "#ff0000"
    player = "#000000"
    free = "#ffffff"
    visited = "#29d929"
