import random

from GameObjects.Cell import Cell
from Utils.CellState import CellState
from Utils.Utils import fill_steps


class GameField(object):

    def __init__(self, n_width, n_height, n_bombs, player):
        self.n_width = n_width
        self.n_height = n_height
        self.n_bombs = n_bombs
        self.cells = self._create_cells(player)

    def _create_cells(self, player):
        cells = self._init_cells()
        self._put_player(cells, player)
        self._put_bombs(cells)
        return cells

    def _init_cells(self):
        cells = [[Cell(fill_steps(), CellState.free, 50, 50) for i in range(self.n_width)] for j in range(self.n_height)]
        return cells

    def _put_bombs(self, cells):
        nb = self.n_bombs
        while nb > 0:
            m, n = self.__get_random_free_cell(cells)
            cells[m][n].state = CellState.bomb
            nb -= 1

    def _put_player(self, cells, player):
        cells[player.y][player.x].state = CellState.player

    def __get_random_free_cell(self, cells):
        while True:
            m = random.randint(0, self.n_height - 1)
            n = random.randint(0, self.n_width - 1)
            if cells[m][n].state == CellState.free:
                break
        return m, n

    @property
    def width(self):
        return self.n_width * self.cells[0][0].width

    @property
    def height(self):
        return self.n_height * self.cells[0][0].height
