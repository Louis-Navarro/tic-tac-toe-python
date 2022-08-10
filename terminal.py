import numpy as np

from util import Verifier


class TerminalGame:
    def __init__(self):
        self.grid = np.full((3, 3), '-')
        self.player = 'X'
        self.run = True

    def start_game(self):
        while self.run:
            self.print_grid()

            row = col = None
            while (row, col) == (None, None):
                try:
                    print()
                    row = int(
                        input(f'Enter row for player {self.player} (1, 2 or 3): ')) - 1
                    col = int(
                        input(f'Enter column for player {self.player} (1, 2 or 3): ')) - 1

                    print()

                    if self.grid[row, col] != '-':
                        continue

                    self.grid[row, col] = self.player
                    self.player = 'X' if self.player == 'O' else 'O'

                    result = Verifier.verify_winner(self.grid)
                    if result in Verifier.WINNER_MAP:
                        if result != -1:
                            print(f'{Verifier.WINNER_MAP[result]} won!')
                        else:
                            print('It is a tie!')
                        self.run = False

                except Exception as e:
                    row = col = None
                    print('Error')

    def print_grid(self):
        for row in self.grid:
            for char in row:
                print(char, end=' ')

            print()


if __name__ == '__main__':
    game = TerminalGame()
    game.start_game()
