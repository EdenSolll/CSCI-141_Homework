"""
File: printedWords.py
Description:
    This program uses wordData.py to read a file and store the data in a dictionary of words with a value of a dictionary representing the use of the word by year as a dictionary.
    Then the program asks the user for a year and prints out the total count of printed words for that year. 
    The program also displays a plot of the total count of printed words for each year.

Language: python3
Class: CSCI 141
Professor: Lima
Author: Eden Grace
"""


import matplotlib.pyplot as plt

import wordData as wd


def printedWords(words: dict[str, dict[int, int]]) -> list[tuple[int, int]]:
    """
    Calculates the total count of printed words for each year.

    Args:
        words (dict[str, dict[int, int]]): A dictionary containing word counts for each year.

    Returns:
        list[tuple[int, int]]: A list of tuples containing the year and the total count of printed words for that year.
    """
    yearData: dict[int, int] = dict()
    for i in words.values():
        for x in i:
            yearData[x] = i[x] + yearData.get(x, 0)
    return list(yearData.items())


def wordsForYear(year: int, yearList: list[tuple[int, int]]) -> int:
    """
    Returns the number of printed words for a given year.

    Args:
        year (int): The year for which to retrieve the number of printed words.
        yearList (list[tuple[int, int]]): A list of tuples representing the year and the corresponding number of printed words.

    Returns:
        int: The number of printed words for the given year.
    """
    plt.plot(list(dict(yearList).keys()), list(dict(yearList).values()))
    return dict(yearList)[year]


def main():
    """
    This main function prompts the user to enter a data file and a year. It reads the words from the file,
    calculates the total printed words for the given year, and displays the result. It also shows a plot
    of the data.

    Raises:
        FileNotFoundError: If the specified data file is not found.

    """
    while True:
        try:
            file = input("Enter data file: ")
            words = wd.readWordFile(file)
            year = input("Enter year: ")
            data = printedWords(words)
            print(f"Total printed words in {year}: {wordsForYear(int(year), data)}")
            plt.show()
            break
        except FileNotFoundError:
            print("File not found, try again.")


if __name__ == "__main__":
    main()
