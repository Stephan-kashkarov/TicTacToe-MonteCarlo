import pprint
from random import randint
from functions import check_win, score_game

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
        @param simulation: defines rand_move or regular move usage
        """
        if not simulation:
            vals = []
            coords = []
            self.gen_weights(10000, [[str(x) for x in row] for row in grid])
            coords = []
            for y, row in enumerate(self.weights):
                row = [(y, row.index(x), x) for x in row]
                coords.extend(sorted(row, key=lambda x: x[2]))
            coords = sorted(coords, key=lambda x: x[2])
            while coords:
                y, x, val = coords.pop()
                if grid[y][x] in [".", 0]:
                    grid[y][x] = char
                    break
                if len(coords) <= 0:
                    print("AI: No spaces")
            return grid
        else:
            return self.rand_move(grid, char)

    def gen_weights(self, games, grid=[[".", ".", "."] for x in range(3)]):
        print("Simulating")
        g = Game(self, self, True, grid)
        for i in range(games):
            grid, winner = g.run()
            self.weights = score_game(
                grid,
                winner,
                self.win_const,
                self.loss_const,
                self.weights
            )[0]
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
        self.grid_org = tuple(([str(y) for y in x] for x in self.grid)) # Why dosent List() work!!!!
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
        if not self.simulation:
            print(f"And the winner is... {winner if winner else 'Oh its a tie'}")
        return self.grid, winner

    def reset(self):
        self.grid = list([[str(y) for y in x] for x in self.grid_org]) # Why dosent List() work!!!!
        self.current_player = 0
        self.winner = None

    
if __name__ == "__main__":
    p = Player("John")
    a = Bot()
    game = Game(p, a, False, [["." for x in range(3)] for y in range(3)])
    game.reset()
    grid, winner = game.run()
    print("Thanks for playing")
