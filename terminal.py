import numpy as np

import verify
import algorithm


def print_grid(grid):
    for row in grid:
        for char in row:
            print(char, end=' ')

        print()


def main(grid):
    player = 'X'

    while True:
        print_grid(grid)

        row = int(input(f'Enter row for player {player} (1-2-3): ')) - 1
        col = int(input(f'Enter column for player {player} (1-2-3): ')) - 1

        if grid[row, col] != '-':
            continue

        grid[row, col] = player
        player = 'X' if player == 'O' else 'O'

        print(verify.verify(grid))


if __name__ == '__main__':
    grid = np.full((3, 3), '-')
    main(grid)
