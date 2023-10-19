import re


def filereader(input_file):
    with open(input_file, "r") as file:
        text = file.read()
        numbers = re.findall("\d+", text)
        return numbers


def distances(lst, location):
    x = 0
    for a in lst:
        x += abs(location - lst[a])
    return x


def med(sortedlist):
    if len(sortedlist) % 2:
        return sortedlist[(len(sortedlist) - 1) // 2]
    else:
        return (
            sortedlist[(len(sortedlist) - 1) // 2]
            + sortedlist[((len(sortedlist) - 1) // 2) + 1]
        ) / 2
