from dataclasses import dataclass
from typing import Any, ClassVar


@dataclass
class Box:
    """Class for tracking the properties of boxes"""

    box_name: str
    space_remaining: int
    contents: list


def output(dataclass_lst, original_capacities, remaining_items):
    if len(remaining_items) > 0:
        print("Unable to pack all items!")
    for i, data in enumerate(dataclass_lst):
        print(f"{data.box_name} of weight capacity {original_capacities[i]} contains:")
        print(f"{data.contents[i]} of weight {data.contents}")
    for item in remaining_items:
        print(f"{item} of weight {item.value} got left behind.")
    else:
        print("All items successfully packed into boxes!")
        for i, data in enumerate(dataclass_lst):
            print(f"{data} of weight capacity {original_capacities[i]} contains:")
            print(f"{data.contents} of weight {data.contents}")


def filereader(input_file):
    with open(input_file, "r") as f:
        capacities = list(map(int, f.readline().split()))
        items = {}
        list_of_boxes = []
        for line in f:
            item, weight_str = line.split()
            items[item] = int(weight_str)
        for i, weight in enumerate(capacities):
            list_of_boxes.append(Box("box" + str(i + 1), weight, []))
    return list_of_boxes, items


def roomiest(list_of_boxes, sorted_weights):
    return list_of_boxes, sorted_weights


def tightest_fit(list_of_boxes, sorted_dict):
    for index, value in enumerate(sorted_dict.values()):
        current_tightest_box = None
        current_tightest_fit = float("inf")  # Initialize with a large value

        for box in list_of_boxes:
            if box.space_remaining >= value:
                if (box.space_remaining - value) < current_tightest_fit:
                    current_tightest_fit = box.space_remaining - value
                    current_tightest_box = box

        if current_tightest_box is not None:
            current_tightest_box.contents.append(value)
            current_tightest_box.space_remaining -= value


def obaat(list_of_boxes, sorted_weights):
    for box in list_of_boxes:
        for index, value in enumerate(sorted_weights.values()):
            if box.weight >= value:
                box.contents.append(list(sorted_weights.keys())[index])
                sorted_weights.pop(sorted_weights[index])
                box.weight -= value
                break
    return list_of_boxes, sorted_weights


def main():
    filename = input("Enter your input file: ")
    boxes, stuff = filereader(filename)
    sorted_boxes = sorted(boxes, key=lambda boxes: boxes.space_remaining, reverse=True)
    sorted_dict = dict(sorted(stuff.items(), key=lambda item: item[1]))
    print(sorted_dict)
    original_capacities = list(sorted(map(lambda box: box.space_remaining, boxes)))
    filled_boxes_1, remaining_items_1 = tightest_fit(sorted_boxes, sorted_dict)

    # filled_boxes_2, remaining_items_2 = tightest_fit(sorted_boxes, sorted_dict)

    # filled_boxes_3, remaining_items_3 = obaat(sorted_boxes, sorted_dict)
    print("Result from Greedy Strategy 1")
    print(filled_boxes_1)
    output(filled_boxes_1, original_capacities, remaining_items_1)


if __name__ == "__main__":
    main()
