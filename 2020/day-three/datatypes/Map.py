from dataclasses import dataclass, field
from typing import List

@dataclass
class Map:
    tree_map: List[str]
    rise: int
    run: int
    width: int = field(init=False)
    height: int = field(init=False)


    def __post_init__(self):
        self.width = len(self.tree_map[0])
        self.height = len(self.tree_map)
    
    def __repr__(self):
        return f"TreeMap Width= {self.width} Height= {self.height}"