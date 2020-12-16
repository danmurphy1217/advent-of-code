from dataclasses import dataclass, field

@dataclass
class Boarding:
    first_seven_charcters: str = field(init=False)
    last_three_characters: str = field(init=False)
    encoded_boarding_pass: str

    def __post_init__(self):
        self.first_seven_charcters = self.encoded_boarding_pass[0:7]
        self.last_three_characters = self.encoded_boarding_pass[-3:]