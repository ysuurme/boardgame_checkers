# creates the checkers board

import pygame

from .config import ROWS, COLS, RED, WHITE, SQUARE_SIZE, BLACK, YELLOW, GREY, PADDING, OUTLINE, CROWN


class Board:
    def __init__(self):
        self.board = [[]]
        self.black_left = self.yellow_left = 12
        self.black_kings = self.yellow_kings = 0
        self.draw_pieces()

    def draw_board(self, win):  # TWT draw_squares
        win.fill(WHITE)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_pieces(self):  # TWT create board
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

    def move_piece(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)
        if row == ROWS or row == 0:
            piece.make_piece_king()
            if piece.color == YELLOW:
                self.yellow_kings += 1
            elif piece.color == BLACK:
                self.black_kings += 1

    def select_piece(self, row, col):
        return self.board[row][col]

    def remove_piece(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == BLACK or piece.king:
            moves.update(self._traverse_left(row+1, max(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, max(row + 3, ROWS), 1, piece.color, right))

        if piece.color == YELLOW or piece.king:
            moves.update(self._traverse_left(row - 1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped

                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._traverse_left(r+step, row, step, color, left - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, left + 1, skipped=last))
                break

            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1

        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped

                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)

                    moves.update(self._traverse_left(r + step, row, step, color, right - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, right + 1, skipped=last))
                break

            elif current.color == color:
                break
            else:
                last = [current]

            right += 1

        return moves


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
