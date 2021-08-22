# Lai Wai Hang, IT01, 06-Aug-2021

from typing import Callable, List, Set, Tuple


def get_island_size(
    row: int,
    col: int,
    grid: List[List[str]],
    visited_location_set: Set[Tuple[int]],
    direction: Tuple[str]
) -> int:
    """
        Calculate the island size.
        (Note: Please take note of the direction to traverse.)

        Parameters
        ----------
        row: int
            Row index.

        column: int
            Column index.

        grid: List[List[str]]
            A logical matrix containing all the park detail. 1 represent building - park while other building are represent by 0.

        visited_location_set: Set[Tuple[int, int]]
            A set containing all the visited place. (In the form of x, y coordinates, where x = row, y = col.)

        direction: Tuple[str]
            A tuple containing all the direction to traverse.
            (Note: Only 'up', 'down', 'left', 'right', 'slant' is recognized.)

        Returns
        -------
        size: int
            The size of the island.
    """

    if not(
        0 <= row < len(grid) and
        0 <= col < len(grid[0]) and
        (row, col) not in visited_location_set and
        grid[row][col]
    ):
        return 0

    visited_location_set.add((row, col))

    size = 1

    if 'up' in direction:
        size += get_island_size(row - 1, col, grid, visited_location_set, direction)

    if 'down' in direction:
        size += get_island_size(row + 1, col, grid, visited_location_set, direction)

    if 'left' in direction:
        size += get_island_size(row, col - 1, grid, visited_location_set, direction)

    if 'right' in direction:
        size += get_island_size(row, col + 1, grid, visited_location_set, direction)

    if 'slant' in direction:
        size += (
            get_island_size(row - 1, col - 1, grid, visited_location_set, direction) +
            get_island_size(row - 1, col + 1, grid, visited_location_set, direction) +
            get_island_size(row + 1, col - 1, grid, visited_location_set, direction) +
            get_island_size(row + 1, col + 1, grid, visited_location_set, direction)
        )

    return size


def get_score_beach(
    board: List[List[str]],
    func_get_header_col: Callable[[List[List[str]]], List[str]],
) -> Tuple[int]:
    """
        Calculate the score for the building - beach (BCH).
        Score 3: If the beach in column 'A' or 'D'.
        Score 1: If the beach not in column 'A' or 'D'.

        Parameters
        ----------
        board: List[List[str]]
            2D array containing all the game detail, including column header, row header and placed buildings.

        func_get_header_col: Callable[[List[List[str]]], List[str]]
            A function that will accept board as parameter and return column header list as result.

            Parameters
            ----------
            board: List[List[str]]

            Returns
            -------
            column_header_list: List[str]
                A list containing all the column headers.

        Returns
        -------
        score: Tuple[int]
            A list containing all the score for the specific building - beach (BCH).
    """

    type = 'BCH'
    score_list = []

    col_header_list = func_get_header_col(board)

    # * this tuple ONLY contains INDEX of the column 'A' and 'D'
    col_add_score_tuple = col_header_list.index('A'), col_header_list.index('D')

    for row in board:
        for idx_col, col in enumerate(row):
            if type == col:
                score_list.append(3 if idx_col in col_add_score_tuple else 1)

    return *score_list,


def get_score_factory(board: List[List[str]]) -> Tuple[int]:
    """
        Calculate the score for the building - factory (FAC).
        Score  1: If total count of factory is 1.
        Score  4: If total count of factory is 2.
        Score  9: If total count of factory is 3.
        Score 16: If total count of factory is 4.
        Score 16 + x: If total count of factory more than 4, where x = total count of factory - 4

        Parameters
        ----------
        board: List[List[str]]
            2D array containing all the game detail, including column header, row header and placed buildings.

        Returns
        -------
        score: Tuple[int]
            A list containing all the score for the specific building - factory (FAC).
    """

    type = 'FAC'
    score_list = []

    count = 0
    for row in board:
        count += row.count(type)

    if 4 >= count:
        score_list = [count for _ in range(count)]
    else:
        # * First 4 factory score 4 point, 1 for all subsequent factory
        score_list = [4 for _ in range(4)] + [1 for _ in range(count - 4)]

    return *score_list,


def get_score_shop(
    board: List[List[str]],
    func_get_header_col: Callable[[List[List[str]]], List[str]],
    func_get_header_row: Callable[[List[List[str]]], List[str]],
    func_get_building_around: Callable[[List[List[str]], str], Tuple[str]],
) -> Tuple[int]:
    """
        Calculate the score for the building - shop (SHP).
        Score x: where x = count of unique buidling around the shop.

        Parameters
        ----------
        board: List[List[str]]
            2D array containing all the game detail, including column header, row header and placed buildings.

        func_get_header_col: Callable[[List[List[str]]], List[str]]
            A function that will accept board as parameter and return column header list as result.

            Parameters
            ----------
            board: List[List[str]]

            Returns
            -------
            column_header_list: List[str]
                A list containing all the column headers.

        fun_get_header_row: Callable[[List[List[str]]], List[str]]
            A function that will accept board as paraemter and return the row header list as result.

            Parameters
            ----------
            board: List[List[str]]

            Returns
            -------
            row_header_list: List[str]
                A list containing all the row headers.

        fun_get_building_around: Callable[[List[List[str]], str], Tuple[str]]
            A function that will accept board and location as parameter and return a tuple containing all the building around the location.

            Parameters
            ----------
            board: List[List[str]]

            location: str
                Use to locate the cell on the board.

            Returns
            -------
            building_tuple: tuple
                A tuple containing all the building around the given location.

        Returns
        -------
        score: Tuple[int]
            A list containing all the score for the specific building - beach (BCH).
    """

    type = 'SHP'
    score_list = []

    col_header_list = func_get_header_col(board)
    row_header_list = func_get_header_row(board)

    for idx_row, row in enumerate(board):
        for idx_col, col in enumerate(row):
            if type != col:
                continue

            # * An example of a cell is A1, B2, C3, D4.
            cell = col_header_list[idx_col] + row_header_list[idx_row]
            building_list = func_get_building_around(board, cell)
            unique_building_list = []

            for building in building_list:
                if building not in unique_building_list and ' ' != building:
                    unique_building_list.append(building)

            score_list.append(len(unique_building_list))

    return *score_list,


def get_score_highway(board: List[List[str]]) -> Tuple[int]:
    """
        Calculate the score for the building - highway (HWY).
        Score 1 per connected highway in the SAME row.

        Parameters
        ----------
        board: List[List[str]]
            2D array containing all the game detail, including column header, row header and placed buildings.

        Returns
        -------
        score: Tuple[int]
            A list containing all the score for the specific building - highway (HWY).
    """

    type = 'HWY'

    grid = [[1 if type == col else 0 for col in row] for row in board]

    visited_location_set = set()
    score_list = []

    for idx_row in range(len(grid)):
        for idx_col in range(len(grid[0])):
            size = get_island_size(idx_row, idx_col, grid, visited_location_set, direction=('left', 'right'))

            [score_list.append(size) for _ in range(size)]

    return *score_list,


def get_score_house(
    board: List[List[str]],
    func_get_header_col: Callable[[List[List[str]]], List[str]],
    func_get_header_row: Callable[[List[List[str]]], List[str]],
    func_get_building_around: Callable[[List[List[str]], str], Tuple[str]],
) -> Tuple[int]:
    """
        Calculate the score for the building - house (HSE).
        Score 1: If there are any factory around the house.
        Score x + 2y: 
            If there are not factory around the house, 
            where x = total count of house + shop
            where y = total count of beach

        Parameters
        ----------
        board: List[List[str]]
            2D array containing all the game detail, including column header, row header and placed buildings.

        func_get_header_col: Callable[[List[List[str]]], List[str]]
            A function that will accept board as parameter and return column header list as result.

            Parameters
            ----------
            board: List[List[str]]

            Returns
            -------
            column_header_list: List[str]
                A list containing all the column headers.

        fun_get_header_row: Callable[[List[List[str]]], List[str]]
            A function that will accept board as paraemter and return the row header list as result.

            Parameters
            ----------
            board: List[List[str]]

            Returns
            -------
            row_header_list: List[str]
                A list containing all the row headers.

        fun_get_building_around: Callable[[List[List[str]], str], Tuple[str]]
            A function that will accept board and location as parameter and return a tuple containing all the building around the location.

            Parameters
            ----------
            board: List[List[str]]

            location: str
                Use to locate the cell on the board.

            Returns
            -------
            building_tuple: tuple
                A tuple containing all the building around the given location.

        Returns
        -------
        score: Tuple[int]
            A list containing all the score for the specific building - house (HSE).
    """

    type = 'HSE'
    score_list = []

    col_header_list = func_get_header_col(board)
    row_header_list = func_get_header_row(board)

    for idx_row, row in enumerate(board):
        for idx_col, col in enumerate(row):
            if type != col:
                continue

            score = 0
            cell = col_header_list[idx_col] + row_header_list[idx_row]
            building_list = func_get_building_around(board, cell)

            if 'FAC' in building_list:
                score = 1
            else:
                count_beach = building_list.count('BCH')
                count_house = building_list.count('HSE')
                count_shop = building_list.count('SHP')

                score = count_beach * 2 + count_house + count_shop

            score_list.append(score)
    return *score_list,


def get_score_park(board: List[List[str]]) -> Tuple[int]:
    """
        Calculate the score for the building - park (PRK).
        Score  1: If ONLY 1 park.
        Score  3: If the park size is 2.
        Score  8: If the park size is 3.
        Score 16: If the park size is 4.
        Score 22: If the park size is 5.
        Score 23: If the park size is 6.
        Score 24: If the park size is 7.
        Score 25: If the park size is 8.
        Score 17 + x: For all park size > 8, where x = size of park

        Parameters
        ----------
        board: List[List[str]]
            2D array containing all the game detail, including column header, row header and placed buildings.

        Returns
        -------
        score: Tuple[int]
            A list containing all the score for the specific building - park (PRK).
    """

    type = 'PRK'

    # @ Convert board into logical matrix, where 1 represent park and other type of building are represent by 0.
    grid = [[1 if type == col else 0 for col in row] for row in board]

    visited_location_set = set()
    score_list = []

    table = [
        [1, 2, 3, 4, 5, 6, 7, 8],
        [1, 3, 8, 16, 22, 23, 24, 25]
    ]
    for idx_row in range(len(grid)):
        for idx_col in range(len(grid[0])):
            score = 0
            size = get_island_size(idx_row, idx_col, grid, visited_location_set, direction=('up', 'down', 'left', 'right'))

            if 0 == size:
                continue

            if 8 > size:
                score_idx = table[0].index(size)
                score = table[1][score_idx]
            else:
                score = 17 + size

            score_list.append(score)

    return *score_list,


def get_score_monument(
    board: List[List[str]],
    func_get_header_col: Callable[[List[List[str]]], List[str]],
    func_get_header_row: Callable[[List[List[str]]], List[str]],
) -> Tuple[int]:
    """
        Calculate the score for the building - monument (MON).
        Score 1: If not build at the corner.
        Score 2: If build at the corner.
        Score 4x: If there are atlease 3 monument builded at the corner, where x = total count of monument.

        Parameters
        ----------
        board: List[List[str]]
            2D array containing all the game detail, including column header, row header and placed buildings.

        func_get_header_col: Callable[[List[List[str]]], List[str]]
            A function that will accept board as parameter and return column header list as result.

            Parameters
            ----------
            board: List[List[str]]

            Returns
            -------
            column_header_list: List[str]
                A list containing all the column headers.

        fun_get_header_row: Callable[[List[List[str]]], List[str]]
            A function that will accept board as paraemter and return the row header list as result.

            Parameters
            ----------
            board: List[List[str]]

            Returns
            -------
            row_header_list: List[str]
                A list containing all the row headers.

        Returns
        -------
        score: Tuple[int]
            A list containing all the score for the specific building - monument (MON).
    """

    type = 'MON'
    corner = 0
    total = 0

    col_header_list = func_get_header_col(board)
    row_header_list = func_get_header_row(board)

    idx_last_col = len(col_header_list) - 1
    idx_last_row = len(row_header_list) - 1

    for idx_row, row in enumerate(board):
        for idx_col, col in enumerate(row):
            if type != col:
                continue

            # * If the building is located at the 4 corner.
            if idx_row in [1, idx_last_row] and idx_col in [1, idx_last_col]:
                corner += 1

            total += 1

    score_list = []

    if corner >= 3:
        score_list = [4 for _ in range(total)]
    else:
        score_list = [2 for _ in range(corner)] + [1 for _ in range(total - corner)]

    return *score_list,


def get_score(
    board_size: str,
    board: List[List[str]],
    func_get_header_row: Callable[[List[List[str]]], List[str]],
    func_get_header_col: Callable[[List[List[str]]], List[str]],
    func_get_building_around: Callable[[List[List[str]], str], Tuple[str]],
) -> dict:
    """
        Calculate the score for all the building.

        Parameters
        ----------
        board_size: str
            The board size which will be included in the score dict.

        board: List[List[str]]
            2D array containing all the game detail, including column header, row header and placed buildings.

        func_get_header_col: Callable[[List[List[str]]], List[str]]
            A function that will accept board as parameter and return column header list as result.

            Parameters
            ----------
            board: List[List[str]]

            Returns
            -------
            column_header_list: List[str]
                A list containing all the column headers.

        fun_get_header_row: Callable[[List[List[str]]], List[str]]
            A function that will accept board as paraemter and return the row header list as result.

            Parameters
            ----------
            board: List[List[str]]

            Returns
            -------
            row_header_list: List[str]
                A list containing all the row headers.

        func_get_building_around: Callable[[List[List[str]], str], Tuple[str]]
            A function that will accept board and location as parameter and return a tuple containing all the building around the location.

            Parameters
            ----------
            board: List[List[str]]

            location: str
                Use to locate the cell on the board.

            Returns
            -------
            building_tuple: tuple
                A tuple containing all the building around the given location.

        Returns
        -------
        score_dict: dict
            A dictionary containing all the score for all the different type of building, and the board size.
    """

    return {
        'HSE': get_score_house(board, func_get_header_col, func_get_header_row, func_get_building_around),
        'FAC': get_score_factory(board),
        'SHP': get_score_shop(board, func_get_header_col, func_get_header_row, func_get_building_around),
        'HWY': get_score_highway(board),
        'BCH': get_score_beach(board, func_get_header_col),
        'PRK': get_score_park(board),
        'MON': get_score_monument(board, func_get_header_col, func_get_header_row),
        'BOARD_SIZE': board_size,
    }
