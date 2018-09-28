def draw_board(marks):
    print(  '   |   |   \n'\
            ' {} | {} | {} \n'\
            '___|___|___\n'\
            '   |   |   \n'\
            ' {} | {} | {} \n'\
            '___|___|___\n'\
            '   |   |   \n'\
            ' {} | {} | {}\n'\
            '   |   |   \n'.format(*marks[2], *marks[1], *marks[0]))


def print_invalid_choice():
    print('Invalid choice, must be from 1 to 9!')

def numpad_to_coords(n):
    """ Converts a numpad representation of a placeholder on the tic tac toe board to the indices (x, y coordinates) of the marks 2d array
    """
    if n == 1:
        return (0, 0)
    elif n == 2:
        return (0, 1)
    elif n == 3:
        return (0, 2)

    elif n == 4:
        return (1, 0)
    elif n == 5:
        return (1, 1)
    elif n == 6:
        return (1, 2)

    elif n == 7:
        return (2, 0)
    elif n == 8:
        return (2, 1)
    elif n == 9:
        return (2, 2)


def coords_to_numpad(n):
    """ Converts an indices (x, y coords) of the marks 2d array to a numpad representation of a placeholder on the tic tac toe board
    """
    if n == 1:
        return (0, 0)
    elif n == 2:
        return (0, 1)
    elif n == 3:
        return (0, 2)
    elif n == 4:
        return (1, 0)
    elif n == 5:
        return (1, 1)
    elif n == 6:
        return (1, 2)
    elif n == 7:
        return (2, 0)
    elif n == 8:
        return (2, 1)
    elif n == 9:
        return (2, 2)

def prompt_player(name, sym, marks):
    while True:
        try:
            choice = int(input('{}, it is your turn. Choose a number: '.format(name)))
        except ValueError:
            print_invalid_choice()
            continue

        if choice < 1 or choice > 9:
            print_invalid_choice()
            continue

        # convert to coords
        (x, y) = numpad_to_coords(choice)
        
        # check if the space is available
        if marks[x][y] != ' ':
            print('That space has already been marked!')
        else:
            marks[x][y] = sym
            break

def check_board(marks):
    """Checks if X or O has won. Returns 'X' if X has won, 'O' if O has won, 'D' for draw, or 'I' for incomplete
    """

    winning_combinations = [[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9],
                            [1, 4, 7],
                            [2, 5, 8],
                            [3, 6, 9],
                            [7, 5, 3],
                            [1, 5, 9]]

    contains_space = False

    for combo in winning_combinations:
        (x1, y1) = numpad_to_coords(combo[0])
        (x2, y2) = numpad_to_coords(combo[1])
        (x3, y3) = numpad_to_coords(combo[2])

        s = {marks[x1][y1], marks[x2][y2], marks[x3][y3]}
        if ' ' in s:
            contains_space = True
        elif len(s) == 1:
            # found winner
            return list(s)[0]

    if contains_space:
        return 'I'
    else:
        return 'D'

def play_game(p1_name, p2_name):

    # set default symbol selection for each player
    p1_sym = 'X'
    p2_sym = 'O'

    # Find out which symbol per player
    p1_choice = input('{}, would you like to be X or O? '.format(p1_name)).lower()

    # Keeps track of which player's turn it is. 0 for p1 and 1 for p2
    turn = 0

    if p1_choice.upper() == 'O':
        turn = 1
        p1_sym = 'O'
        p2_sym = 'X'

    # use a 3x3 array to store marks
    marks = [[' ']*3, [' ']*3, [' ']*3]

    # Loop until game ends
    while True:
        if turn == 0:
            prompt_player(p1_name, p1_sym, marks)
            turn = 1
        else:
            prompt_player(p2_name, p2_sym, marks)
            turn = 0

        draw_board(marks)

        # Check board if there is a winner
        r = check_board(marks)

        if r == 'I':
            continue
        else:
            if r == 'X':
                if p1_sym == 'X':
                    winner = p1_name
                else:
                    winner = p2_name

                print('{} wins!'.format(winner))
            elif r == 'O':
                if p1_sym == 'O':
                    winner = p1_name
                else:
                    winner = p2_name

                print('{} wins!'.format(winner))
            elif r == 'D':
                print('It\'s a draw!')
            break

    ans = input('Would you like to play again? (y or n): ')
    if ans.lower().startswith('y'):
        return 1
    else:
        return 0

def main():
    print('Welcome to Tic Tac Toe\n')
    print('How to play: choose a number on the number pad that visually corresponds'\
          ' to a place holder on the Tic Tac Toe board like this:\n')
    draw_board([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

    print()

    p1_name = input('Enter name for player 1: ')
    p2_name = input('Enter name for player 2: ')
    

    while (play_game(p1_name, p2_name)):
        pass

if __name__ == '__main__':
    main()
