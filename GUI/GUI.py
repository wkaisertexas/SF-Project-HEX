# this is the absolute GUI file for the HEX program
import turtle








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