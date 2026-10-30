# Chess

A mouse-driven chess game built with Python and Pygame.

## Features

- Legal move highlighting for each selected piece
- Check and checkmate detection
- Castling, en passant, and pawn promotion
- Stalemate and bare-kings draw handling

## Requirements

- Python 3
- Pygame

Install Pygame:

```bash
python -m pip install pygame
```

## Run

From the repository root:

```bash
python Chess.py
```

Select a piece to see its legal destinations, then click a destination square to move. When a pawn reaches the last rank, choose its promotion piece in the prompt.

## Project layout

- `Chess.py` contains the game state, move rules, and Pygame interface.
- `images/` contains the piece sprites loaded by the game.

Keep the working directory at the repository root so the relative image paths resolve.
