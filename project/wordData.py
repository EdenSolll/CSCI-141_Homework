def readWordFile(filename: str) -> dict[str, dict[int, int]]:
    words:dict[str,dict[int,int]] = dict()
    last_word = None
    with open(filename, 'r') as f:
      for line in f:
        if ',' not in line:
          last_word = line.strip()
          words[last_word] = {}
        else:
          year, count = list(map(int, line.split(',')))
          words[str(last_word)][year] = count
    return words

def totalOccurrences(word: str, words: dict) -> int:
    if word in words:
        return sum(words[word].values())
    else:
        return 0

def main():
    while True:
        try:
            file = input('Enter data file: ')
            words = (read_word_file(file))
            word = input('Enter word: ')
            print(total_occurrences(word, words))
            break
        except FileNotFoundError:
            print('File not found, try again.')

if __name__ == '__main__':
    main()
