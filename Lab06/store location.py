"""
file: insertion_sort.py
language: python3
author: Arthur Nunes-Harwitt
purpose: Implementation of insertion sort algorithm
"""
import insertion_sort
import tools
import time


def insertion_compute(lst):
    original_list = lst.copy()
    sorted_list = insertion_sort.insertion_sort(lst)
    optimal_location = tools.median(sorted_list)
    sumdist = tools.sum_of_distances(original_list, optimal_location)
    return optimal_location, sumdist


def main():
    while True:
        try:
            file = input("Enter data file: ")
            read_file = open(file, "r")
            locations_lst = tools.filereader(read_file)
            starttime = time.time()
            num1, num2 = insertion_compute(locations_lst)
            print(f"Optimum new store location: {num1}")
            print(f"Sum of distances to the new store: {num2}")
            print(f"Elapsed time is {time.time() - starttime} seconds.")
            read_file.close()
            break
        except FileNotFoundError:
            print("invalid file name or path, try again")


if __name__ == "__main__":
    main()
