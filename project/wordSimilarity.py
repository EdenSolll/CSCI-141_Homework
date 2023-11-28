"""
File: wordSimilarity.py
Description:
    This program takes in a file of words and their usage each year and a word. It then calculates the cosine similarity of the given word to every word in the file.
    The top 5 most similar words are then returned. 

Language: python3
Course: CSCI-141
professor: Lima
Author: Eden Grace
"""

import wordData as wd
import numpy as np

RETURN_SIZE = 5


def topSimilar(words: dict[str, dict[int, int]], word: str) -> list[str]:
    """
    This function takes in a dictionary of words and a word. It converts the data of the word in the dictionary to a vector array. It then compares the vector
    array of the given word to every word in the dictionary. It does this by looping through all the words in the dictionary, converting them to a vector array,
    normalizing their data, calculating the dot product of the two vectors, and calculating the cosine between the two vectors, which is then stored in a dictionary
    relating words to their cosine similarity to the given word. The dictionary is then sorted by the cosine similarity, and the top 5 most similar words are returned.

    Args:
        words (dict[str, dict[int, int]]): A dictionary of words and their usage each year.
        word (str): The word to compare to the dictionary of words.

    Returns:
        list[str]: A list of the top 5 most similar words to the given word.
    """

    vecSimilarity: dict[str, int] = dict()
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
    This main function prompts the user for a file and a word. The file is read using the readWordFile function from wordData.py, and the word and the data from the file
    are passed to the topSimilar function. The topSimilar function calculates the similarity of each word in the file to the given word and returns the 5 most similar words.
    If a file is not found, the user will be prompted to enter a new file name.

    Args:
        None

    Returns:
        None
    """

    while True:
        try:
            file = input("Enter data file: ")
            words = wd.readWordFile(file)
            word = input("Enter word: ")
            print(topSimilar(words, word))
            break
        except FileNotFoundError:
            print("File not found, try again.")


if __name__ == "__main__":
    main()
