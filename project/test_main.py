import unittest
import letterFreq
import wordData
import printedWords
import trending
from wordSimilarity import topSimilar


A_TXT_WORDS = wordData.readWordFile("a.txt")
Z_TXT_WORDS = wordData.readWordFile("z.txt")
ALL_TXT_WORDS = wordData.readWordFile("all.txt")
VERY_SHORT_TXT_WORDS = wordData.readWordFile("very_short.txt")

WORD_OCCURRENCES = {"airplane": 2487028, "alien": 5400198, "accept": 26299474}
LETTER_FREQ_STRING = "andetsrliocupgmybhvfwkxqjz"
WORDS = ((1900, 136049), (1931, 155940), (1964, 581610), (2008, 2450556))
TRENDS = (
    (1927, 1931, 0, "av"),
    (1927, 1931, -1, "acetate"),
    (1950, 1952, 0, "antibiotics"),
    (1950, 1952, -1, "atque"),
    (1966, 1975, 0, "algorithms"),
    (1966, 1975, -3, "aeroplanes"),
    (1981, 2008, 1, "authentication"),
    (1981, 2008, -2, "antisera"),
)


class TestMain(unittest.TestCase):
    def test_letterFreq(self):
        for word in WORD_OCCURRENCES:
            assert (
                wordData.totalOccurrences(word, A_TXT_WORDS) == WORD_OCCURRENCES[word]
            )
        assert letterFreq.letterFreq(A_TXT_WORDS) == LETTER_FREQ_STRING

    def test_wordSimilarity(self):
        assert topSimilar(VERY_SHORT_TXT_WORDS, "airport") == [
            "airport",
            "wandered",
            "request",
        ]
        assert topSimilar(A_TXT_WORDS, "ajf") == [
            "adj",
            "antitrust",
            "adenosine",
            "adenomas",
            "ambulatory",
        ]
        assert topSimilar(ALL_TXT_WORDS, "robot") == [
            "robot",
            "robots",
            "robotics",
            "neuroendocrine",
            "programmable",
        ]

    def test_printedWords(self):
        wordsByYearList = printedWords.printedWords(Z_TXT_WORDS)
        for idx in range(len(WORDS)):
            got = printedWords.wordsForYear(WORDS[idx][0], wordsByYearList)
            assert got == WORDS[idx][1]

    def test_trending(self):
        for idx in range(len(TRENDS)):
            trendList = trending.trending(A_TXT_WORDS, TRENDS[idx][0], TRENDS[idx][1])
            assert trendList[TRENDS[idx][2]][0] == TRENDS[idx][3]


if __name__ == "__main__":
    unittest.main()
