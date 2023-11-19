import matplotlib.pyplot as plt
import wordData as wd


def trending(words: dict[str, dict[int, int]], startYr: int, endYr: int) -> list[tuple[int, int]]:
    words.keys()
    startYr += 1
    endYr += 1

    print(list(words.items()))


def main():
    while True:
        try:
            file = input('Enter data file: ')
            year = input('Enter year: ')
            words = wd.readWordFile(file)
            trending(words, int(year), int(year))
            break
        except FileNotFoundError:
            print('File not found, try again.')


if __name__ == '__main__':
    main()
