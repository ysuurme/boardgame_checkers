import pygame
from constants import SQUARE_SIZE, GREY, PADDING, OUTLINE, CROWN, BLACK, YELLOW

class Piece:
    def __init__(self, row, col, color):
        self.padding = PADDING
        self.outline = OUTLINE
        self.row = row
        self.col = col
        self.color = color
        self.king = False

        if self.color == BLACK:
            self.direction = 1
        if self.color == YELLOW:
            self.direction = -1

        self.x = 0
        self.y = 0

        self.calc_piece_pos()

    def __repr__(self):
        return str(self.color)

    def draw_piece(self, win):
        radius = SQUARE_SIZE // 2 - self.padding
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.outline)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))

    def calc_piece_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_piece_king(self):
        self.king = True

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_piece_pos()
