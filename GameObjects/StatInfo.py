class StatInfo(object):

    def __init__(self, total):
        self.steps = 0
        self.total_cells = total
        self.filled_cells = 0

    def add_filled_cells(self, filled):
        self.steps += 1
        self.filled_cells += filled
