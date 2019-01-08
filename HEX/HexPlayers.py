import numpy as np

def play_human_player(legal_moves):
    for move in legal_moves:
        print(str(move.x) + ' ' + str(move.y))
    while True:
        a = input()

        x, y = [int(x) for x in a.split(' ')]
        for move in legal_moves:
            if x == move.x and y == move.y:
                return move


def random_player(legal_moves, size):
    while True:
        randX = np.random.randint(0, size - 1)
        randY = np.random.randint(0, size - 1)
        for move in legal_moves:
            if randX == move.x and randY == move.y:
                return move

def greedy_player(legal_moves, size)
        candidates = []
        for a in range(size):






