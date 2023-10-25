def filereader(input_file):
    numbers = []
    file_contents = input_file.read().strip()
    content_list = file_contents.split("\n")
    for i in content_list:
        numbers.append(int(i.split(" ")[1]))
    return numbers


def sum_of_distances(lst, location):
    x = 0
    for a in range(len(lst)):
        x += abs(location - lst[a])
    return x


def median(sortedlist):
    if len(sortedlist) % 2 == 0:
        return (
            int(sortedlist[len(sortedlist) // 2] + sortedlist[len(sortedlist) // 2 - 1])
            / 2
        )
    else:
        return sortedlist[len(sortedlist) // 2]
