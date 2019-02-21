import unittest
import functions as fn

grid1 = [
    [".", ".", "O"],
    [".", ".", "O"],
    [".", ".", "O"],
]
grid2 = [
    ["X", ".", "."],
    [".", "X", "."],
    [".", ".", "X"],
]
grid3 = [
    [".", ".", "X"],
    [".", "X", "."],
    ["X", ".", "."],
]
grid4 = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["O", "O", "O"],
]
grid5 = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["O", "X", "O"],
]
grid6 = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["O", "X", "."],
]


class TestFunctions(unittest.TestCase):       
    
    def test_check_win_col(self):
        result1 = fn.check_win(grid1)
        self.assertEqual(result1, ("O", True))
       
    def test_check_win_diag(self):
        result2 = fn.check_win(grid2)
        self.assertEqual(result2, ("X", True))

    def test_check_win_diag2(self):
        result3 = fn.check_win(grid3)
        self.assertEqual(result3, ("X", True))
    
    def test_check_win_row(self):
        result4 = fn.check_win(grid4)
        self.assertEqual(result4, ("O", True))

    def test_check_win_false(self):
        result5 = fn.check_win(grid5)
        self.assertEqual(result5, (None, True))

    def test_check_win_not_full(self):
        result6 = fn.check_win(grid6)
        self.assertEqual(result6, (None, False))

    def test_score_game_1(self):
        result = fn.score_game(grid1, "O", 2, 1)
        self.assertEqual(result[1], 6)
        self.assertEqual(result[0], [
            [0, 0, 2],
            [0, 0, 2],
            [0, 0, 2],
        ])
    
    def test_score_game_2(self):
        result = fn.score_game(grid2, "X", 1, 1)
        self.assertEqual(result[1], 3)
    
    def test_score_game_3(self):
        result = fn.score_game(grid3, "X", 3, 1)
        self.assertEqual(result[1], 9)

    def test_score_game_4(self):
        result = fn.score_game(grid4, "O", 2, 1)
        self.assertEqual(result[1], 12)
    
    def test_score_game_5(self):
        result = fn.score_game(grid5, "O", 3, 1)
        self.assertEqual(result[1], 15)
    
    def test_score_game_6(self):
        result = fn.score_game(grid5, "X", 2, 1)
        self.assertEqual(result[1], 8)
