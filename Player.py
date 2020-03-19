from Cell import Cell
from Utils.CellState import CellState
from Utils.Direction import Direction
from GameField import GameField


def is_acceptable_move(cell: Cell):
    print(cell.state)
    return cell.state == CellState.free or cell.state == CellState.player


class Player(object):
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def make_move(self, direction: Direction, field: GameField):
        px = self.x
        py = self.y
        cells = field.cells

        if direction == Direction.top:
            steps = cells[px][py - 1].steps
            for i in range(py, py - steps, -1):
                if is_acceptable_move(cells[px][i]):
                    cells[px][i].state = CellState.visited
                else:
                    return False
            cells[px][py - steps].state = CellState.player
            self.y = py - steps

        elif direction == Direction.right:
            steps = cells[px + 1][py].steps
            for i in range(px, px + steps):
                if is_acceptable_move(cells[i][py]):
                    cells[i][py].state = CellState.visited
                else:
                    return False
            cells[px + steps][py].state = CellState.player
            self.x = px + steps

        elif direction == Direction.bottom:
            steps = cells[px][py + 1].steps
            for i in range(py, py + steps):
                if is_acceptable_move(cells[px][i]):
                    cells[px][i].state = CellState.visited
                else:
                    return False
            cells[px][py + steps].state = CellState.player
            self.y = py + steps

        elif direction == Direction.left:
            steps = cells[px - 1][py].steps
            for i in range(px, px - steps, -1):
                if is_acceptable_move(cells[i][py]):
                    cells[i][py].state = CellState.visited
                else:
                    return False
            cells[px - steps][py].state = CellState.player
            self.x = px - steps

        return True
