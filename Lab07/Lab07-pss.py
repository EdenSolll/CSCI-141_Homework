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
sorted_weights = dict(sorted(items_and_weight.items(), key=lambda item: item[1], reverse=True))
print(items_and_weight.values())

for index, value in enumerate(sorted_weights.values()):
    for box in list_of_boxes:
        if box.weight >= value:
            box.contents.append(list(sorted_weights.keys())[index])
            box.weight -= value
            break

print([box.__dict__ for box in list_of_boxes])
