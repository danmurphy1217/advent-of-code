from typing import List
from datatypes.Passport import Passport
import re


def separate_into_passports(file_contents: str) -> List[str]:
    """
    splits the file contents on double new-lines (empty lines)

    :param file_contents -> ``str``: the contents of the file
    :returns result -> ``List[str]``: a list of un-parsed passport 
                                      data [each item represents the data for one passport].
    """
    result = file_contents.split("\n\n")
    return result


def parsed_passports_from(un_parsed_passport_list: List[str]) -> List[Passport]:
    """
    from a list of unclean passport data, attempts to extract the following data:
        byr (Birth Year)
        iyr (Issue Year)
        eyr (Expiration Year)
        hgt (Height)
        hcl (Hair Color)
        ecl (Eye Color)
        pid (Passport ID)
        cid (Country ID)
    if a value is not able to be extracted (i.e. it is missing from the passport), it's
    value is set to None [see __post_init__ in datatypes.Passport].
    """
    result = [
        unparsed_pw.split() for unparsed_pw in un_parsed_passport_list
    ]
    all_passport_credentials = []
    for passport in result:
        credentials_for_passport = {}
        for credential in passport:
            credential_and_value = credential.split(":")
            credentials_for_passport[credential_and_value[0]
                                     ] = credential_and_value[1]
        all_passport_credentials.append(Passport(**credentials_for_passport))
    return all_passport_credentials


def is_valid_part_one(a_passport_dataclass_instance: Passport) -> bool:
    """Returns whether or not a passport instance meets the conditions outlined for Problem 4 Part I."""
    # check all but cid, since that is OK to skip.
    return all(
        credential is not None for credential in
        [
            a_passport_dataclass_instance.byr,
            a_passport_dataclass_instance.eyr,
            a_passport_dataclass_instance.iyr,
            a_passport_dataclass_instance.hgt,
            a_passport_dataclass_instance.hcl,
            a_passport_dataclass_instance.ecl,
            a_passport_dataclass_instance.pid
        ]
    )


def is_valid_birth_year(birth_year: int) -> bool:
    """returns whether or not a birth year meets the criteria specified in Part II."""
    return birth_year.isnumeric() and 1920 <= int(birth_year) <= 2002


def is_valid_expiration_year(expiration_year: int) -> bool:
    """returns whether or not an expiration year meets the criteria specified in Part II."""
    return expiration_year.isnumeric() and 2020 <= int(expiration_year) <= 2030


def is_valid_issue_year(issue_year: int) -> bool:
    """returns whether or not an issue year meets the criteria specified in Part II."""
    return issue_year.isnumeric() and 2010 <= int(issue_year) <= 2020


def is_valid_height(height: str) -> bool:
    """
    returns whether or not a height meets the criteria specified in Part II.
    It is assumed that the height is followed by either 'cm' or 'in' denoting
    the metric used to calculate their height as centimeters or inches.
    """
    split_height_at_centimeters = height.split("cm")
    if len(split_height_at_centimeters) == 1:
        split_height_at_inches = height.split("in")
        return split_height_at_inches[0].isnumeric() and 59 <= int(split_height_at_inches[0]) <= 76
    else:
        return split_height_at_centimeters[0].isnumeric() and 150 <= int(split_height_at_centimeters[0]) <= 193


def is_valid_hair_color(hair_color: str) -> bool:
    """returns whether or not a hair color meets the criteria specified in Part II."""
    return re.match(r'^#[a-f|0-9]{5}', hair_color)


def is_valid_eye_color(eye_color: str) -> str:
    """returns whether or not an eye color meets the criteria specified in Part II."""
    return eye_color in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def is_valid_passport_id(passport_id: int) -> bool:
    """returns whether or not a passport ID meets the criteria specified in Part II."""
    return len(passport_id) == 9 and passport_id.isnumeric()


def is_valid_part_two(a_passport_dataclass_instance: Passport) -> bool:
    """Returns whether or not a passport instance meets the conditions outlined for Problem 4 Part II."""
    if is_valid_part_one(a_passport_dataclass_instance):
        return all([
            is_valid_birth_year(a_passport_dataclass_instance.byr),
            is_valid_expiration_year(a_passport_dataclass_instance.eyr),
            is_valid_issue_year(a_passport_dataclass_instance.iyr),
            is_valid_height(a_passport_dataclass_instance.hgt),
            is_valid_hair_color(a_passport_dataclass_instance.hcl),
            is_valid_eye_color(a_passport_dataclass_instance.ecl),
            is_valid_passport_id(a_passport_dataclass_instance.pid)
        ])
    else:
        return False


def main():
    with open("input.txt", "r") as f:
        unparsed_passports = separate_into_passports(f.read())

    print(sum([is_valid_part_one(i)
               for i in parsed_passports_from(unparsed_passports)]))
    print(sum([
        is_valid_part_two(i)
        for i in parsed_passports_from(unparsed_passports)
    ]))


if __name__ == '__main__':
    main()
