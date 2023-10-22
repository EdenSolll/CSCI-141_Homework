import re


def filereader(input_file):
    numbers = re.findall("\d+", input_file)
    return numbers


def sum_of_distances(lst, location):
    x = 0
    for a in lst:
        x += abs(location - lst[a])
    return x


def median(sortedlist):
    if len(sortedlist) % 2:
        return sortedlist[(len(sortedlist) - 1) // 2]
    else:
        return (
            sortedlist[(len(sortedlist) - 1) // 2]
            + sortedlist[((len(sortedlist) - 1) // 2) + 1]
        )
