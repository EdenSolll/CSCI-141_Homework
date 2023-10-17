import insertionsort from insertion_sort as sortfun


def filereader(file):
    lst = []
    for x in file:
        if ord(x) == 32:
            lst.append(x)


def median(lst):
    sortedlist = sortfun(lst)
    if len(lst) % 2 == 0:
        return sortedlist[len(lst) // 2] + sortedlist[len(lst) // 2 - 1] / 2
    else:
        return sortedlist[len(lst) // 2]


def distances(lst, location):
    x = 0
    for a in lst:
        x += abs(location - lst[a])
    return x


def main():
    location = open("test-data.txt", "f")
    filereader(location)


if __name__ == "__main__":
    main()
