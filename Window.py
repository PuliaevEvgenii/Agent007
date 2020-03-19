from PyQt5 import QtGui
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget

from Cell import Cell
from Utils.CellState import CellState
from Utils.Direction import Direction
from Game import Game
from Utils.Utils import click_on_rect


class Window(QWidget):

    def __init__(self, game: Game):
        super().__init__()
        self.game = game
        self.init_ui(game.field.n_width, game.field.n_height, 50)

    def init_ui(self, w, h, c):
        self.setGeometry(300, 300, c * w, c * h)
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
            self.game.next_move(player_dir)
            self.update()

    def paint_field(self, qp: QPainter):
        field = self.game.field
        for i in range(field.n_width):
            for j in range(field.n_height):
                cell: Cell = field.cells[i][j]

                col = QColor(0, 0, 0)
                qp.setPen(col)

                col.setNamedColor(cell.state.value)
                qp.setBrush(col)

                r = QRect(i * cell.width, j * cell.height, cell.width, cell.height)

                qp.drawRect(r)

                if cell.state == CellState.free:
                    col = QColor(0, 0, 0)
                    qp.setPen(col)
                    qp.drawText(r, Qt.AlignCenter, str(cell.steps))
