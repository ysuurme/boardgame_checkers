"""
Practice project following the tutorials of Tech With Tim
Part 1 - https://www.youtube.com/watch?v=vnd3RfeG3NM
Part 2 - https://www.youtube.com/watch?v=LSYj8GZMjWY
Part 3 - https://www.youtube.com/watch?v=_kOXGzkbnps
"""

import pygame
from constants import WIDTH, HEIGHT, SQUARE_SIZE, BLACK, YELLOW
from src.game import Game

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bossche checkers, verzin is wah gekkers!')

FPS = 60


def mouse_select_piece(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():  # todo implement sounds for game start, lost pieces and game won
            # todo implement AI
    pygame.init()
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:  # todo implement indicator for player turn
        clock.tick(FPS)

        if game.winner() is not None:
            print('Player {} won the game!'.format(game.winner()))  # todo implement nice victory picture
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = mouse_select_piece(pos)
                game.select_piece(row, col)

        game.update()

    pygame.quit()


main()