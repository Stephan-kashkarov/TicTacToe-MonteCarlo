from random import randint
from pprint import pprint
from functions import check_win

class Player:

    def move(self, grid, char):
        # TODO: Make gui
        pass



class Bot:
    def __init__(self, weights=[[0 for x in range(3)] for x in range(3)]):
        self.weights = weights

    def move(self, grid, char, simulation=False):
        """
        Makes a calculated move based on weights
        and grid state

        @param grid: a 3x3 2d array
        @param char: the character used in move e.g. "X"
        """
        if not simulation:
            vals = []
            coords = []
            for index, row in enumerate(self.weights):
                for item in row:
                    if len(vals) == 0:
                        coords.append([index, row.index(item)])
                    else:
                        for i, val in enumerate(coords):
                            if val < item:
                                coords.insert(i, [index, row.index(item)])


            return grid
        else:
            return self.rand_move(grid, char)

    def gen_weights(self):
        pass

    def rand_move(self, grid, char):
        """
        Makes a random move

        @param grid: a 3x3 2d array
        @param char: the character used in move e.g. "O"
        """
        while True:
            move = [randint(0,2), randint(0,2)]
            if grid[move[0]][move[1]] == 0:
                grid[move[0]][move[1]] = char
                return grid


class Game:
    def __init__(self, player1, player2, simulation=False, grid=[[0 for x in range(3)] for x in range(3)]):
        self.simulation = simulation
        self.players = [(player1, "O"), (player2, "X")]
        self.grid = grid
        self.current_player = 0
        self.winner = None

    def run(self):
        exit_cond = False
        while not exit_cond:
            self.grid = self.players[self.current_player][0].move(self.grid, self.players[self.current_player][1])
            self.current_player = int(not self.current_player)
            winner, exit_cond = check_win(self.grid)
        if not self.simulation:
            print(f"And the winner is... {winner if winner else 'Oh its a tie'}")

    
