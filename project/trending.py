"""
File: trending.py
Description:
    This program uses wordData.py to read a file and store the data in a dictionary of words with a value of a dictionary representing the use of the word by year as a dictionary.
    Then the program asks the user for a starting year and an ending year and prints out the top 10 trending words and the bottom 10 trending words between those years. 
    Trending words are words that have a usage of at least 1000 in both the starting year and the ending year. The trending words are sorted by the ratio of the ending year 
    usage to the starting year usage. 

Language: python3
Class: CSCI 141
Professor: Lima
Author: Eden Grace
"""

import wordData as wd

MIN_TREND = 1000
WORDS_TO_PRINT = 10


def trending(
    words: dict[str, dict[int, int]], startYr: int, endYr: int
) -> list[tuple[str, float]]:
    """
    Calculate the trending score for each word in the given dictionary of words.

    Parameters:
    - words (dict[str, dict[int, int]]): A dictionary containing words as keys and their frequency over the years as values.
    - startYr (int): The starting year for calculating the trend.
    - endYr (int): The ending year for calculating the trend.

    Returns:
    - list[tuple[str, float]]: A list of tuples containing the word and its trending score, sorted in descending order of the score.
    """
    trends: dict[str, float] = dict()
    for key, value in words.items():
        if startYr in value and endYr in value:
            if value[startYr] >= MIN_TREND and value[endYr] >= MIN_TREND:
                trends[key] = float(value[endYr] / value[startYr])
    return sorted(trends.items(), key=lambda item: item[1], reverse=True)


def main():
    """
    This main function prompts the user to enter a data file, starting year, and ending year.
    It reads the word file, calculates the trending words within the specified year range,
    and prints the top and bottom 10 trending words.
    """
    while True:
        try:
            file = input("Enter data file: ")
            startYear = input("Enter starting year: ")
            endYear = input("Enter ending year: ")
            words = wd.readWordFile(file)
            trendingWords = trending(words, int(startYear), int(endYear))
            print(f"The top 10 trending words from {startYear} to {endYear}: ")
            for i in range(WORDS_TO_PRINT):
                print(trendingWords[i][0])
            print(f"\nThe bottom 10 trending words from {startYear} to {endYear}: ")
            for i in range(WORDS_TO_PRINT):
                print(trendingWords[-i - 1][0])
            print("\n")
            break
        except FileNotFoundError:
            print("File not found, try again.")


if __name__ == "__main__":
    main()
