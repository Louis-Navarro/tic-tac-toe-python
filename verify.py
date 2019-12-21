def verify_x(grid):
    for row in range(3):
        if set(grid[row]) == {'X'}:
            return True

        elif set(grid.T[row]) == {'X'}:
            return True

    if grid[0, 0] == grid[1, 1] == grid[2, 2] == 'X':
        return True

    elif grid[0, 2] == grid[1, 1] == grid[2, 0] == 'X':
        return True


def verify_o(grid):
    for row in range(3):
        if set(grid[row]) == {'O'}:
            return True

        elif set(grid.T[row]) == {'O'}:
            return True

    if grid[0, 0] == grid[1, 1] == grid[2, 2] == 'O':
        return True

    elif grid[0, 2] == grid[1, 1] == grid[2, 0] == 'O':
        return True


def verify(grid):
    if verify_x(grid):
        return 1

    elif verify_o(grid):
        return 2

    else:
        if '-' in grid:
            return 0

        else:
            return -1
