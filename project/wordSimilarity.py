import numpy as np
import wordData as wd
import math as math

def topSimilar(words: dict[str, dict[int, int]], word: str) -> list[str]:
    vecSimilarity:dict[str, int] = dict()
    vec1 = np.array(list(words[word].values()))
    for key, value in words.items():
        vec2 = np.array(list(value.values()))
        unit_vector1 = vec1 / np.linalg.norm(vec1)
        unit_vector2 = vec2 / np.linalg.norm(vec2)
        dot_product = np.dot(unit_vector1, unit_vector2)
        vecSimilarity[key] = np.cos(dot_product)
    sortedVec = dict(sorted(vecSimilarity.items(), key=lambda item: item[1]))
    return list(sortedVec.keys())[:5]

def main():
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
