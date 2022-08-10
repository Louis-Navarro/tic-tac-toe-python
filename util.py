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
import typing


class Verifier:
    WINNER_MAP = {
        1: 'X',
        2: 'O',
        -1: 'Tie'
    }

    def __init__(self, grid: np.ndarray):
        self.grid = grid

    def _verify(self):
        if self._verify_symbol('X'):
            return 1  # X wins

        elif self._verify_symbol('O'):
            return 2  # O wins

        elif (self.grid == '-').sum() == 0:  # If the grid is full
            return -1  # Tie

        return 0  # Game not over

    def _verify_symbol(self, symbol: str):
        if ((self.grid == symbol).sum(axis=0) == 3).any():
            return True

        elif ((self.grid.T == symbol).sum(axis=0) == 3).any():
            return True

        elif ((self.grid.diagonal() == symbol).sum() == 3):
            return True

        elif ((np.fliplr(self.grid).diagonal() == symbol).sum() == 3):
            return True

        return False

    @staticmethod
    def verify_winner(grid: np.ndarray):
        verifier = Verifier(grid)
        return verifier._verify()
