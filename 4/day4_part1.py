#!/usr/bin/env python3

import re
from collections import defaultdict

with open("test.txt") as f:
    data = f.read()


def parse_data_into_dictionaries(data):
    boards = []
    for i in range(1, len(data)):
        board = list(filter(None, map(lambda row: list(map(int, row.split())), data[i].split("\n"))))
        board_dict = {}
        for row in range(len(board)):
            for column in range(len(board[0])):
                board_dict.update({board[row][column] : {"row": row, "column": column, "marked" : False }})

        board_dict.update({"marked_rows" : defaultdict(int)})
        board_dict.update({"marked_columns" : defaultdict(int)})
        boards.append(board_dict)
    return boards

def find_score(numbers, boards, winning_marked_numbers_needed):
    for number in numbers:
        for board in boards:
            if board.get(number) is None:
                continue
            board[number]["marked"] = True

            row = board[number]["row"]
            column = board[number]["column"]
            board["marked_rows"][row] += 1
            board["marked_columns"][column] += 1
            if board["marked_rows"][row] == winning_marked_numbers_needed or board["marked_columns"][column] == winning_marked_numbers_needed:
                return sum(number for number in board.keys() if not board[number]["marked"] and type(number) == int) * number

    return 0


data = data.split("\n\n")  # split on empty lines
numbers = list(map(int, data[0].split(",")))

winning_marked_numbers_needed = 5
boards = parse_data_into_dictionaries(data=data)
print(find_score(boards=boards, numbers=numbers, winning_marked_numbers_needed=winning_marked_numbers_needed))
