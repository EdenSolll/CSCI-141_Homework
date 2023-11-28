"""
File: letterFreq.py
Description:
    This program uses wordData.py to read a file and store the data in a dictionary of words with a value of a dictionary representing the use of the word by year as a dictionary.
    The program then calculates the frequency of letters in the words, prints the letters in order of most to least used, and displays a frequency distribution plot.

Language: python3
Class: CSCI 141
Professor: Lima
Author: Eden Grace
"""


import matplotlib.pyplot as plt
import wordData as wd

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def letterFreq(words: dict[str, dict[int, int]]) -> str:
    """
    Calculate the frequency of letters in a given set of words.

    Args:
        words (dict[str, dict[int, int]]): A dictionary containing words and their occurrences.

    Returns:
        str: A string representing the letters sorted by their frequency.

    """
    letters = {a: 0 for a in ALPHABET}
    for word in words:
        word_use = wd.totalOccurrences(word, words)
        for letter in word:
            letters[letter] += word_use
    plt.bar(list(ALPHABET), list(letters.values()), color="skyblue")
    return "".join(
        list(
            map(
                lambda item: item[0],
                (sorted(letters.items(), key=lambda item: item[1], reverse=True)),
            )
        )
    )


def main():
    """
    This main function prompts the user to enter a data file, reads the words from the file,
    calculates the letter frequency of the words, and displays the frequency distribution plot.
    """
    while True:
        try:
            file = input("Enter data file: ")
            words = wd.readWordFile(file)
            print(letterFreq(words))
            plt.show()
            break
        except FileNotFoundError:
            print("File not found, try again.")


if __name__ == "__main__":
    main()
