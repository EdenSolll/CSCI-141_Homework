import matplotlib.pyplot as plt
import wordData as wd

def letterFreq(words: dict[str, dict[int, int]]) -> str:
    letters = {a:0 for a in "abcdefghijklmnopqrstuvwxyz"}
    for word in words:
        worduse = wd.totalOccurrences(word, words)
        for letter in word:
            letters[letter] += worduse
    plt.bar(list("abcdefghijklmnopqrstuvwxyz"), list(letters.values()), color='skyblue')
    plt.show()
    return "".join(list(map(lambda item: item[0], (sorted(letters.items(), key=lambda item: item[1], reverse=True)))))

def main():
    while True:
        try:
            file = input('Enter data file: ')
            words = wd.readWordFile(file)
            print(letterFreq(words))
            break
        except FileNotFoundError:
            print('File not found, try again.')


if __name__ == '__main__':
    main()
