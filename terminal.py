import numpy as np
import verify
import os
from colorama import init, Fore

init()
RED = Fore.RED
BLUE = Fore.BLUE
RESET = Fore.RESET


def print_grid(grid):
    for row in range(3):
        for col in range(3):
            char = grid[row, col]

            if char == 'X':
                print(RED, char, end=' ')
            elif char == 'O':
                print(BLUE, char, end='')
            else:
                print(RESET, char, end='')

        print(RESET)


def main():
    grid = np.full((3, 3), '-')
    player = 'X'

    while not verify.verify(grid):
        os.system('clear')

        print_grid(grid)

        if player == 'X':
            print(f'Player : {RED}X')
        else:
            print(f'Player : {BLUE}O')

        print(RESET, end='')

        row = int(input('Enter the row you want to change : ')) - 1
        col = int(input('Enter the column you want to change : ')) - 1

        if grid[row, col] == '-':
            grid[row, col] = player

            player = 'X' if player == 'O' else 'O'


if __name__ == "__main__":
    main()
