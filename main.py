import pprint
from random import randint
from functions import check_win, score_game
from timeit import default_timer as timer

class Player:
    def __init__(self, name):
        self.name = name

    def move(self, grid, char, *args):
        x = None
        y = None
        for row in grid:
            print(f"{row[0]} {row[1]} {row[2]}")
        print(f"You are playing with \"{char}\"")

        while True:
            while not (x and y):
                try:
                    x, y = [int(z) for z in input("Your turn format(x y): ").split(" ")]
                except:
                    x, y = None, None
                    print("\nInvalid input!")
                    print("Try using coordinates and entering them sepatrated with spaces.")
                if x in range(3) and y in range(3):
                    break
            if not grid[y][x] != ".":
                break
            else:
                x = None
                y = None
                print("Move already taken!")
        grid[y][x] = char
        for row in grid:
            print(f"{row[0]} {row[1]} {row[2]}")
        return grid



class Bot:
    def __init__(self, weights=[[0 for x in range(3)] for x in range(3)]):
        self.weights = weights
        self.loss_const = 1
        self.win_const = 2

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
                    if len(vals) == ".":
                        coords.append([index, row.index(item)])
                    else:
                        for i, val in enumerate(coords):
                            if val < item:
                                coords.insert(i, [index, row.index(item)])
            for move in coords:
                if grid[move[0]][move[1]] == ".":
                    print("AI: moving")
                    for row in grid:
                        print(f"{row[0]} {row[1]} {row[2]}")
                    print("-" * 5)
                    grid[move[0]][move[1]] = char
                    for row in grid:
                        print(f"{row[0]} {row[1]} {row[2]}")
                    print("AI: move complete")
                    return grid

            print("[AI-S: No empty moves!]")
            return grid
        else:
            return self.rand_move(grid, char)

    def gen_weights(self, games):
        g = Game(self, self, True)
        c = 0
        for i in range(games):
            grid, winner = g.run()
            self.weights = score_game(
                grid,
                winner,
                self.win_const,
                self.loss_const,
                self.weights
            )[0]
            print(f"Sim game {c} complete")
            c += 1
            g.reset()

    def rand_move(self, grid, char):
        """
        Makes a random move

        @param grid: a 3x3 2d array
        @param char: the character used in move e.g. "O"
        """
        while True:
            move = [randint(0,2), randint(0,2)]
            if grid[move[0]][move[1]] == ".":
                grid[move[0]][move[1]] = char
                return grid


class Game:
    def __init__(self, player1, player2, simulation, grid=[["." for x in range(3)] for y in range(3)]):
        self.simulation = simulation
        self.players = [(player1, "O"), (player2, "X")]
        self.grid = list(grid)
        self.grid_org = list(grid)
        self.current_player = 0
        self.winner = None

    def run(self):
        exit_cond = False
        while not exit_cond:
            player, char = self.players[self.current_player]
            self.grid = player.move(
                self.grid,
                char,
                self.simulation,
            )
            self.current_player = int(not self.current_player)
            winner, exit_cond = check_win(self.grid)
            print(exit_cond)
        if not self.simulation:
            print(f"And the winner is... {winner if winner else 'Oh its a tie'}")
        return self.grid, winner

    def reset(self):
        print(self.grid)
        self.grid = list(self.grid_org)
        print(self.grid)
        self.current_player = 0
        self.winner = None

    
if __name__ == "__main__":
    p = Player("John")
    a = Bot()
    a.gen_weights(100)
    pprint.pprint(a.weights)
    game = Game(p, a, False)
    game.reset()
    grid, winner = game.run()
    print(score_game(grid, winner, 3, 1))




