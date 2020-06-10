from PyQt5.QtCore import QCoreApplication, Qt, pyqtSlot
from PyQt5.QtWidgets import QPushButton, QDesktopWidget, QLabel, QGridLayout, QSlider
from PyQt5.QtWidgets import QWidget

from GameObjects.Game import Game
from GameObjects.GameField import GameField
from Windows.GameWindow import GameWindow
from GameObjects.Player import Player
from GameObjects.StatInfo import StatInfo


class StartSettingsWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.width = 15
        self.height = 15
        self.bombs = 3
        self.init_ui()

    def init_ui(self):
        w_l = QLabel('Width')
        h_l = QLabel('Height')
        b_l = QLabel('Bombs')

        self.w_num = QLabel(str(self.width))
        self.h_num = QLabel(str(self.height))
        self.b_num = QLabel(str(self.bombs))

        w_sld = QSlider(Qt.Horizontal, self)
        w_sld.valueChanged[int].connect(self.change_w_value)
        w_sld.setMinimum(10)
        w_sld.setMaximum(50)

        h_sld = QSlider(Qt.Horizontal, self)
        h_sld.valueChanged[int].connect(self.change_h_value)
        h_sld.setMinimum(10)
        h_sld.setMaximum(50)

        b_sld = QSlider(Qt.Horizontal, self)
        b_sld.valueChanged[int].connect(self.change_b_value)
        b_sld.setMinimum(3)
        b_sld.setMaximum(20)

        start_btn = QPushButton('Start', self)
        start_btn.setToolTip('Start new game')
        start_btn.clicked.connect(self.start_game)

        quit_btn = QPushButton('Quit', self)
        quit_btn.setToolTip('Quit from game')
        quit_btn.clicked.connect(QCoreApplication.instance().quit)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(w_l, 1, 0)
        grid.addWidget(w_sld, 1, 1)
        grid.addWidget(self.w_num, 1, 2)

        grid.addWidget(h_l, 2, 0)
        grid.addWidget(h_sld, 2, 1)
        grid.addWidget(self.h_num, 2, 2)

        grid.addWidget(b_l, 3, 0)
        grid.addWidget(b_sld, 3, 1)
        grid.addWidget(self.b_num, 3, 2)

        grid.addWidget(start_btn, 4, 0)
        grid.addWidget(quit_btn, 4, 1)

        self.setLayout(grid)
        self.center()
        self.setWindowTitle('Agent 007')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def change_w_value(self, value):
        self.width = value
        self.w_num.setText(str(self.width))

    def change_h_value(self, value):
        self.height = value
        self.h_num.setText(str(self.height))

    def change_b_value(self, value):
        self.bombs = value
        self.b_num.setText(str(self.bombs))

    @pyqtSlot()
    def start_game(self):
        player = Player("player1", int(self.width / 2), int(self.height / 2))
        field = GameField(self.width, self.height, self.bombs, player)
        game = Game(player, field, StatInfo(self.width * self.height))
        self.gw = GameWindow(game)
