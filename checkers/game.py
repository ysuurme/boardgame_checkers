import pygame

from .config import BLACK, YELLOW
from .board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def _init():
        self.selected = None
        self.board = Board()
        self.turn = BLACK
        self.valid_moves = {}

    def update(self):
        self.board.create_board(self.win)
        pygame.display.update()

    def reset(self):
        self._init()

    def select_piece(self, row, col):
        if self.selected:
            result = self._move_piece(row, col)
            if not result:
                self.select_piece() = None
                self.select_piece(row, col)

        piece = self.board.select_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def move_piece(self, row, col):
        piece = self.board.select_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move_piece(self.selected, row, col)
        else:
            return False
        return True

    def change_turn(self):
        if self.turn == BLACK:
            self.turn = YELLOW
        else:
            self.turn = BLACK


