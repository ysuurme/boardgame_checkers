"""
Practice project following the tutorials of Tech With Tim
Part 1 - https://www.youtube.com/watch?v=vnd3RfeG3NM
Part 2 - https://www.youtube.com/watch?v=LSYj8GZMjWY
Part 3 - https://www.youtube.com/watch?v=_kOXGzkbnps
"""

import pygame

from checkers.config import WIDTH, HEIGHT, SQUARE_SIZE
from checkers.board import Board

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

FPS = 60

def mouse_select_piece(pos):
    x,y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    piece = board.select_piece(0, 1)
    board.move_piece(piece, 4, 3)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = mouse_select_piece(pos)
                piece = board.select_piece(row, col)
                board.move_piece(piece, 0, 0)

        board.create_board(WIN)
        pygame.display.update()

    pygame.quit()


main()
