# ♟️ Chess

A fully playable chess game with a graphical interface, built in Python using Pygame.

## ✨ Features

- ♟️ Complete 8×8 chessboard with a graphical interface
- ✅ Full move validation for all pieces
- 👑 Check and checkmate detection
- 🤝 Draw detection (stalemate & two-king rule)
- 🏰 Special moves: castling, en passant, and pawn promotion

## 📦 Requirements

- Python 3.x
- Pygame
```bash
pip install pygame
```

## ▶️ Running the Game

```bash
python Chess.py
```

> Make sure the piece image assets (e.g. `wP.png`, `bK.png`) are in the same directory as the script.

## 🎮 How to Play

The game is controlled entirely with the mouse:

1. **First click** — select a piece; its legal moves are highlighted.
2. **Second click** — move the piece to the destination square.

When a pawn reaches the last rank, a promotion prompt lets you choose the new piece.

## 🗂️ Project Structure

| Component | Responsibility |
|-----------|----------------|
| `GameState` | Core game logic, move validation, check/checkmate/draw detection |
| `King`, `Queen`, `Rook`, `Bishop`, `Knight`, `Pawn` | Per-piece move generation |
| `Move` | Stores coordinates and metadata for a single move |
| `Board` | Rendering and event handling via Pygame |

## 👤 Author
Morteza Pazhoum — @MortezaPZ

K.N. Toosi University of Technology — Computer Science
