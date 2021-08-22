# Lai Wai Hang, IT01, 06-Aug-2021

import csv
import os

import Game


def get_choice_menu() -> str:
    """
        Display the menu and ask for the choice from the user.

        Returns
        -------
        choice: str
            The valid choice enter by the user.
    """

    valid_choice_list = ['0', '1', '2', '3']
    choice = ''

    menu = (
        '1. Start new game\n'
        '2. Load saved game\n'
        '3. Show highest scores\n'
        '\n'
        '0. Exit\n'
        'Your choice? '
    )

    while True:
        choice = input(menu)

        if choice in valid_choice_list:
            break

        print(f'Please enter a valid choice: {valid_choice_list}')

    return choice


def get_historical_score_file_path(filename: str = 'historical.csv') -> str:
    """
        Get the absolute path of the csv file that use to store the highest score.
        (Note: the csv file should be store under the working directory.)

        Parameters
        ----------
        filename: str
            The name of the file. (Default is 'historical.csv')

        Returns
        -------
        path: str
            The absolute path of the file.
    """

    return os.path.join(os.getcwd(), filename)


def get_historical_score() -> tuple:
    """
        Read the history highest score from the file.
        (Note: return empty arrays if the file is not exist, or is corrupted, or error occurred when reading the csv file.)

        Returns
        -------
        size_list: List[str]
            A list of board size read from the csv file.

        rank_ling: List[int]
            A list of the rank/position read from the csv file.

        name_list: List[str]
            A list of name read from the csv file.

        score_list: List[int]
            A list of score read from the csv file.
    """

    path = get_historical_score_file_path()

    size_list = []
    rank_list = []
    name_list = []
    score_list = []

    if os.path.isfile(path):
        with open(path, mode='r', newline='') as file:
            reader = csv.reader(file, delimiter=',')

            try:
                # * Skip header row.
                next(reader)

                for row in reader:
                    size, rank, name, score = row

                    size_list.append(size)
                    rank_list.append(int(rank))
                    name_list.append(name)
                    score_list.append(int(score))
            except:
                return [], [], [], []

    return size_list, rank_list, name_list, score_list


def split_historical_score(
    size_all_list: list,
    rank_all_list: list,
    name_all_list: list,
    score_all_list: list,
    by_size: str = '4*4',
) -> list:
    """
        Split the full historical score into 2 list.
            - historical score that matched the board size.
            - historical score that doesn't matched the board size.

        Parameters
        ----------
        size_all_list: list
            A list containing all the historical size detail.

        rank_all_list: list
            A list containing all the historical rank detail.

        name_all_list: list
            A list containing all the historical name detail.

        score_all_list: list
            A list containing all the historical score detail.

        by_size: str
            The specific size that use to split/recognize the list. 

        Returns
        -------
        splited_historical_list: list
            - 1st list containing all the detail matched the condition.
            - 2st list containing all the detail not matched the condition.

            general format are as such [size, rank, name, score]
    """

    size_list = []
    rank_list = []
    name_list = []
    score_list = []

    size_other_list = []
    rank_other_list = []
    name_other_list = []
    score_other_list = []

    for i in range(len(size_all_list)):
        size = size_all_list[i]
        rank = rank_all_list[i]
        name = name_all_list[i]
        score = score_all_list[i]

        if by_size == size:
            size_list.append(size)
            rank_list.append(rank)
            name_list.append(name)
            score_list.append(score)
        else:
            size_other_list.append(size)
            rank_other_list.append(rank)
            name_other_list.append(name)
            score_other_list.append(score)

    return (
        [size_list, rank_list, name_list, score_list],
        [size_other_list, rank_other_list, name_other_list, score_other_list]
    )


def write_historical_score(size: str, rank: int, name: str, score: int) -> None:
    """
        Write the score into the file.

        Parameters
        ----------
        size: str
            The board size.

        rank: int
            The ranking of the current game played.

        name: str
            The name of the player.

        score: int
            The score of the current game played.
    """

    path = get_historical_score_file_path()

    # * --- NAMING REFERENCE ---
    # * matched_list: is a list should only contain details that matched the board size.
    # * other_list:   is a list should only contain details that doesn't matched the board size.
    matched_list, other_list = split_historical_score(*get_historical_score(), size)

    detail_list = [size, rank, name, score]

    # * Insert the detail into specific index, and hence rank must be minus 1 here.
    [xlist.insert(rank - 1, detail_list[i]) for i, xlist in enumerate(matched_list)]

    # * Remove the last position from every list if there are more than 9 element.
    if len(matched_list[0]) > 9:
        [xlist.pop() for xlist in matched_list]

    with open(path, mode='w', newline='') as file:
        file.write('size,rank,player,score\n')

        size_list = matched_list[0] + other_list[0]
        name_list = matched_list[2] + other_list[2]
        score_list = matched_list[3] + other_list[3]

        ranking = 1
        previous_size = ''

        for i in range(len(size_list)):
            size = size_list[i]
            name = name_list[i]
            score = score_list[i]

            if previous_size != size:
                previous_size = size
                ranking = 1

            file.write(','.join([size, str(ranking), name, str(score)]))
            file.write('\n')
            ranking += 1
    pass


def display_historical_score() -> None:
    """
        Display the highest score that that read from file.
    """

    size_list, rank_list, name_list, score_list = get_historical_score()
    message = ''

    for i in range(len(rank_list)):
        size = size_list[i]
        rank = rank_list[i]
        name = name_list[i]
        score = score_list[i]

        message += f'{size:<5} {rank:<4} {name:<20} {score:<5}\n'

    print(
        '-----------HIGH SCORES---------------',
        f'{"Size":<5} {"Pos":<4} {"Player":<20} {"Score":<5}',
        f'{"----":<5} {"---":<4} {"------":<20} {"-----":<5}',
        message,
        '-------------------------------------', sep='\n'
    )
    pass


def get_position_rank_and_total(score_dict: dict) -> tuple:
    """
        Calculate the ranking and the total score of the game played.

        Parameters
        ----------
        score_dict: dict
            A dictionary containing all the score for each building and the board size.

        Returns
        -------
        position: int
            Position of the current game played.

        total: int
            Total score of the current game played.
    """

    total = 0

    # * Calculate the total score.
    for building, score_list in score_dict.items():
        if 'BOARD_SIZE' != building:
            total += sum(score_list)

    size = score_dict['BOARD_SIZE']
    matched_list, _ = split_historical_score(*get_historical_score(), size)
    _, rank_list, _, score_list = matched_list
    position = 0

    # * If there no previous record.
    if 1 > len(rank_list):
        position = 1

    # * If the current player score have atleast the minimum historical score.
    elif total >= min(score_list):
        position = len(rank_list) + 1

        for score in score_list[::-1]:
            if total <= score:
                break
            position -= 1

    return position, total


if '__main__' == __name__:
    print(
        'Welcome, mayor of Simp City!\n'
        '----------------------------'
    )

    choice = ''
    score_dict = {}

    while True:
        choice = get_choice_menu()

        if '0' == choice:
            break

        elif '3' == choice:
            display_historical_score()
            continue

        if '1' == choice:
            score_dict = Game.start(is_new=True)

        elif '2' == choice:
            score_dict = Game.start(is_new=False)

        position, total = get_position_rank_and_total(score_dict)

        if 1 <= position <= 9:
            name = input(f'Congratulations! You made the high score board at position {position}.\nPlease enter your name (max 20 chars): ')
            write_historical_score(score_dict['BOARD_SIZE'], position, name, total)
