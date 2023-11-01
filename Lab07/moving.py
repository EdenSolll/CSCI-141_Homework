from dataclasses import dataclass

"""
CSCI 141 Labo7
Professor: Lima
Name: Eden Grace

This program takes an input file containing box capacities and items and their corrisponding
weight which need to packed into boxes. The program will try three different methods of packing
the boxes and then output the sucess of each method.
"""


@dataclass
class Box:
    """Class for tracking the properties of boxes"""

    box_name: str
    space_remaining: int
    contents: list


def output(dataclass_lst, original_capacities, remaining_items):
    """
    Prints the results from the packing strategy

    Arguments:
        dataclass_lst (list): List of Box objects.
        original_capacities (list): List of original capacities of boxes.
        remaining_items (dict): Dictionary of items that could not be packed.
    """
    if len(remaining_items) > 0:
        print("Unable to pack all items!")
        for i, data in enumerate(dataclass_lst):
            print(
                f"{data.box_name} of weight capacity {original_capacities[i]} contains:"
            )
            for item in data.contents:
                print(f"{item[0]} of weight {item[1]}")
        for item in remaining_items:
            print(f"{item} of weight {remaining_items[item]} got left behind.")
    else:
        print("All items successfully packed into boxes!")
        for i, data in enumerate(dataclass_lst):
            print(
                f"{data.box_name} of weight capacity {original_capacities[i]} contains:"
            )
            for item in data.contents:
                print(f"{item[0]} of weight {item[1]}")


def filereader(input_file):
    """
    Reads input from a file and initializes boxes and items.

    Arguments:
        input_file (str): Name of the input file.

    Returns:
        list: A list containing initialized boxes list_of_boxes (list) and items (dict).
    """
    with open(input_file, "r") as f:
        capacities = list(map(int, f.readline().split()))
        items = {}
        list_of_boxes = []
        for line in f:
            item, weight_str = line.split()
            items[item] = int(weight_str)
        for i, weight in enumerate(capacities):
            list_of_boxes.append(Box("Box " + str(i + 1), weight, []))
    return list_of_boxes, items


def roomiest(list_of_boxes, sorted_dict):
    """
    Packs items using the roomiest fit strategy
    Take a List of Box objects (list_of_boxes) and a dictionary of items sorted by weight (sorted_dict)
    as arguments.
    Returns a list containing the updated boxes which have had the boxes property udated with items from the sorted dictionary
    using the packing method and a dictionary of remaining items which were not able to fit into the boxes property.
    """
    packed_items = {}
    for item, weight in sorted_dict.items():
        current_roomiest_box = None
        current_roomiest_space = 0
        for box in list_of_boxes:
            if box.space_remaining >= weight:
                if box.space_remaining > current_roomiest_space:
                    current_roomiest_space = box.space_remaining
                    current_roomiest_box = box
                    packed_items[item] = weight
        if current_roomiest_box is not None:
            current_roomiest_box.contents.append((item, weight))
            current_roomiest_box.space_remaining -= weight
            packed_items[item] = weight
    remaining_items = {
        item: weight for item, weight in sorted_dict.items() if item not in packed_items
    }
    return list_of_boxes, remaining_items


def tightest_fit(list_of_boxes, sorted_dict):
    """
    Packs items using the tighest fit strategy
    Take a List of Box objects (list_of_boxes) and a dictionary of items sorted by weight (sorted_dict)
    as arguments.
    Returns a list containing the updated boxes which have had the boxes property udated with items from the sorted dictionary
    using the packing method and a dictionary of remaining items which were not able to fit into the boxes property.
    """
    packed_items = {}
    for item, weight in sorted_dict.items():
        current_tightest_box = None
        current_tightest_space = 0
        for box in list_of_boxes:
            if box.space_remaining >= weight:
                if (
                    box.space_remaining < current_tightest_space
                    or current_tightest_box is None
                ):
                    if box.space_remaining - weight >= 0:
                        current_tightest_space = box.space_remaining - weight
                        current_tightest_box = box
                        packed_items[item] = weight
        if current_tightest_box is not None:
            current_tightest_box.contents.append((item, weight))
            current_tightest_box.space_remaining -= weight
            packed_items[item] = weight
    remaining_items = {
        item: weight for item, weight in sorted_dict.items() if item not in packed_items
    }
    return list_of_boxes, remaining_items


def obaat(list_of_boxes, sorted_dict):
    """
    Packs items using the one box at a time strategy.
    Take a List of Box objects (list_of_boxes) and a dictionary of items sorted by weight (sorted_dict)
    as arguments.
    Returns a list containing the updated boxes which have had the boxes property udated with items from the sorted dictionary
    using the packing method and a dictionary of remaining items which were not able to fit into the boxes property.
    """
    packed_items = {}
    for box in list_of_boxes:
        for item, weight in sorted_dict.items():
            if box.space_remaining >= weight and item not in packed_items:
                box.contents.append((item, weight))
                box.space_remaining -= weight
                packed_items[item] = weight
    remaining_items = {
        item: weight for item, weight in sorted_dict.items() if item not in packed_items
    }
    return list_of_boxes, remaining_items


def main():
    """
    Main function for running the packing strategies.

    Calls for user input then passes it to the file reader, then for each packing method,
    the main function sorts the contents, saves the original capacities then sends the contents
    to the packing algorithms then passes the information to the text output function
    """
    filename = input("Enter your input file: ")
    # packing method 1
    boxes, stuff = filereader(filename)
    sorted_boxes = sorted(boxes, key=lambda boxes: boxes.space_remaining, reverse=True)
    sorted_dict = dict(sorted(stuff.items(), key=lambda item: item[1], reverse=True))
    original_capacities = list(sorted(map(lambda box: box.space_remaining, boxes)))
    filled_boxes_1, remaining_items_1 = roomiest(sorted_boxes, sorted_dict)
    print("Result from Greedy Strategy 1")
    output(filled_boxes_1, original_capacities, remaining_items_1)
    # packing method 2
    boxes, stuff = filereader(filename)
    sorted_boxes = sorted(boxes, key=lambda boxes: boxes.space_remaining, reverse=True)
    sorted_dict = dict(sorted(stuff.items(), key=lambda item: item[1], reverse=True))
    original_capacities = list(sorted(map(lambda box: box.space_remaining, boxes)))
    filled_boxes_2, remaining_items_2 = tightest_fit(sorted_boxes, sorted_dict)
    print("Result from Greedy Strategy 2")
    output(filled_boxes_2, original_capacities, remaining_items_2)
    # packing method 3
    boxes, stuff = filereader(filename)
    sorted_boxes = sorted(boxes, key=lambda boxes: boxes.space_remaining, reverse=True)
    sorted_dict = dict(sorted(stuff.items(), key=lambda item: item[1], reverse=True))
    original_capacities = list(sorted(map(lambda box: box.space_remaining, boxes)))
    filled_boxes_3, remaining_items_3 = obaat(sorted_boxes, sorted_dict)
    print("Result from Greedy Strategy 3")
    output(filled_boxes_3, original_capacities, remaining_items_3)


if __name__ == "__main__":
    main()
