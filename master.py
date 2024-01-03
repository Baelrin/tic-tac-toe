# Define the number of cells for the game board
board_size = 3

# Define the game field
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Function to draw a single row of the board


def draw_row(row):
    return " " + str(row[0]) + " | " + str(row[1]) + " | " + str(row[2]) + "\n"

# Function to display the game board


def draw_board():
    board_str = "_" * 4 * board_size + "\n"
    # For each row in the board
    for i in range(board_size):
        row = [board[i * 3], board[1 + i * 3], board[2 + i * 3]]
        board_str += " " * 3 + "|" + " " * 3 + "|" + " " * 3 + "\n"
        board_str += draw_row(row)
        board_str += "_" * 4 * board_size + "\n"
    print(board_str)

# Function to perform a move


def game_step(index, char):
    try:
        index = int(index)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return False

    # Check if the move is valid
    if index < 1 or index > 9 or board[index - 1] in ('X', 'O'):
        return False
    # Set the new value at the index
    board[index - 1] = char
    return True

# Function to check for victory of one of the players


def check_win():
    win_combinations = {(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
                        (0, 4, 8), (2, 4, 6)}  # Diagonal

    for combination in win_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != ' ':
            return board[combination[0]]
    return None

# Function to start the game


def start_game():
    current_player = "X"  # The current player
    move_number = 1  # The current move number
    draw_board()

    # Loop until there are no more moves
    while move_number < 10:
        index = input("Current player => " + current_player +
                      ". Enter the number (0 - exit):")
        if int(index) == 0:
            break
        elif 1 <= int(index) <= 9:
            # If the move was successful
            if game_step(int(index), current_player):
                print('Successful move')
                draw_board()
                # Switch players
                current_player = "O" if current_player == "X" else "X"
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
