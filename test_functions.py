import unittest
import functions as fn

grid1 = [
    [0, "O", 0],
    [0, "O", 0],
    [0, "O", 0],
]
grid2 = [
    ["X", 0, 0],
    [0, "X", 0],
    [0, 0, "X"],
]
grid3 = [
    [0, 0, "X"],
    [0, "X", 0],
    ["X", 0, 0],
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
    ["O", "X", 0],
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
        self.assertEqual(result6, (None, True))
