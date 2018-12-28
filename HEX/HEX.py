# this contains the game logic for Hex
import math


class Board:
    tile_array = None
    white_groups = []  # groups are sets of contiguous moves
    black_groups = []
    moves = []  # this is a array of moves that were played in the game

    def __init__(self, size):
        self.tile_array = [[Space()] * size] * size

    def white_move(self, x, y):
        self.tile_array[x][y].white_space()
        self.moves.append[Move(x, y, True)]

    def black_move(self, x, y):
        self.tile_array[x][y].black_space()
        self.moves.append[Move(x, y, False)]

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
            print(x_item)
            if x_item == move.x:
                for y_item in [y + bordering_move.y for y in y_mapping[x_item - bordering_move.x]]:
                    print("Y:" + str(y_item))
                    if y_item == move.y:
                        return True
        return False

    def calculate_win_condition(self):
        # this will not return which team one since that is the player that currently moved
        if self.moves[-1].white:
            testing_groups = self.white_groups
        else:
            testing_groups = self.black_groups

        for group in testing_groups:
            for move in group:
                if self.moves[-1].white:
                    if move.y == 0:
                        first = True
                    elif move.y == len(self.tile_array):
                        last = True
                else:
                    if move.x == 0:
                        first = True
                    elif move.x == len(self.tile_array):
                        last = True
            if first and last:
                return True

        return False
    
    def to_string(self):
        if self.calculate_win_condition():
            if self.moves[-1].white:
                return_string = "W:"
            else:
                return_string = "B:"
        else:
            return_string = "U:"

        for move in self.moves:
            return_string += move.to_string() + ","

        return return_string

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


'''
    This of things tested:
        check_bordering_moves()

'''

# start of test code

# this tests the check_bordering_moves function
'''
# this creates the moves
move1 = Move(3, 0, True)
move2 = Move(4, 1, True)

# this checks if they register correctly
test_board = Board(11)

print(test_board.check_bordering_moves(move1, move2))
'''

