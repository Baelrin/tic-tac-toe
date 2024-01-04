# Define the number of cells for the game board
board_size = 3
# Define the game field
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

MODE_HUMAN_VS_HUMAN = '1'
MODE_HUMAN_VS_AI = '2'


def draw_board():
    ''' Display game board '''
    print(('_' * 4 * board_size))
    for i in range(board_size):
        print((' ' * 3 + '|') * 3)
        print('', board[i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
        print(('_' * 3 + '|') * 3)


def check_win(board):
    ''' Check one of the players' victory '''
    win = False

    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal lines
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical lines
        (0, 4, 8), (2, 4, 6) 			# diagonal lines
    )

    for pos in win_combination:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]] and board[pos[1]] in ('X', 'O')):
            win = board[pos[0]]

    return win


def game_step(index, char):
    ''' Player's move function '''
    if (index > 10 or index < 1 or board[index-1] in ('X', 'O')):
        return False

    board[index-1] = char
    return True


def computer_step(human, ai):
    ''' simple AI for playing with a person'''
    available_steps = [i-1 for i in board if type(i) == int]
    # successful steps in order of priority
    win_steps = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    # first we look at the option for the computer to win
    # and then we prevent a human victory
    for char in (ai, human):
        for pos in available_steps:
            # cloning the game board
            board_ai = board[:]
            board_ai[pos] = char
            if (check_win(board_ai) != False):
                return pos

    # if we are here, that means we did not find a variant for victory
    for pos in win_steps:
        if (pos in available_steps):
            return pos

    return False


def next_player(current_player):
    ''' Determine whose next move'''
    if (current_player == 'X'):
        return 'O'

    return 'X'


def start_game(mode):
    # current player
    current_player = 'X'
    ai_player = 'O'
    # step number
    step = 1

    draw_board()

    # the game continues until someone wins or quits
    while (step < 9) and (check_win(board) == False):
        index = input('Moves ' + current_player +
                      '. Enter field number (0 - exit):')

        if (int(index) == 0):
            break

        # if it was possible to make a move
        if (game_step(int(index), current_player)):
            print('Successful move')

            current_player = next_player(current_player)

            step += 1

            if (mode == MODE_HUMAN_VS_AI):
                if (computer_step('X', 'O') != False):
                    board[computer_step('X', 'O')] = ai_player
                    current_player = next_player(current_player)
                    step += 1

            draw_board()

        else:
            print('Wrong number! Repeat!')

    if (step > 8):
        print('The game is over. Draw!')
    elif check_win(board):
        print('Won ' + check_win(board))


print('Welcome to the game!')
mode = 0
while mode not in (MODE_HUMAN_VS_HUMAN, MODE_HUMAN_VS_AI):
    mode = input(
        "Game mode:\n1 — Player vs Player\n2 — Player vs AI\nChoose a game mode:")
# start of the game
start_game(mode)
