"""
file: wordData.py
description:
    This program reads a file and stores the data in a dictionary of words with a value of a dictionary representing the use of the word by year as a dictionary.
    Then the program asks the user for a word and prints out the total occurrences of that word in the file.

language: python3
class: CSCI 141
professor: Lima
author: Eden Grace
"""

from wordData import readWordFile

MIN_TREND = 1000
WORDS_TO_PRINT = 10

def trending(words: dict[str, dict[int, int]], startYr: int, endYr: int) -> list[tuple[str, float]]:
    trends:dict[str, float] = dict()
    for key, value in words.items():
        if startYr in value and endYr in value:
            if value[startYr] >= MIN_TREND and value[endYr] >= MIN_TREND:
                trends[key] = float(value[endYr]/value[startYr])
    return sorted(trends.items(), key=lambda item: item[1], reverse=True)

def main():
    while True:
        try:
            file = input('Enter data file: ')
            startYear = input('Enter starting year: ')
            endYear = input('Enter ending year: ')
            words = readWordFile(file)
            trendingWords = (trending(words, int(startYear), int(endYear)))
            print(f'The top 10 trending words from {startYear} to {endYear}: ')
            for i in range(WORDS_TO_PRINT):
                print(trendingWords[i][0])
            print(f'\nThe bottom 10 trending words from {startYear} to {endYear}: ')
            for i in range(WORDS_TO_PRINT):
                print(trendingWords[-i-1][0])
            print('\n')
            break
        except FileNotFoundError:
            print('File not found, try again.')


if __name__ == '__main__':
    main()
