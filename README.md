🚀 **Boardgame Checkers:** A modular, object-oriented implementation of the classic strategy game.

A turn-based simulation built with Pygame to apply 'Recursive Pathfinding Algorithms' or in plain language to apply multi-step capturing logic allowing checkers to take multiple pieces in a single move. This project combines the real-time rendering of the board and its pieces through an Object-Oriented Game Architecture.

🛠️ **Skills & Learning Overview:** This project served as a practical application of several core software engineering concepts:

*   **Modular Architecture:** The /src or Source folder models complex systems like the Game Loop (`Game`), Board Logic (`Board`), and Entity Attributes (`Piece`) into distinct classes and files. Example: instead of using a nested list for a board, a Board class manages its own pieces.
*   **Mathematical Game Coordination:** Implements arithmetic logic to map logical grid coordinates (Rows/Cols) to screen positions (X/Y) for accurate rendering of the game.
*   **Recursive Algorithms:** Calculates complex multi-step capture chains (double/triple jumps) for checkers, a core method in the move validation logic.
*   **Event-Driven Programming:** Manages a real-time game loop to handle user input (mouse clicks) and game events seamlessly.

⚡ **Fast-Track Setup:**
Get up and running in seconds with `uv`:

```bash
uv sync
uv run main.py
```

📋 **Project Glossary:**
A classic checkers game in a jolly color scheme of my local region 'Brabant'. This project is inspired by the Object Oriented Programming tutorials of 'Tech with Tim'.

* [Python/Pygame Checkers Part 1](https://www.youtube.com/watch?v=vnd3RfeG3NM)
* [Python/Pygame Checkers Part 2](https://www.youtube.com/watch?v=LSYj8GZMjWY)
* [Python/Pygame Checkers Part 3](https://www.youtube.com/watch?v=_kOXGzkbnps)
* [Rules of English Draughts (Checkers)](https://en.wikipedia.org/wiki/English_draughts)

🕹️'Bossche checkers, verzin is wah gekkers!'
