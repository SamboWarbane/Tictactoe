import numpy as np
import pygame
import sys

width = 600
height = 600
line_width = 15
no_rows = 3
no_columns = 3
square_size = 200
circle_radius = 60
circle_width = 15
cross_width = 25
space = 55

bg_color = pygame.Color("#ed6767")
line_color = pygame.Color("#793f5c")
circle_color = pygame.Color("#f2f2e6")
cross_color = pygame.Color("#292939")

pygame.init()
screen = pygame.display.set_mode((width, height))
screen.fill(bg_color)

board = np.zeros((no_rows, no_columns))


def draw_lines():
    pygame.draw.line(screen, line_color, (0, square_size), (width, square_size), line_width)
    pygame.draw.line(screen, line_color, (0, 2 * square_size), (width, 2 * square_size), line_width)
    pygame.draw.line(screen, line_color, (square_size, 0), (square_size, height), line_width)
    pygame.draw.line(screen, line_color, (2 * square_size, 0), (2 * square_size, height), line_width)


def draw_figures():
    for row in range(no_rows):
        for col in range(no_columns):
            if board[row][col] == 1:
                pygame.draw.circle(screen, circle_color, (int(col * square_size + square_size // 2),
                                                          int(row * square_size + square_size // 2)),
                                   circle_radius, circle_width)
            elif board[row][col] == 2:
                pygame.draw.line(screen, cross_color, (col * square_size + space,
                                                       row * square_size + square_size - space),
                                 (col * square_size + square_size - space, row * square_size + space), cross_width)
                pygame.draw.line(screen, cross_color, (col * square_size + space, row * square_size + space),
                                 (col * square_size + square_size - space, row * square_size + square_size - space),
                                 cross_width)


def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    return board[row][col] == 0


def is_board_full():
    for row in range(no_rows):
        for col in range(no_columns):
            if board[row][col] == 0:
                return False
    return True


def check_win(player):
    for col in range(no_columns):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True
    for row in range(no_rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True
    return False


def draw_vertical_winning_line(col, player):
    posx = col * square_size + square_size // 2
    if player == 1:
        color = circle_color
    else:
        color = cross_color

    pygame.draw.line(screen, color, (posx, 15), (posx, height - 15), line_width)


def draw_horizontal_winning_line(row, player):
    posy = row * square_size + square_size // 2
    if player == 1:
        color = circle_color
    else:
        color = cross_color

    pygame.draw.line(screen, color, (15, posy), (width - 15, posy), line_width)


def draw_asc_diagonal(player):
    if player == 1:
        color = circle_color
    else:
        color = cross_color

    pygame.draw.line(screen, color, (15, height - 15), (width - 15, 15), line_width)


def draw_desc_diagonal(player):
    if player == 1:
        color = circle_color
    else:
        color = cross_color

    pygame.draw.line(screen, color, (15, 15), (width - 15, height - 15), line_width)


def restart():
    screen.fill(bg_color)
    draw_lines()
    for row in range(no_rows):
        for col in range(no_columns):
            board[row][col] = 0


draw_lines()

player = 1
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mousex = event.pos[0]
            mousey = event.pos[1]

            clicked_row = int(mousey // square_size)
            clicked_col = int(mousex // square_size)

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True
                player = player % 2 + 1
                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 1
                game_over = False
    pygame.display.update()
