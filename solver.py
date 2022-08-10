# Copyright (C) 2022 Louis-Navarro
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import numpy as np
from util import Verifier


class Solver:
    def __init__(self, grid: np.ndarray):
        self.grid = grid

    def solve(self, player: str):
        """Main function, used to solve any grid given in the constructor
        Uses the min-max algorithm to find the best moves for the current player

        Args:
            player (str): current player playing

        Returns:
            tuple: Tuple containing the score (winning, losing or draw) and the location of the best play
        """
        max_score = -float('inf')
        max_pair = ()
        required_moves = 0
        for row in range(3):
            for col in range(3):
                if self.grid[row, col] == '-':
                    self.grid[row, col] = player
                    res = self.check_win(self.grid, player)
                    if res is not None:
                        # Finished game
                        if res > max_score:
                            max_score = res
                            max_pair = (row, col)
                            required_moves = 0

                    else:
                        next_move = self.solve(self._change_player(player))
                        if -next_move[0] > max_score:
                            max_score = -next_move[0]
                            max_pair = (row, col)
                            required_moves = next_move[2]
                        elif -next_move[0] == max_score and next_move[2] < required_moves:
                            max_pair = (row, col)
                            required_moves = next_move[2]

                    self.grid[row, col] = '-'

        return max_score, max_pair, required_moves+1

    def _change_player(self, player: str):
        return 'X' if player == 'O' else 'O'

    def check_win(self, grid: np.ndarray, player: str):
        """Checks if the current player won with the given grid

        Args:
            grid (np.ndarray): the current game grid
            player (str): the player that is playing

        Returns:
            int: Returns 0 if the game is not over, 1 if it is a tie, 2 if the player won, -1 if the player lost
        """
        result = Verifier.verify_winner(grid)
        if result == 0:
            return None
        if Verifier.WINNER_MAP[result] == player:
            return 1
        if Verifier.WINNER_MAP[result] == 'Tie':
            return 0
        return -1


if __name__ == '__main__':
    init_grid = np.array([
        ['X', 'O', 'X'],
        ['-', '-', '-'],
        ['-', '-', 'O'],
    ])
    solver = Solver(init_grid)
    print(solver.solve('X'))
