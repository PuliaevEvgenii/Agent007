from GameObjects.GameField import GameField
from GameObjects.Player import Player
from GameObjects.StatInfo import StatInfo


class Game(object):

    def __init__(self, player: Player, field: GameField, stats: StatInfo):
        self.player = player
        self.field = field
        self.stats = stats
        self.in_progress = True

    def next_move(self, player_dir):
        if self.in_progress:
            self.in_progress, filled = self.player.make_move(player_dir, self.field)
            self.stats.add_filled_cells(filled)
        return self.in_progress
