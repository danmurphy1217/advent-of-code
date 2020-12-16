from dataclasses import dataclass


@dataclass(frozen=True)
class Passport:
    byr: int = None # birth year
    iyr: int = None # issue year
    eyr: int = None # expiration year
    hgt: str = None # height
    hcl: str = None # hair color
    ecl: str = None # eye color
    pid: int = None # passport ID
    cid: int = None # country ID