# creates the checkers board

import pygame


from .config import ROWS, COLS, RED, WHITE, SQUARE_SIZE, BLACK, YELLOW, GREY, PADDING, OUTLINE


class Board:
    def __init__(self):
        self.board = [[]]
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.draw_pieces()

    def draw_board(self, win):  # TWT draw_squares
        win.fill(WHITE)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


    def draw_pieces(self):  #TWT create board
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, BLACK))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, YELLOW))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)


    def create_board(self, win):
        self.draw_board(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw_piece(win)


class Piece:
    def __init__(self, row, col, color):
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
        self.padding = PADDING
        self.outline = OUTLINE

        radius = SQUARE_SIZE // 2 - self.padding
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.outline)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)


    def calc_piece_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2


    def make_piece_king(self):
        self.king = True
