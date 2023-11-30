from tests.testWordSimilarity import testAll
from tests.testLetterFreq import testA
from tests.testPrintedWords import testZ
from tests.testTrending import testA2


def main() -> None:
    testAll()
    testA()
    testZ()
    testA2()


if __name__ == "__main__":
    main()
