# Lai Wai Hang, IT01, 06-Aug-2021

from typing import Dict, List


def display_board(
    board: List[List[str]],
    building_remaining_list: List[str],
    building_type_list: List[str],
) -> None:
    """
        Display the board and the remaining building.
        (Note: Board should be place at the left side of the board while remaining building should be located at the right side.)

        Parameters
        ----------
        board: List[List[str]]
            2D array containing all the game detail, including column header, row header and placed buildings.

        building_remaining_list: List[str]
            A list containing all the remaining building.

        building_type_list: List[str]
            A list containing all the different type of the building.
    """

    seperator = ''  # To store the last seperating line.
    message_board_list = []
    message_remaining_building_list = [f'{"Building":<15}{"Remaining":<15}', f'{"--------":<15}{"---------":<15}']

    # * Preparation of Game Board Printing * #
    for row in board:
        seperator = '+'
        placeholder = '|'

        for col in row:
            seperator += f'{"-"*5:^5}+'
            placeholder += f'{col:^5}|'

        message_board_list.append(seperator)
        message_board_list.append(placeholder)

    message_board_list.append(seperator)

    # * Preparation of Building Remaining Printing * #
    for type in building_type_list:
        count = building_remaining_list.count(type)

        message_remaining_building_list.append(f'{type:<15}{count:<15}')

    len_msg_brd_list = len(message_board_list)
    len_msg_rem_list = len(message_remaining_building_list)
    max = len_msg_brd_list if len_msg_brd_list > len_msg_rem_list else len_msg_rem_list

    # * Printing * #
    for i in range(max):
        left = ''
        right = ''

        if len_msg_brd_list > i:
            left = message_board_list[i]

        if len_msg_rem_list > i:
            right = message_remaining_building_list[i]

        print(f'{left:<75} {right:>25}')
    pass


def display_remaining_building(
    building_remaining_list: List[str],
    building_type_list: List[str],
) -> None:
    """
        Display the remaining building.

        Parameters
        ----------
        building_remaining_list: List[str]
            A list containing all the remaining building.

        building_type_list: List[str]
            A list containing all the different type of the building.
    """

    message = f'\n{"Building":<15}{"Remaining":<15}\n{"--------":<15}{"---------":<15}\n'

    for type in building_type_list:
        count = building_remaining_list.count(type)

        message += f'{type:<15}{count:<15}\n'

    print(message)
    pass


def display_score(score_dict: Dict[str, List[int]]) -> None:
    """
        Calculate the total score and display the score for each building.

        Parameters
        ----------
        score_dict: Dict[str, List[int]]
            A dictionary that contain all the score for different type of building and the size of board.

            Keys
            ----
            building_type: str
                The name/type of the building.

            Values:
            score_list: List[int]
                A list containing all the score for all the specific building. 
    """

    message = '\n'
    total = 0

    for type, score_list in score_dict.items():
        if 'BOARD_SIZE' == type:
            continue

        score = sum(score_list)
        total += score

        message += f'{type}: {" + ".join([str(score) for score in score_list])} = {score}\n'

    message += f'Total = {total}\n'
    print(message)
    pass
