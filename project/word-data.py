import matplotlib as plot

def read_word_file(filename: str) -> dict[str, dict[int, int]]:
    words = {}
    last_word = None
    with open(filename, 'r') as f:
      for line in f:
        if ',' not in line:
          last_word = line.strip()
          words[last_word] = {}
        else:
          year, count = list(map(int, line.split(',')))
          words[last_word][year] = count
    return words

def total_occurrences(word: str, words: dict) -> int:
    if word in words:
        return sum(words[word].values())
    else:
        return 0
#    return sum(words[word].values())

def main():
    words = (read_word_file("very_short.txt"))
    print(total_occurrences('airport', words))

if __name__ == '__main__':
    main()
