"""
file: insertion_sort.py
language: python3
author: Arthur Nunes-Harwitt
purpose: Implementation of insertion sort algorithm
"""
import tools
import time


def quick_select(a_list, k):
    if a_list:
        pivot = a_list[len(a_list) // 2]
        smaller_list, larger_list = [], []
        count = 0
        for x in a_list:
            if x < pivot:
                smaller_list.append(x)
            elif x > pivot:
                larger_list.append(x)
            else:
                count += 1

        m = len(smaller_list)

        if m <= k < m + count:
            return pivot
        elif k < m:
            return quick_select(smaller_list, k)
        else:
            return quick_select(larger_list, k - m - count)
    else:
        return -1


def main():
    while True:
        try:
            file = input("Enter data file: ")
            read_file = open(file, "r")
            locations_lst = tools.filereader(read_file)
            starttime = time.time()
            if len(locations_lst) % 2 == 0:
                optimum = (
                    quick_select(locations_lst, len(locations_lst) // 2)
                    + (quick_select(locations_lst, len(locations_lst) // 2 - 1))
                ) / 2
            else:
                optimum = quick_select(locations_lst, len(locations_lst) // 2)
            print(f"Optimum new store location: {optimum}")
            print(
                f"Sum of distances to the new store: {tools.sum_of_distances(locations_lst, optimum)}"
            )
            print(f"Elapsed time is {time.time() - starttime} seconds.")
            read_file.close()
            break
        except FileNotFoundError:
            print("invalid file name or path, try again")


if __name__ == "__main__":
    main()
