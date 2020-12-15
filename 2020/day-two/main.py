from typing import List, Any, Tuple, Dict
from datatypes.PasswordMeta import PasswordMeta

def create_modular_passwords_from(a_list_of_passwords: List[Any]) -> List[List[Any]]:
    """
    :param a_list_of_passwords -> ``List[Any]``: a list of 'clean' passwords
    :returns result -> ``List[List[Any]]``: a list of passwords split into three components (aka modularized):
        1. lower and upper bound
        2. character
        3. password to search through
    """
    result = [
        password.split(" ") for password in a_list_of_passwords if "".join(password) != ""
    ]
    return result

def extract_from(a_modularized_nested_list_of_passwords: List[List[Any]], type_to_extract: str) -> List[Tuple[int, int]]:
    """
    extracts the upper and lower bounds for a character from a nested list of passwords.

    :param a_modularized_nested_list_of_passwords -> ``List[List[Any]]``: a list of passwords that are broken into three components (see line 3 -> create_modular_passwords_from)
    :returns result -> ``List[Tuple[int, int]]``: the extracted values from each password.
    """
    valid_types = ["bounds", "character", "password"]
    if type_to_extract not in valid_types:
        # https://stackoverflow.com/questions/256222/which-exception-should-i-raise-on-bad-illegal-argument-combinations-in-python
        raise ValueError("Invalid extraction type. Try: {0}".format(", ".join(valid_types)))
    else:
        if type_to_extract == "bounds":
            result = [
                modules_of_password[0] for modules_of_password in a_modularized_nested_list_of_passwords
            ]
        elif type_to_extract == "character":
            result = [
                modules_of_password[1] for modules_of_password in a_modularized_nested_list_of_passwords
            ]
        else:
            # guaranteed to be password
            result = [
                modules_of_password[2] for modules_of_password in a_modularized_nested_list_of_passwords
            ]

    return result

def clean_bounds_in(a_list_of_bounds: List[str]) -> List[List[str]]:
    """
    splits the bounds at "-" and returns them as a nested list of two components: lower_bound and upper_bound.

    :param a_list_of_bounds -> ``List[str]``: a list of strings representing the upper and lower bounds separated by "-"
    :returns result -> List[List[str]]: a list containing sublists filled with the lower and upper bounds
    """
    result = [
        bound.split("-") for bound in a_list_of_bounds
    ]
    return result

def clean_characters_in(a_list_of_characters: List[str]) -> List[str]:
    """
    clean the characters in the list of characters extracted from the input text.

    :param a_list_of_characters -> ``List[str]``: a list of unclean characters. Each character should be followed by a colon.
    :returns result -> ``List[str]``: a list of chars that represent the character to search for in the password.
    """
    result = [
        character.strip(":") for character in a_list_of_characters
    ]
    return result

def compile_modules_from(a_list_of_bounds: List[List[int]], a_list_of_characters: List[str], a_list_of_passwords: List[str]) -> List[PasswordMeta]:
    """
    compiles the separate modules/components of the password: upper and lower bounds, characters, and a list of passwords.

    :param a_list_of_bounds -> ``List[List[int]]``: a nested list containing upper and lower bounds for each password.
    :param a_list_of_characters -> ``List[str]``: a list of chars which represent the character to search for in each password.
    :param a_list_of_passwords -> ``List[str]``: a list of passwords.

    :returns result -> ``List[PasswordMeta]``: a list of PasswordMeta instances which represent each parsed row from the input file.
    """
    if len(a_list_of_bounds) == len(a_list_of_characters) == len(a_list_of_passwords):
        list_representation_of_input = list(zip(a_list_of_bounds, zip(a_list_of_characters, a_list_of_passwords)))
        result = [
            PasswordMeta(row[0], row[1][0], row[1][1]) for row in list_representation_of_input
        ]
        return result
    else:
        raise ValueError("Length of inputs is not equal so 'Zipping' the lists together is prone to data loss. Skipping...")


def part_one_validation_for(a_password_meta_dataclass: PasswordMeta) -> bool:
    """
    Part One validation in which we check to see that the count of the character within the
    password is between the lower and upper bounds. If so, return True else return False.

    :param a_password_meta_dataclass -> ``PasswordMeta``: a PasswordMeta dataclass containing lower and upper bound properties along 
                                                          with the character and password.

    :returns ``bool``: whether the conditions were met or not.
    """
    if not isinstance(a_password_meta_dataclass, PasswordMeta):
        raise ValueError("Invalid input, expected a PasswordMeta class instance.")
    else:
        lower_bound = a_password_meta_dataclass.lower_bound
        upper_bound = a_password_meta_dataclass.upper_bound
        character = a_password_meta_dataclass.character
        password = a_password_meta_dataclass.password
        count = 0
        for char in password:
            if char == character:
                count += 1
            else:
                pass
        if lower_bound <= count <= upper_bound:
            return True
        else:
            return False

def part_two_validation_for(a_password_meta_dataclass: PasswordMeta) -> bool:
    """
    Part Two validation in which we check to see that the character exists at either the lower_bound or upper_bound.
    If it does, return True else return False.
    
    :param a_password_meta_dataclass -> ``PasswordMeta``: a PasswordMeta dataclass instance. Same properties necessary as defined on line 94 (within part_one_validation_for()).
    :returns ``bool``: whether or not the conditions were met.
    """
    if not isinstance(a_password_meta_dataclass, PasswordMeta):
        raise ValueError("Invalid input, expected a PasswordMeta class instance.")
    else:
        lower_bound = a_password_meta_dataclass.lower_bound
        upper_bound = a_password_meta_dataclass.upper_bound
        character = a_password_meta_dataclass.character
        password = a_password_meta_dataclass.password
        if (password[lower_bound - 1] != password[upper_bound - 1]) and \
            (password[lower_bound - 1] == character or password[upper_bound - 1] == character):
            
            return True
        else:
            return False

def main():
    with open("puzzle-input.txt", "r") as f:
        file_contents = f.read()
        split_passwords_at_newline = file_contents.split("\n")
    
    modularized_passwords = create_modular_passwords_from(split_passwords_at_newline)
    extracted_bounds = clean_bounds_in(extract_from(modularized_passwords, "bounds"))
    extracted_character = clean_characters_in(extract_from(modularized_passwords, "character"))
    extracted_password = extract_from(modularized_passwords, "password")
    input_row_instances = compile_modules_from(extracted_bounds, extracted_character, extracted_password)
    
    return sum([
        part_one_validation_for(pw) for pw in input_row_instances
    ]), sum([
        part_two_validation_for(pw) for pw in input_row_instances
    ])
    



if __name__ == '__main__':
    print(main())