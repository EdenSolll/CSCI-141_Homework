def readWordFile(filename: str) -> dict[str, dict[int, int]]:
    words:dict[str,dict[int,int]] = dict()
    last_word = None
    defaultDict:dict[int,int] = {year: 0 for year in range(1900, 2009)}
    with open('data/' + filename, 'r') as f:
      for line in f:
        if ',' not in line:
          last_word = line.strip()
          words[last_word] = {}
        else:
          year, count = list(map(int, line.split(',')))
          words[str(last_word)][year] = count
    for key, value in words.items():
        words[key] = defaultDict | value
    f.close()
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
            words = (readWordFile(file))
            word = input('Enter word: ')
            print(totalOccurrences(word, words))
            break
        except FileNotFoundError:
            print('File not found, try again.')

if __name__ == '__main__':
    main()
