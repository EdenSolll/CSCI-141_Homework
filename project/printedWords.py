import matplotlib.pyplot as plt
import wordData as wd

def printedWords(words: dict[str, dict[int, int]]) -> list:
    yearData:dict[int,int] = dict()
    for i in words.values():
        for x in i:
            yearData[x] = i[x] + yearData.get(x, 0)
    return list(yearData.items())

def wordsForYear(year: int, yearList: list) -> int:
    plt.plot(list(dict(yearList).keys()), list(dict(yearList).values()))
    return dict(yearList)[year]

def main():
    while True:
        try:
            file = input('Enter data file: ')
            year = input('Enter year: ')
            words = wd.readWordFile(file)
            data = printedWords(words)
            print(f'Total printed words in {year}: {wordsForYear(int(year), data)}')
            plt.show()
            break
        except FileNotFoundError:
            print('File not found, try again.')

if __name__ == '__main__':
    main()
