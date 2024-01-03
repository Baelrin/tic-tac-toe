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


def game_step():
    """Perform a move"""
    pass


def check_win():
    return False


def start_game():
    # Current Player
    current_player = "X"
    # Step Number
    step = 1
    draw_board()

    while True and (step < 10) and (check_win() == False):
        index = input(
            (
                "Current player => "
                + current_player
                + ". Enter the field number (0 - exit):"
            )
        )
        if index.isdigit():
            step += 1
        else:
            print("Invalid input. Please enter the field number.")


print("Добро пожаловать в Крестики-нолики!")
start_game()
