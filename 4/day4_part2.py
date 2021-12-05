#!/usr/bin/env python3

import re
from collections import defaultdict

with open("input.txt") as f:
    data = f.read()


def parse_data_into_dictionaries(data):
    boards = []
    for i in range(1, len(data)):
        board = list(
            filter(
                None, map(lambda row: list(map(int, row.split())), data[i].split("\n"))
            )
        )
        board_dict = {}
        for row in range(len(board)):
            for column in range(len(board[0])):
                board_dict.update(
                    {
                        board[row][column]: {
                            "row": row,
                            "column": column,
                            "marked": False,
                        }
                    }
                )

        board_dict.update({"marked_rows": defaultdict(int)})
        board_dict.update({"marked_columns": defaultdict(int)})
        board_dict.update({"is_bingo": False})
        boards.append(board_dict)
    return boards


def find_score(numbers, boards, winning_marked_numbers_needed):
    count_boards_bingo = 0
    for number in numbers:
        for board in boards:
            if board.get(number) is None:
                continue

            row = board[number]["row"]
            column = board[number]["column"]

            if board["is_bingo"]:
                continue
            board[number]["marked"] = True

            board["marked_rows"][row] += 1
            board["marked_columns"][column] += 1
            if (
                board["marked_rows"][row] == winning_marked_numbers_needed
                or board["marked_columns"][column] == winning_marked_numbers_needed
            ):
                board["is_bingo"] = True
                count_boards_bingo += 1
                if count_boards_bingo == len(boards):
                    numbers = [number for number in board.keys() if type(number) == int]
                    sum_of_unmarked_numbers = sum(
                        number for number in numbers if not board[number]["marked"]
                    )
                    return sum_of_unmarked_numbers * number

    return 0


data = data.split("\n\n")  # split on empty lines
numbers = list(map(int, data[0].split(",")))

winning_marked_numbers_needed = 5
boards = parse_data_into_dictionaries(data=data)
print(
    find_score(
        boards=boards,
        numbers=numbers,
        winning_marked_numbers_needed=winning_marked_numbers_needed,
    )
)
