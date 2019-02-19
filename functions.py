def check_win(grid):
    spaces = False
    # diagonal1
    if all(grid[x][x] == grid[1][1] for x in range(3)):
        return(grid[1][1], True)
    #diagonal2
    if all(grid[2-x][x] == grid[1][1] for x in range(2, -1, -1)):
        return(grid[1][1], True)

    # Rows
    for row in grid:
        if 0 in row:
            spaces = True
        if all(x == row[0] for x in row):
            if row[0] in ["O", "X"]:
                return row[0], True

    # Cols
    for x in range(3):
        col = [grid[y][x] for y in range(3)]
        if all(x == col[0] for x in col):
            if col[0] in ["O", "X"]:
                return col[0], True

    return None, False if spaces else True
