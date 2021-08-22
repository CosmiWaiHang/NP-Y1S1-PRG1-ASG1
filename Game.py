# Lai Wai Hang, IT01, 06-Aug-2021

import csv
import os
from math import ceil
from random import shuffle
from secrets import choice
from typing import List, Tuple

from Display import display_board, display_remaining_building, display_score
from Score import get_score


def get_choice(random_2_building_tuple: Tuple[str, str]) -> str:
    """
        Display the game menu and ask for the choice from the user.

        Parameters
        ----------
        building: Tuple[str, str]
            A tuple containing 2 randomly selected building.

        Returns
        -------
        chocie: str
            The valid choice enter by the user.
    """

    building1, building2 = random_2_building_tuple
    menu = (
        f'1. Build a {building1}\n'
        f'2. Build a {building2}\n'
        '3. See remaining buildings\n'
        '4. See current score\n'
        '\n'
        '5. Save game\n'
        '0. Exit to main menu\n'
        'Your choice? '
    )

    choice = ''
    valid_choice_list = ['1', '2', '3', '4', '5', '0']

    while True:
        choice = input(menu)

        if choice in valid_choice_list:
            break

        print('Please enter a valid choice!\n')

    return choice


def get_historical_board_file_path(filename: str = 'board.csv') -> str:
    """
        Get the absolute path of the csv file that use to store the previous game board.

        Parameters
        ----------
        filename: str
            The name of the file. (Default is 'board.csv')

        Returns
        -------
        path: str
            The absolute path of the file.
    """

    return os.path.join(os.getcwd(), filename)


def generate_board(
    row: int,
    column: int,
) -> List[List[str]]:
    """
        Generate a new board in a row * column manner.

        Parameters
        ----------
        row: int
            A number that indicate how many row should be generated.

        column: int
            A numebr that indicated how many column should be generated.

        Returns
        -------
        board: List[List[str]]
            2D array containing all the game detail, including column header, row header and placed buildings.
    """

    board = []

    # * Preparation of the column header * #
    ordinal = ord('A')

    header_list = [' '] + [chr(ordinal + i) for i in range(column)]

    board.append(header_list)

    # * Preparation for each row * #
    for i in range(1, row + 1):
        row_list = [str(i)] + [' ' for _ in range(column)]

        board.append(row_list)

    return board


def get_board_size() -> Tuple[int, int]:
    """
        Ask for the row and column from the user.

        Returns
        -------
        size: Tuple[int, int]
            The size of the board should be genereated. Format in ({row}, {column})
    """

    row = 0
    column = 0

    message = 'Please indicate how many [{:^6}] to be generated: '

    while True:
        row = input(message.format('row'))
        column = input(message.format('column'))

        if row.isnumeric() and column.isnumeric():
            row = int(row)
            column = int(column)
            break

        print(f'Either row: [{row}] or column: [{column}] is not numeric.')

    return row, column


def get_building_type_list(board: List[List[str]]) -> Tuple[str]:
    """
        Ask 5 building type from the user.

        Parameters
        ----------
        board: List[List[str]]
            2D array containing all the game detail, including column header, row header and placed buildings.

        Returns
        -------
        building_type_list: Tuple[str]
            A list containing 5 type of unique valid building that is selected by the user.
    """
    type_list = ('BCH', 'FAC', 'HSE', 'SHP', 'HWY', 'PRK', 'MON')
    selected_type_list = []

    for building in get_shrink_board(board, is_flatten=True):
        if building not in selected_type_list and building in type_list:
            selected_type_list.append(building)

    while 5 > len(selected_type_list):
        message = (
            f'{"No.":<5}{"Type":<5}\n'
            f'{"---":<5}{"----":<5}\n'
        )

        for i, type in enumerate(type_list, 1):
            if type not in selected_type_list:
                message += f'{f"{i}.":<5}{type:<5}\n'

        print(message)
        selected = input('Please enter a type of building: ')

        if selected in type_list and selected not in selected_type_list:
            selected_type_list.append(selected)
            continue

        print('Either building type cannot be found or already selected!')

    return *selected_type_list,


def get_game_detail(is_new: bool) -> Tuple[List[List[str]], List[str], int, int]:
    """
        Get the game board, number of row and column, and selected building type.
        If is new game: generate new board, ask for the column, row and building type
        If is not new game: read the board from the file, calculate the column, row and building type

        Parameters
        ----------
        is_new: bool
            A flag that indicate if it is a new game.

        Returns
        -------
        board: List[List[str]]
            2D array containing all the game detail, including column header, row header and placed buildings.

        building_type_list: Tuple[str]
            A list containing 5 type of unique valid building that is selected by the user.

        row: int
            Number of row.

        column: int
            Number of column.
    """

    row = 0
    column = 0
    board = []

    if not is_new:
        path = get_historical_board_file_path()

        if os.path.isfile(path):
            with open(path, mode='r', newline='') as file:
                flag = 0

                reader = csv.reader(file, delimiter=',')

                try:
                    for i, row in enumerate(reader, 1):
                        board.append(row)

                        # @ Use total count of first row header row) as column flag
                        if 0 == flag:
                            flag = len(row)

                        # @ If the total count of current column is not the same as header.
                        elif flag != len(row):
                            raise Exception('Column mismatched.')

                    row = i - 1
                    column = flag - 1
                except:
                    board = []
                    print('The file use to save the board might be corrupted')
        else:
            print('The file use to save the board not found.')

    if not board:
        row, column = get_board_size()
        board = generate_board(row, column)

    return board, get_building_type_list(board), row, column


def get_header_col(board: List[List[str]]) -> List[str]:
    """
        Get the column header.
        (Note: this list should only contain alphabet.)

        Parameters
        ----------
        board: List[List[str]]
            2D array containing all the game detail, including column header, row header and placed buildings.

        Returns
        -------
        col_header_list: List[str]
            A list containing all the column header.
    """

    return board[0]


def get_header_row(board: List[List[str]]) -> List[str]:
    """
        Get the row header.
        (Note: this list should only contain numbers, but in str type.)

        Parameters
        ----------
        board: List[List[str]]
            2D array containing all the game detail, including column header, row header and placed buildings.

        Returns
        -------
        row_heder_list: List[str]
            A list containing all the row header.
    """

    return [row[0] for row in board]


def get_shrink_board(
    board: List[List[str]],
    is_flatten: bool
) -> List:
    """
        Get only the building placeholder.
        (Note: In other word, remove the row and column header.)

        Parameters
        ----------
        board: List[List[str]]
            2D array containing all the game detail, including column header, row header and placed buildings.

        is_flatten: bool
            A flag that indicate if the result need to be in flatten into 1d array.

        Returns
        -------
        (Note: there are two possible scenario depending on {is_flatten})

        placeholder_list: List[str]
            A 1D array containing all the placeholder. (When is_flatten = True)

        placeholder_list: List[List[str]]
            A 2D array containing all the placeholder. (When is_flatten = False)
    """

    if is_flatten:
        return [board[r][c] for r in range(1, len(board)) for c in range(1, len(board[r]))]
    else:
        return [[board[r][c] for c in range(1, len(board[r]))] for r in range(1, len(board))]


def get_expand_board(board: List[List[str]]) -> List[List[str]]:
    """
        Get expanded building placeholder.
        (Note: In other word, remove the row and column header, add 1 additional row on above and below, add 1 addtional column at left and right.)

        +-----+-----+-----+-----+-----+-----+
        |     |     |     |     |     |     |
        +-----+-----+-----+-----+-----+-----+
        |     |  X  |  X  |  X  |  X  |     |
        +-----+-----+-----+-----+-----+-----+
        |     |  X  |  X  |  X  |  X  |     |
        +-----+-----+-----+-----+-----+-----+
        |     |  X  |  X  |  X  |  X  |     |
        +-----+-----+-----+-----+-----+-----+
        |     |  X  |  X  |  X  |  X  |     |
        +-----+-----+-----+-----+-----+-----+
        |     |     |     |     |     |     |
        +-----+-----+-----+-----+-----+-----+
        (Note: X is the original board size and the empty placeholder is the expanded placeholder.)

        Parameters
        ----------
        board: List[List[str]]
            2D array containing all the game detail, including column header, row header and placed buildings.

        Returns
        -------
        board: List[List[str]]
            An expanded 2D array containing all the placed building only.
    """

    expanded_board = [[' ' for _ in range(len(board[0]) + 2)] for _ in range(len(board) + 2)]

    for r in range(len(board)):
        for c in range(len(board[r])):
            expanded_board[r + 1][c + 1] = board[r][c]

    return expanded_board


def get_remaining_building_list(
    board: List[List[str]],
    building_type_list: List[str],
    row: int,
    column: int,
) -> List[str]:
    """
        Calculate the remaining building.

        Parameters
        ----------
        board: List[List[str]]
            2D array containing all the game detail, including column header, row header and placed buildings.

        building_type_list: Tuple[str]
            A list containing 5 type of unique valid building that is selected by the user.

        row: int
            Number of row.

        column: int
            Number of column.

        Returns
        -------
        remaining_building_list: List[str]
            A list containing all the remaining building
    """

    flatten_board = get_shrink_board(board, is_flatten=True)
    number_of_building_per_type = ceil((row * column * 2) / 5)

    return [type for type in building_type_list for _ in range(number_of_building_per_type - flatten_board.count(type))]


def get_random(building_list: List[str]) -> Tuple[str, str]:
    """
        Get 2 random element from the given list.

        Parameters
        ----------
        building_list: List[str]
            A list containing all the remaining building that haven't been placed by the user.

        Returns
        -------
        random_building: Tuple[str, str]
            2 element randomly selected from the list.
    """

    first = choice(building_list)
    second = choice(building_list)

    return first, second


def get_choosen_building(
    building: Tuple[str, str],
    choice: str
) -> str:
    """
        Get the specific building that have been selected by the user.

        Parameters
        ----------
        building: Tuple[str, str]
            A tuple containing 2 randomly selected building.

        choice: str
            The valid choice given by the user.

        Returns
        -------
        building: str
            The specific building that selected by the user.
    """

    x, y = building

    return x if '1' == choice else y


def get_building_nearby(
    board: List[List[str]],
    location: str
) -> Tuple[str, str, str, str]:
    """
        Get all the building around the given location.

        Example 1
        +-----+-----+-----+-----+-----+
        |     |  A  |  B  |  C  |  D  |
        +-----+-----+-----+-----+-----+
        |  1  |     |     |  X  |     |
        +-----+-----+-----+-----+-----+
        |  2  |     |  X  | BCH |  X  |
        +-----+-----+-----+-----+-----+
        |  3  |     |     |  X  |     |
        +-----+-----+-----+-----+-----+
        |  4  |     |     |     |     |
        +-----+-----+-----+-----+-----+
        (Description: here is the prefect example, all the building in the placeholder marked in X will be identify and return.)
        (Sample: C1, C3, B2, D2)

        Example 2
        +-----+-----+-----+-----+-----+
        |     |  A  |  B  |  C  |  D  |
        +-----+-----+-----+-----+-----+
        |  1  |     |  X  | BCH |  X  |
        +-----+-----+-----+-----+-----+
        |  2  |     |     |  X  |     |
        +-----+-----+-----+-----+-----+
        |  3  |     |     |     |     |
        +-----+-----+-----+-----+-----+
        |  4  |     |     |     |     |
        +-----+-----+-----+-----+-----+
        (Description: here is another example, all the building in the placeholder marked in X will be idetify and return.)
        (Note: above example only 3 location will be check, in addtional 1 empty placeholder will be added into the return result. Total of 4 element will be return same as example 1.)
        (Sample: C2, B1, D1, ' ')

        Example 3
        +-----+-----+-----+-----+-----+
        |     |  A  |  B  |  C  |  D  |
        +-----+-----+-----+-----+-----+
        |  1  | BCH |  X  |     |     |
        +-----+-----+-----+-----+-----+
        |  2  |  X  |     |     |     |
        +-----+-----+-----+-----+-----+
        |  3  |     |     |     |     |
        +-----+-----+-----+-----+-----+
        |  4  |     |     |     |     |
        +-----+-----+-----+-----+-----+
        (Description: here is the last example, all the building in the placeholder marked in X will be identify and return.)
        (Note: above example 3 only 2 location will be check, in additional 2 empty placeholder will be added into the return result. Total of 4 element will be return same as example 1.)
        (Sample: A2, B1, ' ', ' ')

        Parameters
        ----------
        board: List[List[str]]
            2D array containing all the game detail, including column header, row header and placed buildings.

        location: str
            A string use to locate the position on the board.

        Returns
        -------
        building_list: List[str]
            A list containing all the building nearby the location, up, down, left, right.
    """

    col_header_list = get_header_col(board)
    row_header_list = get_header_row(board)

    expanded_board = get_expand_board(get_shrink_board(board, is_flatten=False))

    column, row = get_representative(location)
    building_list = []

    # * Index of location at the expanded board
    idx_exp_col = col_header_list.index(column)
    idx_exp_row = row_header_list.index(row)

    # * Location to check
    idx_exp_col_ckr_tup = idx_exp_col - 1, idx_exp_col + 1
    idx_exp_row_ckr_tup = idx_exp_row - 1, idx_exp_row + 1

    building_list = [expanded_board[idx_exp_row][col] for col in idx_exp_col_ckr_tup] + [expanded_board[row][idx_exp_col] for row in idx_exp_row_ckr_tup]
    return building_list


def have_building_nearby(
    board: List[List[str]],
    location: str,
    building_type_list: List[str]
) -> bool:
    """
        Check if there are any building nearby the given location.

        Parameters
        ----------
        board: List[List[str]]
            2D array containing all the game detail, including column header, row header and placed buildings.

        location: str
            A string use to locate the position on the board.

        building_type_list: Tuple[str]
            A list containing 5 type of unique valid building that is selected by the user.

        Returns
        -------
        have_building_nearby: bool
            A flag that indicate if there are any building nearby the given location.
    """

    for building in get_building_nearby(board, location):
        # * Make sure the building exist
        if building in building_type_list:
            return True

    return False


def able_to_build(
    board: List[List[str]],
    location: str,
    turn: int,
    building_type_list: List[str]
) -> bool:
    """
        Check if the user able to build a building at the given location.

        Parameters
        ----------
        board: List[List[str]]
            2D array containing all the game detail, including column header, row header and placed buildings.

        location: str
            A string use to locate the position on the board.

        turn: int
            An integer indicating the current turn.

        building_type_list: Tuple[str]
            A list containing 5 type of unique valid building that is selected by the user.

        Returns
        -------
        able_to_build: bool
            A flag that indicate if the location available 
    """

    column, row = get_representative(location)
    idx_row = get_header_row(board).index(row)
    idx_col = get_header_col(board).index(column)

    if ' ' != board[idx_row][idx_col]:
        return False

    if have_building_nearby(board, location, building_type_list) or 1 >= turn:
        return True

    return False


def set_building(
    board: List[List[str]],
    location: str,
    building: str,
) -> bool:
    """
        Place the building into the placeholder.

        Parameters
        ----------
        board: List[List[str]]
            2D array containing all the game detail, including column header, row header and placed buildings.

        location: str
            A string use to locate the position on the board.

        building: str
            The building name to be place into specified placeholder.

        Returns
        -------
        (Note: board is pass by reference, returning of board is NOT required. (POINTER))

        is_set_sucessful: bool
            A flag that indicate the if the building sucessfully place to the specified placeholder.
    """

    col_header_list = get_header_col(board)
    row_header_list = get_header_row(board)

    column, row = get_representative(location)

    idx_col = col_header_list.index(column)
    idx_row = row_header_list.index(row)

    board[idx_row][idx_col] = building
    return True


def save(board: List[List[str]]) -> None:
    """
        Save the board to a file.

        Parameters
        ----------
        board: List[List[str]]
            2D array containing all the game detail, including column header, row header and placed buildings.
    """

    path = get_historical_board_file_path()

    with open(path, mode='w', newline='\n') as file:
        for row in board:
            file.write(','.join(row))
            file.write('\n')

    print('Game saved!')
    pass


def get_representative(location: str) -> tuple[str, str]:
    """
        Split the location into numeric (row) and alphabet (column).

        Parameters
        ----------
        location: str
            A string use to locate the position on the board.

        Returns
        -------
        row: str
            The row representative.

        column: str
            The column representative.
    """

    column = ''
    row = ''

    for c in location:
        if c.isalpha():
            column += c
        elif c.isnumeric():
            row += c

    return column, row


def is_valid_location(
    board: List[List[str]],
    location: str
) -> bool:
    """
        Check if the given location is valid.

        Parameters
        ----------
        board: List[List[str]]
            2D array containing all the game detail, including column header, row header and placed buildings.

        location: str
            A string use to locate the position on the board.

        Returns
        -------
        is_valid: bool
            A flag that indicate if the given location is valid.
    """

    col_header_list = get_header_col(board)
    row_header_list = get_header_row(board)

    column, row = get_representative(location)

    if column in col_header_list and row in row_header_list:
        return True

    return False


def has_empty_location(board: List[List[str]]) -> bool:
    """
        Check if there are any empty placeholder.
        (Note: top left corner is always empty and hence must be ignored.)

        Parameters
        ----------
        board: List[List[str]]
            2D array containing all the game detail, including column header, row header and placed buildings.
    """
    count = 0

    for row in board:
        for col in row:
            if col == ' ':
                # * Use to early break if there are more than 2 empty placeholder.
                if count > 1:
                    return True
                count += 1

    return count > 1


def get_turn(board: List[List[str]]) -> int:
    """
        Calculate the current turn.
        (Note: total placeholder - count of empty + 1)
        (Etc : there are 5 placed building on 4 * 4 board :=> 16 total placeholder - 11 empty space + 1 = 6)

        Parameters
        ----------
        board: List[List[str]]
            2D array containing all the game detail, including column header, row header and placed buildings.

        Returns
        -------
        turn: int
            The current turn.
    """

    shrinked_board = get_shrink_board(board, is_flatten=True)

    return len(shrinked_board) - shrinked_board.count(' ') + 1


def start(is_new: bool) -> dict:
    """
        Run the game.

        Parameters
        ----------
        is_new: bool
            A flag that indicate if it is a new game.

        Returns
        -------
        score_dict: dict
            A dictionary containing all the score for all the different type of building, and the board size.
    """

    board, building_type_list, row, column = get_game_detail(is_new)
    remaining_building_list = get_remaining_building_list(board, building_type_list, row, column)

    score_dict = {}

    turn = get_turn(board)

    while has_empty_location(board):
        shuffle(remaining_building_list)
        random_building_tuple = get_random(remaining_building_list)

        print(f'Turn {turn}')
        display_board(board, remaining_building_list, building_type_list)

        choice = get_choice(random_building_tuple)

        if choice in ['1', '2']:
            location = input('Build where? ')
            building = get_choosen_building(random_building_tuple, choice)

            if is_valid_location(board, location):
                if able_to_build(board, location, turn, building_type_list):
                    if set_building(board, location, building):
                        remaining_building_list.remove(building)
                        turn += 1
                    else:
                        print(f'Failed to place the [{building}] at the location: [{location}]')
                else:
                    print('You must build next to an existing building.')
            else:
                print(f'Location: [{location}] if not valid.')

        elif '3' == choice:
            display_remaining_building(remaining_building_list, building_type_list)

        elif '4' == choice:
            score_dict = get_score(None, board, get_header_row, get_header_col, get_building_nearby)
            display_score(score_dict)

        elif '5' == choice:
            save(board)

        else:
            break

    print('You have come to the end of the game')

    score_dict = get_score(f'{row}*{column}', board, get_header_row, get_header_col, get_building_nearby)
    display_board(board, remaining_building_list, building_type_list)
    display_score(score_dict)

    return score_dict
