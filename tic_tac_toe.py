def create_board():
    """
    Creates an empty 3x3 board for the game.
    Filled with empty spaces.
    Using list comprehension to create rows and columns
    """
    board = [[' ' for _ in range(3)] for _ in range(3)]
    return board

def display_board(board):
    """
    Displays a tic tac toe game board
    """

    print('   0   1   2')
    for idx, row in enumerate(board):
        print(f"{idx}  {' | '.join(row)}")
        if idx < 2:
            print("  ---+---+---")




# create a function to handle moves made by players

def make_move(board, row, col, player):
    """
    Makes a move on the board
    places player's symbol in that position if the chosen cell is empty
    """
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    else:
        return False


def check_win(board, player):
    """
    Checks if player has won
    """
    # check rows
    for row in range(3):
        if all(cell == player for cell in board[row]):
            return True

    # check columns

        if all(board[col][row] == player for col in range(3)):
            return True

    # check diagonals
    if all(board[row][row] == player for row in range(3)):
       return True

    if all(board[row][2 - row] == player for row in range(3)):
        return True

    return False

def check_tie(board):
    """
    Checks if the game is a tie
    """
    return all([cell != ' ' for row in board for cell in row])

def minimax(board, depth, is_maximizing, ai_player, human_player):
    """
    Minimax algorithm
    """
    if check_win(board, ai_player):
        return 1
    elif check_win(board, human_player):
        return -1
    elif check_tie(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        moves_available = False
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = ai_player
                    score = minimax(board, depth + 1, False, ai_player, human_player)
                    board[row][col] = ' '
                    best_score = max(score, best_score)
            if not moves_available:
                return 0
        return best_score

    else:
        best_score = float('inf')
        moves_available = False
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = human_player
                    score = minimax(board, depth + 1, True, ai_player, human_player)
                    board[row][col] = ' '
                    best_score = min(score, best_score)
        if not moves_available:
            return 0
        return best_score

def ai_move(board, ai_player, human_player):
    """
    Makes an AI move
    """
    best_score = float('-inf')
    move = None

    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = ai_player
                score = minimax(board, 0, False, ai_player, human_player)
                board[row][col] = ' '
                if score > best_score:
                    best_score = score
                    move = (row, col)

    return move

def main():
    """
    Main game loop

    """
    board = create_board() # create an empty board
    human_player = 'X' # start with player 'X'
    ai_player = 'O'
    current_player = 'X'

    while True: # game loop
        display_board(board)
        if current_player == human_player:
            print(f"Player {human_player}'s turn")
            try:
                row = int(input('Enter the row (0-2): '))
                col = int(input('Enter the column (0-2): '))
            except ValueError:
                print(" Invalid input. Please enter a number between 0 and 2.")
                continue

            if row not in range(3) or col not in range(3): # check if the input is valid
                print("Invalid postion. Try again.")
                continue

            if not make_move(board, row, col, human_player): # make the move on the board
                print("That position is already taken. Try again.")
                continue
        else:
            print(f"AI Player {ai_player} is making a move...")
            row, col = ai_move(board, ai_player, human_player)
            make_move(board, row, col, ai_player)

        if check_win(board, current_player):
            display_board(board)
            if current_player == human_player:
                print('Congratulations! You have won the game!')
            else:
                print(f"AI Player {ai_player} has won the game!")
            break
        elif check_tie(board):
                display_board(board)
                print("It's a tie!")
                break
        current_player = ai_player if current_player == human_player else human_player



    print("Thanks for playing!")

if __name__ == '__main__':
    main()