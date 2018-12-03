# this contains the game logic for Hex
import math

class Board:
    tile_array = None
    groups = []  # these are groups of pieces that are connected
    moves = []  # this is a array of moves that were played in the game
    
    def __init__(self, size):
        self.tile_array = [[Space()] * size] * size

    def white_move(self, x, y):
        self.tile_array[x][y].white_space()

    def black_move(self, x, y):
        self.tile_array[x][y].black_space()

    def expand_groups(self):
        return
        
    def calculate_win_condition(self):
        if (self.moves / 2) < len(self.tile_array):  # this uses less compute power
            return False

        # this will not return which team one since that is the player that currently moved
        for group in self.groups:
            if group[0].white and self.moves[len(self.moves) - 1].white:  # this is if both

            elif group[0].black and :
            return
        return

class Space:
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
      
class move:  # this is used for storage of the moves in the move array
    x = None
    y = None
    white = False
    black = False
    def __init__(self, x, y, white):
        self.x = x
        self.y = y
        if white:
            self.white = True
        else:
            self.black = True
    
