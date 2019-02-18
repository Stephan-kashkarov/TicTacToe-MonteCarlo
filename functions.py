def check_win(grid):
        # diagonal1
        check = []
        for x in range(3):
            coord = grid[x][x]
            if coord not in check and coord in ["O, X"]:
                check.append(coord)
                if len(check) == 1:
                    return check[0], True
        #diagonal2
        check = []
        for x in range(2, -1, -1):
            y = 2 - x
            coord = grid[y][x]
            if coord not in check and coord in ["O, X"]:
                check.append(coord)
                if len(check) == 1:
                    return check[0], True

        # Rows
        for row in grid:
            if all(x == row[0] for x in row):
                if row[0] in ["O", "X"]:
                    return row[0], True

        # Cols
        for x in range(3):
            col = [grid[y][x] for y in range(3)]
            if all(x == col[0] for x in col):
                if col[0] in ["O", "X"]:
                    return col[0], True
        
        return None, False
