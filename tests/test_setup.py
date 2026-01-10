
import sys
import os

# Add current directory to path
sys.path.append(os.getcwd())

try:
    import pygame
    # Mock pygame display for headless environment
    os.environ["SDL_VIDEODRIVER"] = "dummy"
    pygame.init()
    pygame.display.set_mode((1,1))
    
    from constants import BLACK
    from src.board import Board
    from src.game import Game
    
    print("Imports successful.")
    
    b = Board()
    print("Board initialized.")
    
    if len(b.board) != 8:
        print(f"Error: Board has {len(b.board)} rows, expected 8.")
        sys.exit(1)
        
    print("Board size correct.")
    
    print("Validation complete.")
    
except Exception as e:
    print(f"Validation failed: {e}")
    sys.exit(1)
