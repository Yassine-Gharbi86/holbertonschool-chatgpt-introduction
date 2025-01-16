def print_board(board):
    """
    Print the current state of the board.
    
    Parameters:
    board (list): 2D list representing the Tic-Tac-Toe board.
    
    Returns:
    None
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """
    Check if there is a winner in the current state of the board.
    
    Parameters:
    board (list): 2D list representing the Tic-Tac-Toe board.
    
    Returns:
    bool: True if there is a winner, False otherwise.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_draw(board):
    """
    Check if the game is a draw (no more moves possible and no winner).
    
    Parameters:
    board (list): 2D list representing the Tic-Tac-Toe board.
    
    Returns:
    bool: True if the game is a draw, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Main function to play the Tic-Tac-Toe game.
    
    Returns:
    None
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")
            continue

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid input. Row and column must be between 0 and 2.")
            continue

        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break
            elif is_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

if __name__ == "__main__":
    tic_tac_toe()