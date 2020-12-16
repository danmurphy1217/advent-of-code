from io import TextIOWrapper
from typing import List
from datatypes.Boarding import Boarding
import numpy as np


def clean_contents_of(a_file: TextIOWrapper) -> List[str]:
    """
    strip newlines and spaces from each line in a textIOWrapper.

    :param a_file -> ``TextIOWrapper``: a text file opened in read mode.
    :returns result -> ``List[str]``: a list of each line in the file stripped of any newlines or blank spaces.
    """
    result = [line.strip() for line in a_file]
    return result


def set_dataclasses_for(encoded_boarding_passes: List[str]) -> List[Boarding]:
    """
    sets dataclass instances for each encoded boarding pass.

    :param encoded_boarding_passes -> ``List[str]``: encorded characters from each line of the input.
    """
    return [
        Boarding(encoded_boarding_pass) for encoded_boarding_pass in encoded_boarding_passes
    ]


def traverse_boarding_pass_credentials(traversal_type: str, boarding_pass: Boarding, low: int, high: int) -> int:
    """
    uses a binary search-like implementation to traverse the credentials of a passport
    and return the row and column of an individuals seat.

    :param traversal_type -> ``str``: takes either "row" or "column", in reference to the portion of the
                            passport credentials that should be retrieved.
    :param boarding_pass -> ``Boarding``: a dataclass instance with first_seven_characters and 
                                          list_three_characters attributes.
    :param low -> ``int``: the initial minimum value for the binary search
    :param high -> ``int``: the initial maximum value for the binary search.

    :returns result -> ``int``: the row or the column value.
    """
    result = ""
    lower_bound = "F" if traversal_type == "row" else "L"

    if not (isinstance(traversal_type, str) and (traversal_type in ["row", "column"])):
        raise ValueError("Incorrect input. Try 'row' or 'column'")
    else:
        if traversal_type == "row":
            values_to_traverse = boarding_pass.first_seven_charcters
        else:
            values_to_traverse = boarding_pass.last_three_characters
            if values_to_traverse == "RRR":
                return 7
            elif values_to_traverse == "LLL":
                return 0

    for char in values_to_traverse:

        if char == lower_bound:
            # take lower half
            high = (low + high) // 2
            result = high
        else:
            # take upper half
            low = (low + high) // 2
            result = low
    return int(result)


def build_seat_id_for(a_seat_row: str, a_seat_col: str) -> int:
    """
    build the unique value for a seat ID with the outlined equation in Question 5.
    :param a_seat_row -> ``int``: the value representing the row of a seat.
    :param a_seat_col -> ``int``: the value representing the column of a seat.

    :returns result -> ``int``: the unique ID of a seat.
    """
    result = a_seat_row * 8 + a_seat_col
    return int(result)


def main():
    with open("input.txt", "r") as f:
        clean_file_lines = clean_contents_of(f)
    boarding_passes = set_dataclasses_for(clean_file_lines)

    seat_ids = []
    for boarding_pass in boarding_passes:
        seat_row = traverse_boarding_pass_credentials(
            "row", boarding_pass, 0, 127)
        seat_col = traverse_boarding_pass_credentials(
            "column", boarding_pass, 0, 7)
        seat_ids.append(build_seat_id_for(seat_row, seat_col))

    part_one = max(seat_ids)

    # TODO: Part Two


if __name__ == "__main__":
    main()
