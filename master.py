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
        if int(index) == 0:
            break
        elif index.isdigit():
            # If move was successful
            if (game_step(int(index), current_player)):
                print('Successful move')
                draw_board()
                # Increase the step number
                step += 1
            else:
                print('Wrong number, try again!')
        else:
            print("Invalid input. Please enter the field number (1-9).")


print("Добро пожаловать в Крестики-нолики!")
start_game()
