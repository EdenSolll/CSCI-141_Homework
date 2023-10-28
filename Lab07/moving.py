from dataclasses import dataclass


@dataclass
class Box:
    """Class for tracking the properties of boxes"""

    box_name: str
    box_space_remaining: int
    box_contents: list = []


def filereader(input_file):
    with open(input_file, "r") as f:
        capacities = list(map(int, f.readline.split()))
        items = {}
        for line in f:
            item, weight_str = line.split()
            items[item] = int(weight_str)
    return capacities, items
