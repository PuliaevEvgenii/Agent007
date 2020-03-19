import sys

from PyQt5.QtWidgets import QApplication

from Game import Game
from GameField import GameField
from Player import Player
from Window import Window

if __name__ == '__main__':

    player = Player("player1", 10, 10)
    field = GameField(20, 20, 3, player)
    game = Game(player, field)

    app = QApplication(sys.argv)
    w = Window(game)
    sys.exit(app.exec_())
