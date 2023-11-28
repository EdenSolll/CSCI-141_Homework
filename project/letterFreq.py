import matplotlib.pyplot as plt

from wordData import readWordFile, totalOccurrences

ALPHBET = "abcdefghijklmnopqrstuvwxyz"

def letterFreq(words: dict[str, dict[int, int]]) -> str:
    letters = {a:0 for a in ALPHBET}
    for word in words:
        worduse = totalOccurrences(word, words)
        for letter in word:
            letters[letter] += worduse
    plt.bar(list(ALPHBET), list(letters.values()), color='skyblue')
    return "".join(list(map(lambda item: item[0], (sorted(letters.items(), key=lambda item: item[1], reverse=True)))))

def main():
    while True:
        try:
            file = input('Enter data file: ')
            words = readWordFile(file)
            print(letterFreq(words))
            plt.show()
            break
        except FileNotFoundError:
            print('File not found, try again.')


if __name__ == '__main__':
    main()
