from random import randint
from pprint import pprint
from functions import check_win

class Player:
    def __init__(self):
        self.print = "O"

    def move(self, grid):
        pass



class Bot:
    def __init__(self, weights={}):
        self.print = "X"
        self.weights = weights

    def move(self, grid):
        pass

    def rand_move(self):
        pass


class Game:
    def __init__(self, player1, player2, simulation=False, grid=[[0 for x in range(3)] for x in range(3)]):
        self.simulation = simulation
        self.players = [player1, player2]
        self.grid = grid
        self.current_player = 0
        self.winner = None

    def run(self):
        exit_cond = False
        while not exit_cond:
            self.players[self.current_player].move(self.grid)
            self.current_player = int(not self.current_player)
            winner, exit_cond = check_win(self.grid)
        if not self.simulation:
            print(f"And the winner is... {winner}")

    
