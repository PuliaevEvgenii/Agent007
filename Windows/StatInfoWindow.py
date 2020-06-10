from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout

from GameObjects.StatInfo import StatInfo


class StatInfoWindow(QWidget):

    def __init__(self, stats: StatInfo):
        super().__init__()
        self.stats = stats
        self.init_ui()

    def init_ui(self):
        label = QLabel()
        if self.stats.filled_cells == self.stats.total_cells:
            label.setText('Winner')
        else:
            label.setText('Looser')

        grid = QGridLayout()
        grid.setSpacing(20)

        grid.addWidget(label, 1, 0, 1, 1)

        grid.addWidget(QLabel('Filled cells: '), 2, 0)
        grid.addWidget(QLabel(str(self.stats.filled_cells)), 2, 1)

        grid.addWidget(QLabel('Total cells: '), 3, 0)
        grid.addWidget(QLabel(str(self.stats.total_cells)), 3, 1)

        grid.addWidget(QLabel('Steps: '), 4, 0)
        grid.addWidget(QLabel(str(self.stats.steps)), 4, 1)

        self.setLayout(grid)
        self.setWindowTitle('Game Over')
        self.show()
