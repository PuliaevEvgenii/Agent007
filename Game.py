class Game(object):
    def __init__(self, player, field):
        self.player = player
        self.field = field
        self.in_progress = True

    def next_move(self, player_dir):
        if self.in_progress:
            self.in_progress = self.player.make_move(player_dir, self.field)

        return self.in_progress
