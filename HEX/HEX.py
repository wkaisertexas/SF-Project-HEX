# this contains the game logic for Hex
import math
from array import *

class Board:
    tile_array = []
    white_groups = []  # groups are sets of contiguous moves
    black_groups = []
    moves = []  # this is a array of moves that were played in the game

    def __init__(self, size):  # this code is required to fix weird issues with editing arrays
        for y in range(size):
            row = []
            for x in range(size):
                row.append(Space())
            self.tile_array.append(row)

    def get_board_size(self):
        return len(self.tile_array), len(self.tile_array)

    def white_move(self, x, y):
        self.tile_array[x][y].white_space()
        self.moves.append(Move(x, y, True))

    def black_move(self, x, y):
        self.tile_array[x][y].black_space()
        self.moves.append(Move(x, y, False))

    def make_move(self, move):
        if move.white:
            self.tile_array[move.x][move.y].white_space()
        else:
            self.tile_array[move.x][move.y].black_space()
        self.moves.append(move)

    def expand_groups(self):  # I have no idea if this works
        # this looks at the latest move to check if it is connected to another group
        if self.moves[-1].white:
            connected_groups = []  # this is a list of groups that are connected to the piece that was played

            for group in self.white_groups:
                for move in group:
                    if self.check_bordering_moves(self.moves[-1], move):
                        connected_groups.append(group)
                        break

            # at this point we have a list of all of the groups

            # this removes the groups that are connected from the groups array
            for group in connected_groups:
                self.white_groups.remove(group)

            # this adds the combined, connected groups together and appends that to the global group array
            combined_connected_groups = []

            for group in connected_groups:
                combined_connected_groups += group

            combined_connected_groups.append(self.moves[-1])

            self.white_groups.append(combined_connected_groups)
        else:
            connected_groups = []  # this is a list of groups that are connected to the piece that was played

            for group in self.black_groups:
                for move in group:
                    if self.check_bordering_moves(self.moves[-1], move):
                        connected_groups.append(group)
                        break

            # at this point we have a list of all of the groups

            # this removes the groups that are connected from the groups array
            for group in connected_groups:
                self.black_groups.remove(group)

            # this adds the combined, connected groups together and appends that to the global group array
            combined_connected_groups = []

            for group in connected_groups:
                combined_connected_groups += group

            combined_connected_groups.append(self.moves[-1])

            self.black_groups.append(combined_connected_groups)

    def check_bordering_moves(self, move, bordering_move):
        x_boundaries = [0, 1, -1]
        y_mapping = {0: [-1, 1], 1: [-1, 0], -1: [0, 1]}

        for x_item in [x + bordering_move.x for x in x_boundaries]:
            if x_item == move.x:
                for y_item in [y + bordering_move.y for y in y_mapping[x_item - bordering_move.x]]:
                    if y_item == move.y:
                        return True
        return False

    def calculate_win_condition(self):
        self.expand_groups()

        # this will not return which team one since that is the player that currently moved
        if self.moves[-1].white:
            testing_groups = self.white_groups
        else:
            testing_groups = self.black_groups

        for group in testing_groups:
            first = False
            last = False
            for move in group:
                if self.moves[-1].white:
                    if move.y == 0:
                        first = True
                    elif move.y == (len(self.tile_array) - 1):
                        last = True
                else:
                    if move.x == 0:
                        first = True
                    elif move.x == (len(self.tile_array) - 1):
                        last = True
            if first and last:
                return True

        return False
    
    def to_savable_string(self):
        # this converts all of the moves into a savable string
        if self.calculate_win_condition():
            if self.moves[-1].white:
                return_string = "W:"
            else:
                return_string = "B:"
        else:
            return_string = "U:"

        for move in self.moves:
            return_string += move.to_savable_string() + ","

        return return_string

    def to_string(self):
        # this will convert the board into a string that can be displayed
        return_string = ""

        for x in range(len(self.tile_array)):
            return_string += " " * x
            for y in range(len(self.tile_array)):
                return_string += self.tile_array[y][x].to_string() + " "
            return_string += "\n"
        return return_string

    def get_legal_moves(self, color):  # this serves as an input to the the game
        legal_moves = []
        if color:
            # White
            # this board does not get flipped
            for x in range(len(self.tile_array)):
                for y in range(len(self.tile_array)):
                    if self.tile_array[x][y].check_blank_space():
                        legal_moves.append(Move(x, y, True))
        else:
            # Black
            # this board gets flipped in order to only have to use one neural network in order to play this game

            print("HI")
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

    def check_blank_space(self):
        return not (self.white or self.black)

    def to_string(self):
        if self.white:
            return "W"
        elif self.black:
            return "B"
        else:
            return "-"


class Move:  # this is used for storage of the moves in the move array\\\  this will also be used to calculate groups
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

    def to_string(self):
        if self.white:
            return "W:(" + str(self.x) + "," + str(self.y) + ")"
        else:
            return "B:(" + str(self.x) + "," + str(self.y) + ")"