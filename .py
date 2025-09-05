"""
A command-line implementation of the classic game Tic-Tac-Toe.

This script allows two players to play Tic-Tac-Toe against each other in the console.
It demonstrates fundamental Python concepts such as functions, loops, conditional
statements, and list manipulation.
"""

def create_board():
    """
    Creates and returns a new, empty Tic-Tac-Toe board.
    The board is represented as a list of 9 strings.
    """
    return [" " for _ in range(9)]

def display_board(board):
    """
    Prints the Tic-Tac-Toe board to the console.
    
    Args:
        board (list): The current state of the game board.
    """
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(board, player):
    """
    Checks if a player has won the game.

    Args:
        board (list): The current state of the game board.
        player (str): The player's symbol, "X" or "O".

    Returns:
        bool: True if the player has won, False otherwise.
    """
    win_conditions = [
        # Horizontal wins
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        # Vertical wins
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        # Diagonal wins
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def check_tie(board):
    """
    Checks if the game has ended in a tie.

    Args:
        board (list): The current state of the game board.

    Returns:
        bool: True if the board is full and there is no winner, False otherwise.
    """
    return " " not in board

def get_player_move(player, board):
    """
    Prompts the current player for their move and validates the input.

    Args:
        player (str): The current player's symbol, "X" or "O".
        board (list): The current state of the game board.

    Returns:
        int: The valid index (0-8) where the player wants to place their mark.
    """
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                return move
            else:
                print("Invalid move. The position is already taken or out of range. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def tic_tac_toe():
    """
    The main function to run the Tic-Tac-Toe game.
    """
    board = create_board()
    current_player = "X"
    game_over = False

    while not game_over:
        display_board(board)
        move = get_player_move(current_player, board)
        board[move] = current_player

        if check_win(board, current_player):
            display_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            game_over = True
        elif check_tie(board):
            display_board(board)
            print("The game is a tie!")
            game_over = True
        else:
            # Switch to the other player
            current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe!")
    tic_tac_toe()
