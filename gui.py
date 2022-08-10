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
import pygame as pg
from util import Verifier

pg.init()


class GuiGame:
    WIN_SIDE = 600

    def __init__(self):
        self.grid = np.full((3, 3), '-')
        self.player = 'X'

        self.win = pg.display.set_mode((self.WIN_SIDE, self.WIN_SIDE))
        pg.display.set_caption('Tic Tac Toe')

        self.font = pg.font.SysFont('sourceccodepro', 200)
        self.font_winner = pg.font.SysFont('sourceccodepro', 50)

        self.result = 0
        self.run = True
        self.clock = pg.time.Clock()

    def start_game(self):
        while self.run:
            self.clock.tick(60)

            self.check_events()

            if not self.result:
                self.game_tick()

            elif self.result in Verifier.WINNER_MAP:
                self.game_won()

            else:
                print('idk why this is happening')

    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.run = False
            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_ESCAPE:
                    self.result = 0
                    self.grid = np.full((3, 3), '-')
                    self.player = 'X'

    def game_tick(self):
        self.result = Verifier.verify_winner(self.grid)

        self.check_mouse_clicks()
        self.draw_window()

    def check_mouse_clicks(self):
        clicks = pg.mouse.get_pressed()

        if clicks[0]:
            x, y = pg.mouse.get_pos()

            row = y // (self.WIN_SIDE//3)
            col = x // (self.WIN_SIDE//3)

            if self.grid[row, col] == '-':
                self.grid[row, col] = self.player
                self.player = 'X' if self.player == 'O' else 'O'

    def draw_window(self):
        self.win.fill((255, 255, 255))

        for i in range(1, 3):
            pg.draw.line(self.win, (0, 0, 0), (self.WIN_SIDE//3 *
                         i, 0), (self.WIN_SIDE//3 * i, self.WIN_SIDE))
            pg.draw.line(self.win, (0, 0, 0), (0, self.WIN_SIDE //
                         3 * i), (self.WIN_SIDE, self.WIN_SIDE//3 * i))

        for row in range(3):
            for col in range(3):
                char = self.grid[row, col]
                if char != '-':
                    if char == 'X':
                        text = self.font.render(char, True, (255, 0, 0))
                    elif char == 'O':
                        text = self.font.render(char, True, (0, 0, 255))

                    x = col * 200 + 55
                    y = row * 200 + 40

                    self.win.blit(text, (x, y))

        pg.display.flip()

    def game_won(self):
        self.win.fill((255, 255, 255))

        if self.result != -1:  # Not a tie
            text = self.font_winner.render(
                f'{Verifier.WINNER_MAP[self.result]} won!', True, (0, 0, 0))
            self.win.blit(text, (250, 250))

        else:
            text = self.font_winner.render(f'It is a tie!', True, (0, 0, 0))
            self.win.blit(text, (225, 250))

        pg.display.flip()


if __name__ == '__main__':
    game = GuiGame()
    game.start_game()
