from itertools import combinations
from typing import List, Tuple


def is_empty(a_string) -> bool:
    """
    check if a string is empty.

    :param ``str`` -> a_string: the string to check.
    :return ``bool``: whether the string is empty or not.
    """
    return a_string == ""

def get_all_possible_combinations_for(a_list_of_expenses: List[int], num_combinations: int) -> List[Tuple[int]]:
    """
    returns all possible combinations for a one-dimenstional list of expenses.
    
    :param a_list_of_expense -> ``List[int]``: a one-dimenstional list of expenses
    :param num_combinations -> ``int``: the number of values to include in a combination.
    :return result -> ``List[Tuple[int*num_combinations]]``: a list of tuples of "num_combinations" length containing all possible combinations.
    """
    result = list(combinations(a_list_of_expenses, num_combinations)) 
    return result

def filter_list_for(the_correct_sum: int, list_to_filter: List[Tuple[int]]) -> List[int]:
    """
    filters a list for the correct sum.

    :param the_correct_sum -> ``int``: the correct sum to filter the list for.
    :param list_to_filter -> ``List[Tuple[int]]``: the list to filter.
    :returns result -> ``List[Tuple[int]]``: the tuple whose sum is equal to the_correct_sum.
    """
    result = [
        expense_tuple for expense_tuple in list_to_filter
        if sum(expense_tuple) == 2020
    ]
    return result

def calculate_multiple_of_values_in(a_nested_tuple):
    """
    extracts the sum of the values in a nested tuple.

    :param a_nested_tuple -> ``List[Tuple[int]]``: the nested tuple to extract values from.
    :returns result -> ``int``: the multiple of the values in a nested tuple.
    """
    result = 1
    extracted_tuple = a_nested_tuple[0]
    for expense in extracted_tuple:
        result *= expense
    return result

def main(number_per_combination: int) -> int:
    """
    returns the multiple of the tuple in a list whose sum is 2020.

    :param number_per_combination -> ``int``: the number of values to include for each combination.
    :returns result -> ``int``: the multiple of the values in a tuple whose sum is 2020.
    """

    with open("puzzle-input.txt", "r") as f:
        split_expenses_at_newline = f.read().split("\n")
        standardize_expenses = [int(expense) for expense in split_expenses_at_newline if not is_empty(expense)]
    
    all_possible_combinations_of_two = get_all_possible_combinations_for(standardize_expenses, number_per_combination)

    nested_tuple_whose_sum_is_2020 = filter_list_for(2020, all_possible_combinations_of_two)
    result = calculate_multiple_of_values_in(nested_tuple_whose_sum_is_2020)
    return result

if __name__ == "__main__":
    print(main(2))
    print(main(3))