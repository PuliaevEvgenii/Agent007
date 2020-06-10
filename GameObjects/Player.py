from GameObjects.Cell import Cell
from Utils.CellState import CellState
from Utils.Direction import Direction
from GameObjects.GameField import GameField


def is_acceptable_move(field: GameField, x, y):
    if 0 <= x < field.n_width and 0 <= y < field.n_height:
        cell: Cell = field.cells[y][x]
        return cell.state == CellState.free or cell.state == CellState.player
    return False


class Player(object):

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def make_move(self, direction: Direction, field: GameField):
        px = self.x
        py = self.y
        cells = field.cells
        steps = 0

        cells[py][px].state = CellState.visited

        if direction == Direction.top:
            steps = cells[py - 1][px].steps
            for i in range(py - 1, py - steps - 1, -1):
                if is_acceptable_move(field, px, i):
                    cells[i][px].state = CellState.visited
                else:
                    return False, i
            cells[py - steps][px].state = CellState.player
            self.y = py - steps

        elif direction == Direction.right:
            steps = cells[py][px + 1].steps
            for i in range(px + 1, px + steps + 1):
                if is_acceptable_move(field, i, py):
                    cells[py][i].state = CellState.visited
                else:
                    return False, i
            cells[py][px + steps].state = CellState.player
            self.x = px + steps

        elif direction == Direction.bottom:
            steps = cells[py + 1][px].steps
            for i in range(py + 1, py + steps + 1):
                if is_acceptable_move(field, px, i):
                    cells[i][px].state = CellState.visited
                else:
                    return False, i
            cells[py + steps][px].state = CellState.player
            self.y = py + steps

        elif direction == Direction.left:
            steps = cells[py][px - 1].steps
            for i in range(px - 1, px - steps - 1, -1):
                if is_acceptable_move(field, i, py):
                    cells[py][i].state = CellState.visited
                else:
                    return False, i
            cells[py][px - steps].state = CellState.player
            self.x = px - steps

        return True, steps
