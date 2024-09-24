# Tic Tac Toe Game

This is a simple command-line Tic Tac Toe game implemented in Python. The game allows a human player to play against an AI opponent using the minimax algorithm.

## Features

- 3x3 Tic Tac Toe board
- Human vs AI gameplay
- AI uses the minimax algorithm to make optimal moves
- Detects win, loss, and tie conditions

## Requirements

- Python 3.x

## How to Play

1. Clone the repository or download the `tic_tac_toe.py` file.
2. Open a terminal and navigate to the directory containing `tic_tac_toe.py`.
3. Run the `tic_tac_toe.py` script using Python 3:

    ```bash
    python tic_tac_toe.py
    ```

4. The game will display the board and prompt the human player to enter their move.
5. Enter the row and column numbers (0, 1, or 2) to place your mark on the board.
6. The AI will then make its move.
7. The game continues until there is a win or a tie.


## Code Overview

- `create_board()`: Creates an empty 3x3 board.
- `display_board(board)`: Displays the current state of the board.
- `make_move(board, row, col, player)`: Makes a move on the board for the given player.
- `check_win(board, player)`: Checks if the given player has won.
- `check_tie(board)`: Checks if the game is a tie.
- `minimax(board, depth, is_maximizing, ai_player, human_player)`: Implements the minimax algorithm for the AI.
- `ai_move(board, ai_player, human_player)`: Determines the best move for the AI.
- `main()`: Main game loop.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The minimax algorithm is a classic AI technique used in game theory.
- Inspired by various Tic Tac Toe implementations and tutorials available online.

