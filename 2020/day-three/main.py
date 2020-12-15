from datatypes.Map import Map
from math import prod

def traversal_of(map_meta: Map):
    """
    :param map_meta -> ``Map``: a Map dataclass instance which specifies the height and width of the tree map.
    :returns result: whether the next coordinate pair is a Tree or not.
    """
    row = 0 # the row we are currently accessing
    column = 0 # the column we are currently accessing
    number_of_trees = 0

    while row < map_meta.height:
        number_of_trees += is_tree(map_meta.tree_map[row][column])
        row += map_meta.rise # increment by the rise
        column = (column + map_meta.run) % map_meta.width # set equal to the run
    return number_of_trees



def is_tree(map_cell: str):
    """
    returns True if a coordinate is a tree (denoted by "#"), False otherwise.

    :param map_cell -> ``str``: a coordinate on the Map.
    :returns ``bool``: True if coordinate value is a tree else False.
    """
    return int(map_cell == "#")

def main():
    with open("input.txt", "r") as f:
        lines_in_file = [
            line.strip() for line in f
        ]
        TreeMap = Map(lines_in_file, rise=1, run=3)
    
    part_one = traversal_of(TreeMap)

    part_two = prod([
        traversal_of(Map(lines_in_file, rise=1, run=1)),
        traversal_of(Map(lines_in_file, rise=1, run=3)),
        traversal_of(Map(lines_in_file, rise=1, run=5)),
        traversal_of(Map(lines_in_file, rise=1, run=7)),
        traversal_of(Map(lines_in_file, rise=2, run=1)),
    ])
    return part_two


if __name__ == "__main__":
    print(main())