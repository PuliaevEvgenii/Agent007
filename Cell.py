from Utils.CellState import CellState


class Cell(object):
    def __init__(self, steps, state: CellState, width, height):
        self.steps = steps
        self.state = state
        self.width = width
        self.height = height
