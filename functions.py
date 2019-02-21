def check_win(grid):
    spaces = False
    # diagonal1
    if all([grid[x][x] == grid[1][1] for x in range(3)]):
        if grid[1][1] not in [".", 0]:
            return grid[1][1], True
    #diagonal2
    if all([grid[2-x][x] == grid[1][1] for x in range(2, -1, -1)]):
        if grid[1][1] not in [".", 0]:
            return grid[1][1], True

    # Rows
    for row in grid:
        if 0 in row or "." in row:
            spaces = True
        if all([x == row[0] for x in row]):
            if row[0] in ["O", "X"]:
                return row[0], True

    # Cols
    for x in range(3):
        col = [grid[y][x] for y in range(3)]
        if all([x == col[0] for x in col]):
            if col[0] in ["O", "X"]:
                return col[0], True

    return None, False if spaces else True

def score_game(grid, winner, win_const, loss_const, weights=[[0 for x in range(3)] for y in range(3)]):
    score = 0
    if winner == None:
        win_const = 1
        loss_const = 1
        winner = "X"
    for y, row in enumerate(grid):
        for x, point in enumerate(row):
            if point == winner:
                weights[y][x] += win_const
                score += win_const
            elif point == ("O" if winner == "O" else "X"):
                weights[y][x] += loss_const
                score += loss_const
    return weights, score


