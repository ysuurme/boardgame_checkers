# Configuration file holding constant values used throughout the project.
import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# Board colors, let's go Brabant!
RED = (255, 0, 0)
WHITE = (255, 255, 255)
# Piece colors, let's go HC Den Bosch!
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREY = (128, 128, 128)  # Piece outline color
# Piece size and outline
PADDING = 20
OUTLINE = 2

# King piece image
CROWN = pygame.transform.scale(pygame.image.load('assets/king_piece.png'), (45, 45))
