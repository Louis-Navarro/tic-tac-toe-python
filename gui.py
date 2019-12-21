import numpy as np
import pygame as pg
import verify

pg.init()

#############
# VARIABLES #
#############

# Window
win_side = 600
win = pg.display.set_mode((win_side, win_side))
pg.display.set_caption('Tic Tac Toe')

# Game
grid = np.full((3, 3), '-')
player = 'X'

# Text
font = pg.font.SysFont('sourcecodepro', 200)
font_winner = pg.font.SysFont('sourcecodepro', 50)

#############
# FUNCTIONS #
#############


def check_clicks():
    global player

    clicks = pg.mouse.get_pressed()

    if clicks[0]:
        x, y = pg.mouse.get_pos()

        row = y // 200
        col = x // 200

        if grid[row, col] == '-':
            grid[row, col] = player
            player = 'X' if player == 'O' else 'O'


def draw_window():
    win.fill((255, 255, 255))

    for i in range(1, 3):
        pg.draw.line(win, (0, 0, 0), (200 * i, 0), (200 * i, 600))
        pg.draw.line(win, (0, 0, 0), (0, 200 * i), (600, 200 * i))

    for row in range(3):
        for col in range(3):
            char = grid[row, col]
            if char != '-':
                if char == 'X':
                    text = font.render(char, True, (255, 0, 0))
                elif char == 'O':
                    text = font.render(char, True, (0, 0, 255))

                x = col * 200 + 40
                y = row * 200 - 35

                win.blit(text, (x, y))

    pg.display.flip()


def draw_won(winner):
    win.fill((255, 255, 255))

    if winner != 'Tie':
        text = font_winner.render(f'{winner} won', True, (0, 0, 0))
        win.blit(text, (225, 250))

    else:
        text = font_winner.render(f'No one won', True, (0, 0, 0))
        win.blit(text, (150, 250))

    pg.display.flip()


#############
# MAIN LOOP #
#############

clock = pg.time.Clock()
run = True
result = 0

while run:
    clock.tick(60)

    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False

    if not result:
        result = verify.verify(grid)

    if result == 1:
        draw_won('X')

    elif result == 2:
        draw_won('O')

    elif result == -1:
        draw_won('Tie')

    else:
        check_clicks()
        draw_window()
