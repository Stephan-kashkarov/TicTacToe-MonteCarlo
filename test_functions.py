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

class TestFunctions(unittest.TestCase):       
    
    def test_check_win_col(self):
        result1 = fn.check_win(grid1)
        self.assertEquals(result1, ("O", True))
       
    def test_check_win_diag(self):
        result2 = fn.check_win(grid2)
        self.assertEquals(result2, ("X", True))


    def test_check_win_diag2(self):
        result3 = fn.check_win(grid3)
        self.assertEquals(result3, ("X", True))
    
    def test_check_win_row(self):
        result4 = fn.check_win(grid4)
        self.assertEquals(result4, ("O", True))

    def test_check_win_false(self):
        result5 = fn.check_win(grid5)
        self.assertEquals(result5, (None, False))
