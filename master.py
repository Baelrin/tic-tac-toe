# Define the number of cells for the game board
board_size = 3
# Define the game field
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Define game modes
MODE_HUMAN_VS_HUMAN = '1'
MODE_HUMAN_VS_AI = '2'


def draw_board():
    '''
    Draw the game board:
    This function provides a visual representation of the game board.
    '''
    print('_' * 4 * board_size)
    for i in range(board_size):
        cell1 = board[i*3]
        cell2 = board[1+i*3]
        cell3 = board[2+i*3]
        print(f' {cell1} | {cell2} | {cell3} ')
        print('_' * 4 * board_size)


def check_win(board):
    '''
    Check the game status:
    This function checks whether any player (X or O) has already won the game.
    '''
    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal lines
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical lines
        (0, 4, 8), (2, 4, 6)             # diagonal lines
    )
    win_set = set(win_combination)
    for pos in win_set:
        if (board[pos[0]] == board[pos[1]] == board[pos[2]]) and board[pos[1]] in ('X', 'O'):
            return board[pos[0]]
    return False


def game_step(index, char):
    '''
    Make a player's move:
    This function updates the game board with the new move.
    '''
    if index < 1 or index > 9:
        return False
    if board[index-1] in ('X', 'O'):
        return False
    board[index-1] = char
    return True


def computer_step(human, ai):
    '''
    Make the AI's move:
    This function calculates the next move for the AI, based on the current board state.
    '''
    available_steps = {i-1 for i in board if type(i) == int}
    win_steps = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    for char in (ai, human):
        for pos in available_steps:
            temp = board[pos]
            board[pos] = char
            if (check_win(board) != False):
                board[pos] = temp
                return pos
            board[pos] = temp
    for pos in win_steps:
        if (pos in available_steps):
            return pos
    return False


def next_player(current_player):
    '''
    Determine the next move's player:
    This function changes the current player based on the last player who made the move.
    '''
    player_switch = {'X': 'O', 'O': 'X'}
    return player_switch[current_player]


def start_game(mode):
    '''
    Start the game:
    This function initializes the game and handles the game loop, until the game is over.
    '''
    current_player = 'X'
    ai_player = 'O'
    step = 1
    draw_board()
    while step < 9 and not check_win(board):
        index = input('Moves ' + current_player +
                      '. Enter field number (0 - exit):')
        if int(index) == 0:
            break
        if game_step(int(index), current_player):
            print('Successful move')
            current_player = next_player(current_player)
            step += 1
            if mode == MODE_HUMAN_VS_AI:
                if computer_step('X', 'O') != False:
                    board[computer_step('X', 'O')] = ai_player
                    current_player = next_player(current_player)
                    step += 1
            draw_board()
        else:
            print('Wrong number! Repeat!')
    if step > 8:
        print('The game is over. Draw!')
    elif check_win(board):
        print('Won ' + str(check_win(board)))


# Begin game entrance point
print('Welcome to the game!')
mode = 0
while mode not in (MODE_HUMAN_VS_HUMAN, MODE_HUMAN_VS_AI):
    mode = input(
        "Game mode:\n1 — Player vs Player\n2 — Player vs AI\nChoose a game mode:")
# start of the game
start_game(mode)
