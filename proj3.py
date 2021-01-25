"""
File: design3.txt
Author: Rooklyn Kline
Date: 12/6/19
Section: 15
E-mail: rkline2@umbc.edu
Description:
   This program is a scoring system of the board game "Go".
It replaces all of the empty spaces with the player's piece that
controls those areas. It will then sum up the total scores for
each player and it will display the original board,
"painted" board, and the total scores of the two players.
"""

# Represents input validation
INVALID_BOARD = "bad board"

# Represents an empty string
NOTHING = ''

# Used for string comparison
EXIT_PROGRAM = "QUIT"
BLACK_PIECE = 'X'
WHITE_PIECE = 'O'
EMPTY_SPACE = '+'
COLOR = ["X", "O"]


def nowhitespace(input_response):
    """
    This function removes all of the white spaces of any string value statement.
    :param input_response: This parameter represents the
     word or phrase you would like to remove all of the white spaces from.
    :return: The parameter as a single word or phrase.
    """
    input_response = input_response.strip()
    input_response = input_response.split()
    input_response = NOTHING.join(input_response)
    return input_response


def make_two_d_list(input_file):
    """
    This function creates a two dimensional list of the finished go-board.
    :param input_file: The file the user would like to convert
    :return: A two dimensional list of go-board
    """
    two_d_board = []
    # reads and appends the file to a list and automatically closes it
    with open(input_file, "r") as the_file:
        for line in the_file:
            line = nowhitespace(line)
            two_d_board.append([line])
    return two_d_board


def is_length_valid(two_d_list):
    """
    This recursive function checks to see if each column of the go-board
    are the same.
    :param two_d_list: The two dimensional list that is checked
    :return: Returns the list if the list is valid or returns an invalid message if the
    list is not valid.
    """
    # recursive function that will check the length of each 2-D list element 
    if len(two_d_list) == 1:
        return two_d_list
    elif len(two_d_list[0][0]) != len(two_d_list[1][0]):
        two_d_list = INVALID_BOARD
        return two_d_list
    elif len(two_d_list[0][0]) == len(two_d_list[1][0]):
        is_valid_list = is_length_valid(two_d_list[1:])
        if is_valid_list == INVALID_BOARD:
            return INVALID_BOARD
        else:
            return [two_d_list[0]] + is_valid_list


def find_score(painted_board):
    """
    This function counts the total score for each player.
    :param painted_board: Represents the board that only contains
    the player's pieces.
    :return: The total scores of the two players as a list
    """
    b_piece = 0
    w_piece = 0
    # nested for loop that counts each character in an element of a list
    for x in range(len(painted_board)):
        for y in range(len(painted_board[x])):
            if painted_board[x][y] == BLACK_PIECE:
                b_piece += 1
            elif painted_board[x][y] == WHITE_PIECE:
                w_piece += 1
    return [b_piece, w_piece]


def print_boards(original_board):
    """
    This function displays the original and the painted board as well as the
    total scores for each player. This function will call other functions
    in order to find these values.
    :param original_board: The original imputed board
    :return: None
    """
    paint_list = []
    # displays the original board
    print("We are scoring this board:")
    for x in range(len(original_board)):
        print(original_board[x][0])
    # displays the painted board
    print("\nHere is the colored board:")
    for y in range(len(original_board)):
        paint_list.append(original_board[y][0])
    # rows and columns have to be one less than the actual value 
    paint_board = find_color(paint_list, len(paint_list) - 1, len(paint_list[0])-1)
    for x in paint_board:
        print(x)
    score = find_score(paint_board)
    print("Black scored:", score[0])
    print("White scored:", score[1])


def find_color(board, row, column):
    """
    This recursive function "colors" all of the empty spaces with the player
    that owns that territory.
    :param board: the original board as a list 
    :param row: to row value of the board
    :param column: the column value of the board
    :return: The painted version of the board as a list
    """
    # Okay I know this looks bad, but its really simple.
    # I'll show you

    # base case is when the list is done checking for characters in the list (board)
    if (row == -1) or (column == -1):
        return board
    # asks if the selected character is located in an edge 
    elif (row == len(board) - 1) or (row == 0) or (column == len(board[0]) - 1) or (column == 0):
        # asks if the selected character is located in the bottom right corner
        if row == len(board) - 1 and column == len(board[0]) - 1:
            if board[row][column] == EMPTY_SPACE:
                # sees if there are any characters that are by the current character 
                if board[row - 1][column] in COLOR:
                    if board[row - 1][column] == COLOR[0]:
                        new_board = board[:row] + [board[row][:column] + COLOR[0] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row, column - 1)
                    elif board[row - 1][column] == COLOR[1]:
                        new_board = board[:row] + [board[row][:column] + COLOR[1] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row, column - 1)
                elif board[row][column - 1] in COLOR:
                    if board[row][column - 1] == COLOR[0]:
                        new_board = board[:row] + [board[row][:column] + COLOR[0] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row, column - 1)
                    elif board[row][column - 1] == COLOR[1]:
                        new_board = board[:row] + [board[row][:column] + COLOR[1] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row, column - 1)
                # if there isnt't any, it will call the function again recursively and move one space 
                else:
                    ans = find_color(board, row, column - 1)
                    if ans[row][column - 1] == COLOR[0]:
                        new_board = ans[:row] + [ans[row][:column] + COLOR[0] + ans[row][column + 1:]] \
                            + ans[row + 1:]
                        return new_board
                    elif ans[row][column - 1] == COLOR[1]:
                        new_board = ans[:row] + [ans[row][:column] + COLOR[1] + ans[row][column + 1:]] \
                            + ans[row + 1:]
                        return new_board
            # if the character is a color then it will move one space
            elif board[row][column] in COLOR:
                return find_color(board, row, column - 1)
        # asks if the selected character is located in the bottom left corner
        elif row == len(board) - 1 and column == 0:
            if board[row][column] == EMPTY_SPACE:
                # sees if there are any characters that are by the current character
                if board[row - 1][column] in COLOR:
                    if board[row - 1][column] == COLOR[0]:
                        new_board = board[:row] + [board[row][:column] + COLOR[0] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row - 1, column + len(board[0]) - 1)
                    elif board[row - 1][column] == COLOR[1]:
                        new_board = board[:row] + [board[row][:column] + COLOR[1] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row - 1, column + len(board[0]) - 1)

                elif board[row][column + 1] in COLOR:
                    if board[row][column + 1] == COLOR[0]:
                        new_board = board[:row] + [board[row][:column] + COLOR[0] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row - 1, column + len(board[0]) - 1)
                    elif board[row][column + 1] == COLOR[1]:
                        new_board = board[:row] + [board[row][:column] + COLOR[1] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row - 1, column + len(board[0]) - 1)
                # if there isnt't any, it will call the function again recursively and move one space
                else:
                    ans = find_color(board, row - 1, column + len(board[0]) - 1)
                    if ans[row-1][column] == COLOR[0]:
                        new_board = ans[:row] + [ans[row][:column] + COLOR[0] + ans[row][column + 1:]] \
                            + ans[row + 1:]
                        return new_board
                    elif ans[row-1][column] == COLOR[1]:
                        new_board = ans[:row] + [ans[row][:column] + COLOR[1] + ans[row][column + 1:]] \
                            + ans[row + 1:]
                        return new_board
            # if the character is a color then it will move one space
            elif board[row][column] in COLOR:
                return find_color(board, row + 1, column + len(board[0]) - 1)
        # asks if the selected character is located in the bottom right corner
        elif row == 0 and column == len(board[0])-1:
            if board[row][column] == EMPTY_SPACE:
                # sees if there are any characters that are by the current character
                if board[row][column - 1] in COLOR:
                    if board[row][column - 1] == COLOR[0]:
                        new_board = board[:row] + [board[row][:column] + COLOR[0] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row, column - 1)
                    elif board[row][column - 1] == COLOR[1]:
                        new_board = board[:row] + [board[row][:column] + COLOR[1] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row, column - 1)

                elif board[row + 1][column] in COLOR:
                    if board[row + 1][column] == COLOR[0]:
                        new_board = board[:row] + [board[row][:column] + COLOR[0] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row, column - 1)
                    elif board[row + 1][column] == COLOR[1]:
                        new_board = board[:row] + [board[row][:column] + COLOR[1] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row, column - 1)
                # if there isnt't any, it will call the function again recursively and move one space
                else:
                    ans = find_color(board, row, column - 1)
                    if ans[row][column - 1] == COLOR[0]:
                        new_board = ans[:row] + [ans[row][:column] + COLOR[0] + ans[row][column + 1:]] \
                            + ans[row + 1:]
                        return new_board
                    elif ans[row][column-1] == COLOR[1]:
                        new_board = ans[:row] + [ans[row][:column] + COLOR[1] + ans[row][column + 1:]] \
                            + ans[row + 1:]
                        return new_board
            # if the character is a color then it will move one space
            elif board[row][column] in COLOR:
                return find_color(board, row, column - 1)
        # asks if the selected character is located in the top left corner
        elif row == 0 and column == 0:
            if board[row][column] == EMPTY_SPACE:
                 # sees if there are any characters that are by the current character
                if board[row + 1][column] in COLOR:
                    if board[row + 1][column] == COLOR[0]:
                        new_board = board[:row] + [board[row][:column] + COLOR[0] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row - 1, column - 1)
                    elif board[row + 1][column] == COLOR[1]:
                        new_board = board[:row] + [board[row][:column] + COLOR[1] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row - 1, column - 1)
                elif board[row][column + 1] in COLOR:
                    if board[row][column + 1] == COLOR[0]:
                        new_board = board[:row] + [board[row][:column] + COLOR[0] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row - 1, column - 1)
                    elif board[row][column + 1] == COLOR[1]:
                        new_board = board[:row] + [board[row][:column] + COLOR[1] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row - 1, column - 1)
                # if there isnt't any, it will call the function again recursively and move one space
                else:
                    ans = find_color(board, row, column + 1)
                    if ans[row][column] == COLOR[0]:
                        new_board = ans[:row] + [ans[row][:column] + COLOR[0] + ans[row][column + 1:]] \
                            + ans[row + 1:]
                        return new_board
                    elif ans[row][column] == COLOR[1]:
                        new_board = ans[:row] + [ans[row][:column] + COLOR[1] + ans[row][column + 1:]] \
                            + ans[row + 1:]
                        return new_board
            # if the character is a color then it will move one space
            elif board[row][column] in COLOR:
                return find_color(board, row - 1, column - 1)
        # asks if the selected character is located in the bottom side
        elif row == len(board) - 1:
            if board[row][column] == EMPTY_SPACE:
                # sees if there are any characters that are by the current character
                if board[row - 1][column] in COLOR:
                    if board[row - 1][column] == COLOR[0]:
                        new_board = board[:row] + [board[row][:column] + COLOR[0] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row, column - 1)
                    elif board[row - 1][column] == COLOR[1]:
                        new_board = board[:row] + [board[row][:column] + COLOR[1] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row, column - 1)
                elif board[row][column - 1] in COLOR:
                    if board[row][column - 1] == COLOR[0]:
                        new_board = board[:row] + [board[row][:column] + COLOR[0] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row, column - 1)
                    elif board[row][column - 1] == COLOR[1]:
                        new_board = board[:row] + [board[row][:column] + COLOR[1] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row, column - 1)
                elif board[row][column + 1] in COLOR:
                    if board[row][column + 1] == COLOR[0]:
                        new_board = board[:row] + [board[row][:column] + COLOR[0] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row, column - 1)
                    elif board[row][column + 1] == COLOR[1]:
                        new_board = board[:row] + [board[row][:column] + COLOR[1] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row, column - 1)
                # if there isnt't any, it will call the function again recursively and move one space
                else:
                    ans = find_color(board, row, column - 1)
                    if ans[row][column - 1] == COLOR[0]:
                        new_board = ans[:row] + [ans[row][:column] + COLOR[0] + ans[row][column + 1:]] \
                            + ans[row + 1:]
                        return new_board
                    elif ans[row][column - 1] == COLOR[1]:
                        new_board = ans[:row] + [ans[row][:column] + COLOR[1] + ans[row][column + 1:]] \
                            + ans[row + 1:]
                        return new_board
            # if the character is a color then it will move one space
            elif board[row][column] in COLOR:
                return find_color(board, row, column - 1)
        # asks if the selected character is located in the top side
        elif row == 0:
            if board[row][column] == EMPTY_SPACE:
                # sees if there are any characters that are by the current character
                if board[row][column - 1] in COLOR:
                    if board[row][column - 1] == COLOR[0]:
                        new_board = board[:row] + [board[row][:column] + COLOR[0] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row, column - 1)
                    elif board[row][column - 1] == COLOR[1]:
                        new_board = board[:row] + [board[row][:column] + COLOR[1] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row, column - 1)
                elif board[row + 1][column] in COLOR:
                    if board[row + 1][column] == COLOR[0]:
                        new_board = board[:row] + [board[row][:column] + COLOR[0] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row, column - 1)
                    elif board[row + 1][column] == COLOR[1]:
                        new_board = board[:row] + [board[row][:column] + COLOR[1] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row, column - 1)

                elif board[row][column + 1] in COLOR:
                    if board[row][column + 1] == COLOR[0]:
                        new_board = board[:row] + [board[row][:column] + COLOR[0] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row, column - 1)
                    elif board[row][column + 1] == COLOR[1]:
                        new_board = board[:row] + [board[row][:column] + COLOR[1] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row, column - 1)
                # if there isnt't any, it will call the function again recursively and move one space
                else:
                    ans = find_color(board, row, column - 1)
                    if ans[row][column-1] == COLOR[0]:
                        new_board = ans[:row] + [ans[row][:column] + COLOR[0] + ans[row][column + 1:]] \
                            + ans[row + 1:]
                        return new_board
                    elif ans[row][column - 1] == COLOR[1]:
                        new_board = ans[:row] + [ans[row][:column] + COLOR[1] + ans[row][column + 1:]] \
                            + ans[row + 1:]
                        return new_board
            # if the character is a color then it will move one space
            elif board[row][column] in COLOR:
                return find_color(board, row, column - 1)
        # asks if the selected character is located in the right side
        elif column == len(board[0]) - 1:
            if board[row][column] == EMPTY_SPACE:
                # sees if there are any characters that are by the current character
                if board[row - 1][column] in COLOR:
                    if board[row - 1][column] == COLOR[0]:
                        new_board = board[:row] + [board[row][:column] + COLOR[0] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row, column - 1)
                    elif board[row - 1][column] == COLOR[1]:
                        new_board = board[:row] + [board[row][:column] + COLOR[1] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row, column - 1)
                elif board[row][column - 1] in COLOR:
                    if board[row][column - 1] == COLOR[0]:
                        new_board = board[:row] + [board[row][:column] + COLOR[0] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row, column - 1)
                    elif board[row][column - 1] == COLOR[1]:
                        new_board = board[:row] + [board[row][:column] + COLOR[1] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row, column - 1)

                elif board[row + 1][column] in COLOR:
                    if board[row + 1][column] == COLOR[0]:
                        new_board = board[:row] + [board[row][:column] + COLOR[0] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row, column - 1)
                    elif board[row + 1][column] == COLOR[1]:
                        new_board = board[:row] + [board[row][:column] + COLOR[1] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row, column - 1)
                # if there isnt't any, it will call the function again recursively and move one space
                else:
                    ans = find_color(board, row, column - 1)
                    if ans[row][column-1] == COLOR[0]:
                        new_board = ans[:row] + [ans[row][:column] + COLOR[0] + ans[row][column + 1:]] \
                            + ans[row + 1:]
                        return new_board
                    elif ans[row][column-1] == COLOR[1]:
                        new_board = ans[:row] + [ans[row][:column] + COLOR[1] + ans[row][column + 1:]] \
                            + ans[row + 1:]
                        return new_board
            # if the character is a color then it will move one space
            elif board[row][column] in COLOR:
                return find_color(board, row, column - 1)
        # asks if the selected character is located in the left side
        elif column == 0:
            if board[row][column] == EMPTY_SPACE:
                # sees if there are any characters that are by the current character
                if board[row - 1][column] in COLOR:
                    if board[row - 1][column] == COLOR[0]:
                        new_board = board[:row] + [board[row][:column] + COLOR[0] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row - 1, column + len(new_board[0]) - 1)
                    elif board[row - 1][column] == COLOR[1]:
                        new_board = board[:row] + [board[row][:column] + COLOR[1] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row - 1, column + len(new_board[0]) - 1)
                elif board[row][column + 1] in COLOR:
                    if board[row][column + 1] == COLOR[0]:
                        new_board = board[:row] + [board[row][:column] + COLOR[0] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row - 1, column + len(new_board[0]) - 1)
                    elif board[row][column + 1] == COLOR[1]:
                        new_board = board[:row] + [board[row][:column] + COLOR[1] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row - 1, column + len(new_board[0]) - 1)
                elif board[row + 1][column] in COLOR:
                    if board[row + 1][column] == COLOR[0]:
                        new_board = board[:row] + [board[row][:column] + COLOR[0] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row - 1, column + len(new_board[0]) - 1)
                    elif board[row + 1][column] == COLOR[1]:
                        new_board = board[:row] + [board[row][:column] + COLOR[1] + board[row][column + 1:]] \
                            + board[row + 1:]
                        return find_color(new_board, row - 1, column + len(new_board[0]) - 1)
                # if there isnt't any, it will call the function again recursively and move one space
                else:
                    ans = find_color(board, row - 1, column + len(board) - 1)
                    if ans[row-1][column] == COLOR[0]:
                        new_board = ans[:row] + [ans[row][:column] + COLOR[0] + ans[row][column:]] \
                            + ans[row + 1:]
                        return new_board
                    elif ans[row-1][column] == COLOR[1]:
                        new_board = ans[:row] + [ans[row][:column] + COLOR[1] + ans[row][column:]] \
                            + ans[row + 1:]
                        return new_board
            # if the character is a color then it will move one space
            elif board[row][column] in COLOR:
                return find_color(board, row - 1, column + len(board[0]) - 1)
    # sees if there are any characters that are by the current character
    elif board[row][column] == EMPTY_SPACE:
        if board[row - 1][column] in COLOR:
            if board[row - 1][column] == COLOR[0]:
                new_board = board[:row] + [board[row][:column] + COLOR[0] + board[row][column + 1:]] \
                    + board[row + 1:]
                return find_color(new_board, row, column - 1)
            elif board[row - 1][column] == COLOR[1]:
                new_board = board[:row] + [board[row][:column] + COLOR[1] + board[row][column + 1:]] \
                    + board[row + 1:]
                return find_color(new_board, row, column - 1)
        elif board[row][column - 1] in COLOR:
            if board[row][column - 1] == COLOR[0]:
                new_board = board[:row] + [board[row][:column] + COLOR[0] + board[row][column + 1:]] \
                    + board[row + 1:]
                return find_color(new_board, row, column - 1)
            elif board[row][column - 1] == COLOR[1]:
                new_board = board[:row] + [board[row][:column] + COLOR[1] + board[row][column + 1:]] \
                    + board[row + 1:]
                return find_color(new_board, row, column - 1)
        elif board[row + 1][column] in COLOR:
            if board[row + 1][column] == COLOR[0]:
                new_board = board[:row] + [board[row][:column] + COLOR[0] + board[row][column + 1:]] \
                    + board[row + 1:]
                return find_color(new_board, row, column - 1)
            elif board[row + 1][column] == COLOR[1]:
                new_board = board[:row] + [board[row][:column] + COLOR[1] + board[row][column + 1:]] \
                    + board[row + 1:]
                return find_color(new_board, row, column - 1)
        elif board[row][column + 1] in COLOR:
            if board[row][column + 1] == COLOR[0]:
                new_board = board[:row] + [board[row][:column] + COLOR[0] + board[row][column + 1:]] \
                    + board[row + 1:]
                return find_color(new_board, row, column - 1)
            elif board[row][column + 1] == COLOR[1]:
                new_board = board[:row] + [board[row][:column] + COLOR[1] + board[row][column + 1:]] \
                    + board[row + 1:]
                return find_color(new_board, row, column - 1)
        # if there isnt't any, it will call the function again recursively and move one space
        else:
            ans = find_color(board, row, column - 1)
            if ans[row][column - 1] == COLOR[0]:
                new_board = ans[:row] + [ans[row][:column] + COLOR[0] + ans[row][column + 1:]] \
                    + ans[row + 1:]
                return new_board
            elif ans[row][column - 1] == COLOR[1]:
                new_board = ans[:row] + [ans[row][:column] + COLOR[1] + ans[row][column + 1:]] \
                    + ans[row + 1:]
                return new_board
    # if the character is a color then it will move one space
    elif board[row][column] in COLOR:
        return find_color(board, row, column - 1)


if __name__ == "__main__":
    ask_file = nowhitespace(input("Enter a file you would like to access: "))
    # This only checks if all of the columns are the same per line
    imputed_board = is_length_valid(make_two_d_list(ask_file))
    while imputed_board == INVALID_BOARD and ask_file != EXIT_PROGRAM:
        if imputed_board == INVALID_BOARD:
            print("The file you have entered is invalid")
            ask_file = nowhitespace(input("Enter a file you would like to access "
                                          "(Enter " + "'" + EXIT_PROGRAM + "'" +
                                          " to exit the program): "))
            if ask_file == EXIT_PROGRAM:
                print("Goodbye")
            else:
                imputed_board = is_length_valid(make_two_d_list(ask_file))
    if ask_file == EXIT_PROGRAM:
        pass
    else:
        print_boards(imputed_board)
                        
                        
                        
        
                        
