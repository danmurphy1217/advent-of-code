from dataclasses import dataclass, field

@dataclass
class PasswordMeta:
    bounds: list
    character: str
    password: str
    lower_bound: int = field(init=False)
    upper_bound: int = field(init=False)

    def __post_init__(self):
        self.lower_bound = int(self.bounds[0])
        self.upper_bound = int(self.bounds[1])