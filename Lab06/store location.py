"""
file: insertion_sort.py
language: python3
author: Arthur Nunes-Harwitt
purpose: Implementation of insertion sort algorithm
"""
import insertion_sort
import tools


def compute(lst):
    original_list = lst.copy()
    sorted_list = insertion_sort.insertion_sort(lst)
    print(sorted_list)
    optimal_location = tools.median(sorted_list)
    sumdist = tools.sum_of_distances(original_list, optimal_location)
    return optimal_location, sumdist


def main():
    file = input("Enter data file:")
    while True:
        try:
            read_file = open(file, "r")
            locations_lst = tools.filereader(read_file)
            num1, num2 = compute(locations_lst)
            print(f"Optimum new store location: {num1}")
            print(f"Sum of distances to the new store: {num2}")
            read_file.close()
            break
        except FileNotFoundError:
            print("invalid file name or path, try again")


if __name__ == "__main__":
    main()
