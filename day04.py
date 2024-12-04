from typing import List


def read_data() -> List[str]:
    with open("day04.txt", "r") as f:
        return [l for l in f.readlines()]


def count_xmas_from(data, row, column) -> int:
    WINNER = {"M", "S"}
    if row == 0 or column == 0 or row+1 == len(data) or column+1 == len(data[0]):
        return 0
    bottom_left_top_right = {data[row + 1][column - 1], data[row - 1][column + 1]}
    top_left_bottom_right = {data[row - 1][column - 1], data[row + 1][column + 1]}
    return 1 if bottom_left_top_right == WINNER and top_left_bottom_right == WINNER else 0


def count_from(data, row, column) -> int:
    n_rows = len(data)
    n_cols = len(data[0])
    result = 0
    has_space_above = row >= 3
    has_space_left = column >= 3
    has_space_below = (row + 3) < n_rows
    has_space_right = (column + 3) < n_cols
    if has_space_left and (data[row][column - 1] == "M" and data[row][column - 2] == "A" and data[row][column - 3] == "S"):
        result += 1
    if has_space_above and has_space_left and (data[row - 1][column - 1] == "M" and data[row - 2][column - 2] == "A" and data[row - 3][column - 3] == "S"):
        result += 1
    if has_space_above and (data[row - 1][column] == "M" and data[row - 2][column] == "A" and data[row - 3][column] == "S"):
        result += 1
    if has_space_above and has_space_right and (data[row - 1][column + 1] == "M" and data[row - 2][column + 2] == "A" and data[row - 3][column + 3] == "S"):
        result += 1
    if has_space_right and (data[row][column+1] == "M" and data[row][column+2] == "A" and data[row][column+3] == "S"):
        result += 1
    if has_space_below and has_space_right and (data[row + 1][column + 1] == "M" and data[row + 2][column + 2] == "A" and data[row + 3][column + 3] == "S"):
        result += 1
    if has_space_below and (data[row + 1][column] == "M" and data[row + 2][column] == "A" and data[row + 3][column] == "S"):
        result += 1
    if has_space_below and has_space_left and (data[row + 1][column - 1] == "M" and data[row + 2][column - 2] == "A" and data[row + 3][column - 3] == "S"):
        result += 1
    return result


def count_matches(data: List[str]):
    result = 0
    for row_num, line in enumerate(data):
        for col_num, val in enumerate(line):
            if "X" == val:
                result += count_from(data, row_num, col_num)
    return result


def count_xmas_matches(data: List[str]) -> int:
    result = 0
    for row_num, line in enumerate(data):
        for col_num, val in enumerate(line):
            if "A" == val:
                result += count_xmas_from(data, row_num, col_num)
    return result


if __name__ == "__main__":
    data = read_data()
    print(count_matches(data))
    print(count_xmas_matches(data))