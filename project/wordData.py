"""
File: wordData.py
Description:
    This program reads a file and stores the data in a dictionary of words with a value of a dictionary representing the use of the word by year as a dictionary.
    Then the program asks the user for a word and prints out the total occurrences of that word in the file.

Language: python3
Class: CSCI 141
Professor: Lima
Author: Eden Grace
"""

MIN_YEAR = 1900
MAX_YEAR = 2008


def readWordFile(filename: str) -> dict[str, dict[int, int]]:
    """
    This function reads a file, if a comma is not in line the program assumes it is a word and saves that word as the last used word then assigns it as a key inside
    of the words dictionary. If a comma is in the line the program assumes it is a year and a count then assigns the year as a key and the count as the value.
    Then the program assigns those key, value pairs to the last used word. Finally the program merges a default dictionary with the words dictionary
    to account for any missing year data.

    Args:
        filename (str): A name of a file as a string (data/) file directory is assumed.

    Returns:
        words dict[str, dict[int, int]]: returns a dictionary of words with a value of a dictionary relating the use of the word as years to the data of those years.
    """

    words: dict[str, dict[int, int]] = dict()
    last_word = None
    defaultDict: dict[int, int] = {year: 0 for year in range(MIN_YEAR, MAX_YEAR + 1)}
    with open("data/" + filename, "r") as f:
        for line in f:
            if "," not in line:
                if last_word:
                    words[last_word] = defaultDict | words[last_word]
                last_word = line.strip()
                words[last_word] = {}
            else:
                year, count = list(map(int, line.split(",")))
                words[str(last_word)][year] = count
    f.close()
    return words


def totalOccurrences(word: str, words: dict[str, dict[int, int]]) -> int:
    """
    This function takes a word and looks for it within the full dictionary then returning the sum of how much the word was used over all years.

    Args:
        word (str): A word as a string.
        words dict[str, dict[int, int]]: A dictionary of words with a value of a dictionary representing the use of the word each year as a dictionary.

    Returns:
        int: returns the sum of how much the word was used over all years.
    """

    if word in words:
        return sum(words[word].values())
    else:
        return 0


def main():
    """
    This main function asks the user for a file name then reads the file then asks the user for a word and prints out the total occurrences of that word over all years.
    If the file is not found the program will stay stuck in a while loop until a valid file is entered. If a word is not found the program will return 0.

    Args:
        None

    Returns:
        None
    """

    while True:
        try:
            file = input("Enter data file: ")
            words = readWordFile(file)
            word = input("Enter word: ")
            print(totalOccurrences(word, words))
            break
        except FileNotFoundError:
            print("File not found, try again.")


if __name__ == "__main__":
    main()
