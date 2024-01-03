# Number of cells
board_size = 3
# Game field
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def draw_board():
    """Display game board"""
    print("_" * 4 * board_size)
    for i in range(board_size):
        print((" " * 3 + "|") * 3)
        print("", board[i * 3], "|", board[1 + i * 3],
              "|", board[2 + i * 3], "|")
        print(("_" * 3 + "|") * 3)
    pass


def game_step(index, char):
    """Perform a move"""
    if (index > 9 or index < 1 or board[index - 1] in ('X', 'O')):
        return False
    board[index - 1] = char
    return True


def check_win():
    """Checking for victory of one of the players"""
    win = False
    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
        (0, 4, 8), (2, 4, 6)  # Diagonal
    )

    for pos in win_combination:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]):
            win = board[pos[0]]
    return win


def start_game():
    # Current Player
    current_player = "X"
    # Other Player
    other_player = "O"
    # Move Number
    move_number = 1
    draw_board()

    while move_number < 10:
        index = input(
            "Current player => "
            + current_player
            + ". Enter the number (0 - exit):"
        )
        if int(index) == 0:
            break
        elif index.isdigit():
            # If move was successful
            if game_step(int(index), current_player):
                print('Successful move')
                draw_board()
                # Switch players
                current_player, other_player = other_player, current_player
                move_number += 1
                # Check if there is a winner
                winner = check_win()
                if winner:
                    print(f'Winner — {winner} :)')
                    break
                elif move_number == 10:
                    print('It\'s a draw!')
                    break
        else:
            print("Invalid input. Please enter the field number (1-9).")


print("Welcome to Tic-Tac-Toe!")
start_game()
