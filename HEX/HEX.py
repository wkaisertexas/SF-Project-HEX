# this is the HEX File


class Board:
    tile_array = None
    groups = []  # these are groups of pieces that are connected

    def __init__(self, size):
        self.tile_array = [[Space()] * size] * size

    def white_move(self, x, y):
        return

    def black_move(self, x, y):
        return

    def calculate_win_condition(self):
        # this will not return which team one since that is the player that currently moved
        return

class Space:  # this should be a part of the game logic file, not the GUI file
    white = False
    black = False

    def __init__(self):
        return

    def white_space(self):
        self.white = True
        self.black = False

    def black_space(self):
        self.white = False
        self.black = True

    def blank_space(self):
        self.black = False
        self.white = False