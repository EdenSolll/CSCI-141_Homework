"""
PSS question 1
"""


class Box:
    def __init__(self, box_number, weight, contents):
        self.box_number = box_number
        self.weight = weight
        self.contents = contents


box1 = Box("box1", 5, [])
box2 = Box("box2", 10, [])
box3 = Box("box3", 15, [])

list_of_boxes = [box1, box2, box3]
list_of_boxes.sort(key=lambda x: x.weight, reverse=True)

items_and_weight = {"cheese": 9, "barley": 6, "anise": 2, "doughnuts": 5, "eggplant": 8}
sorted_weights = dict(
    sorted(items_and_weight.items(), key=lambda item: item[1], reverse=True)
)

for index, value in enumerate(sorted_weights.values()):
    for box in list_of_boxes:
        if box.weight >= value:
            box.contents.append(list(sorted_weights.keys())[index])
            box.weight -= value
            break

print([box.__dict__ for box in list_of_boxes])

"""
PSS question 2

If you attempt to append each item to the box in which its weight is closest to that still had space,
the method would fail. 9 is cloest to 10, of the remaining boxes 6 is cloest to 15, 2 goes to 5,
5 goes to 10, and 8 would try to go to 9 but there is no space left in any box.
"""

"""
PSS question 3

Box can either be a class or a dictionary. If it is a class, it will have attributes for the box name, weight, and contents.
If its a dictonary, it will have keys for the box name, weight, and contents. The contents will be a list of strings.

ex:
class
class Box:
    def init(self, box_number, weight, contents):
        self.box_number = box_number
        self.weight = weight
        self.contents = contents

box1 = Box("box1", 5, [])
box2 = Box("box2", 10, [])
box3 = Box("box3", 15, [])

dictionary
box1 = {"box_number": "box1", "weight": 5, "contents": []}
box2 = {"box_number": "box2", "weight": 10, "contents": []}
box3 = {"box_number": "box3", "weight": 15, "contents": []}

list_of_boxes = [box1, box2, box3]
"""

"""
PSS question 4


"""

input_file = input("Enter text file:")
with open(input_file, "r") as f:
    capacities = list(map(int, f.readline().split()))
    items = {}
    for line in f:
        item, weight_str = line.split()
        items[item] = int(weight_str)
    print(items)<D-`>
