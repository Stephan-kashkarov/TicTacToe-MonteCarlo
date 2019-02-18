def check_win(grid):
        # diagonal1
        check = []
        for x in range(3):
            coord = grid[x][x]
            if coord not in check:
                check.append(coord)
                if len(check) == 1:
                    return True
        #diagonal2
        check = []
        for x in range(2, -1, -1):
            y = 2 - x
            coord = grid[y][x]
            if coord not in check:
                check.append(coord)
                if len(check) == 1:
                    return True

        # Rows
        for row in grid:
            if all(x == row[0] for x in row):
                return True

        # Cols
        for x in range(3):
            col = [grid[y][x] for y in range(3)]
            if all(x == col[0] for x in col):
                return True
