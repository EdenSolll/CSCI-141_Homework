"""
file: wordSimilarity.py
description:
    This program reads a file and stores the data in a dictionary of words with a value of a dictionary representing the use of each word by year. The program then asks the user for a word
    to calulate the simialrity of. The word is passed to topSimilar which calculates the cosine similarity between the given word and every word in the dictionary, returning the five
    most simiar words.

language: python3
class: CSCI 141
professor: Lima
author: Eden Grace
"""

import numpy as np

import wordData as wd

RETURN_SIZE = 5

def topSimilar(words: dict[str, dict[int, int]], word: str) -> list[str]:
    """
    This function takes in a dictionary of words and a word, it converts the data of the word in the dictionary to a vector array. It then compares the vector
    array of the given word
    to every word in the dictionary. It does this by looping through all the words in the dictionary, converting them to a vector array, normalizing their data, calculating the dot product
    of the two vectors then calculating the cosine between the two vectors which is then stored in a dictionary relating words to their cosine similarity to the given word.
    The dictionary is then sorted by the cosine simialrity and the top 5 most similar words are returned.

    Args:
        words (dict[str, dict[int, int]]): A dictionary of words and their usage each year.
        word (str): The word to compare to the dictionary of words.

    Returns:
        list[str]: A list of the top 5 most similar words to the given word.
    """

    vecSimilarity:dict[str, int] = dict()
    vec1 = np.array(list(words[word].values()))
    unit_vector1 = vec1 / np.linalg.norm(vec1)

    for key, value in words.items():
        vec2 = np.array(list(value.values()))
        unit_vector2 = vec2 / np.linalg.norm(vec2)
        dot_product = np.dot(unit_vector1, unit_vector2)
        vecSimilarity[key] = np.cos(dot_product)

    sortedVec = dict(sorted(vecSimilarity.items(), key=lambda item: item[1]))
    return list(sortedVec.keys())[:RETURN_SIZE]

def main():
    """
    This main function prompts the user for a file and a word. The file is read using the readWordFile function from wordData.py and the word and the data from the file
    is passed to the top similar function. The top similar function calculates the similarity of each word in the file to the given word and ruturns the 5 most similar words.
    If a file is not found the user will be prompted to enter a new file name.

    Args:
        None

    Returns:
        None

    """

    while True:
        try:
            file = input('Enter data file: ')
            words = wd.readWordFile(file)
            word = input('Enter word: ')
            data = topSimilar(words, word)
            print(data)
            break
        except FileNotFoundError:
            print('File not found, try again.')

if __name__ == '__main__':
    main()
