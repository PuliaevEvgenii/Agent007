from PyQt5 import QtGui
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget

from GameObjects.Cell import Cell
from GameObjects.Game import Game
from Windows.StatInfoWindow import StatInfoWindow
from Utils.CellState import CellState
from Utils.Direction import Direction
from Utils.Utils import click_on_rect


class GameWindow(QWidget):

    def __init__(self, game: Game):
        super().__init__()
        self.game = game
        self.cell_width = 50
        self.init_ui(game.field.n_width, game.field.n_height, self.cell_width)

    def init_ui(self, w, h, c):
        self.setGeometry(300, 300, c * w, c * h + 50)
        self.setWindowTitle('Agent 007')
        self.show()

    def paintEvent(self, e: QtGui.QPaintEvent):
        qp = QPainter()
        qp.begin(self)
        self.paint_field(qp)
        qp.end()

    def mousePressEvent(self, e: QtGui.QMouseEvent):

        cw = self.game.field.cells[0][0].width
        ch = self.game.field.cells[0][0].height

        px = self.game.player.x * cw
        py = self.game.player.y * ch

        player_dir = None

        if click_on_rect(px + cw, py, cw, ch, e.x(), e.y()):
            player_dir = Direction.right

        elif click_on_rect(px - cw, py, cw, ch, e.x(), e.y()):
            player_dir = Direction.left

        elif click_on_rect(px, py - ch, cw, ch, e.x(), e.y()):
            player_dir = Direction.top

        elif click_on_rect(px, py + ch, cw, ch, e.x(), e.y()):
            player_dir = Direction.bottom

        if player_dir is not None:
            if not self.game.next_move(player_dir):
                self.siw = StatInfoWindow(self.game.stats)
                self.close()
            self.update()

    def paint_field(self, qp: QPainter):
        field = self.game.field
        for i in range(field.n_height):
            for j in range(field.n_width):
                cell: Cell = field.cells[i][j]

                col = QColor(0, 0, 0)
                qp.setPen(col)

                col.setNamedColor(cell.state.value)
                qp.setBrush(col)

                r = QRect(j * cell.width, i * cell.height, cell.width, cell.height)

                qp.drawRect(r)

                if cell.state == CellState.free:
                    col = QColor(0, 0, 0)
                    qp.setPen(col)
                    qp.drawText(r, Qt.AlignCenter, str(cell.steps))

        statusbar = QRect(0, field.n_height * self.cell_width, field.n_width * self.cell_width, self.cell_width)
        stats = 'steps: ' + str(self.game.stats.steps) + \
                ', coloured: ' + str(self.game.stats.filled_cells) + ' / ' + str(self.game.stats.total_cells) + ' cells'
        qp.drawText(statusbar, Qt.AlignCenter, stats)
