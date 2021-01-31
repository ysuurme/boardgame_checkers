"""
Practice project following the tutorials of Tech With Tim
Part 1 - https://www.youtube.com/watch?v=vnd3RfeG3NM
Part 2 - https://www.youtube.com/watch?v=LSYj8GZMjWY
Part 3 - https://www.youtube.com/watch?v=_kOXGzkbnps
"""

import pygame

from checkers.config import WIDTH, HEIGHT
from checkers.board import Board

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

FPS = 60


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        board.create_board(WIN)
        pygame.display.update()

    pygame.quit()


main()
