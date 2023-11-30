"""
Project: TextStats
Task Two: Number of Printed Words

This is a test program that students can use to verify that they are
able to compute the correct total number of printed words
based on the input file 'z.txt'.

Author: Sean Strout (sps@cs.rit.edu)
Author: Aaron Deever atd@cs.rit.edu
Author: Eduardo Lima (lima@cs.rit.edu)
"""

__author__ = "sps"

import wordData  # readWordFile
import printedWords  # printedWords, wordsForYear


def testZ():
    """
    Test function for 'z.txt'.
    :return: None
    :return type: None
    """

    # Expected results from z.txt
    WORDS = ((1900, 136049), (1931, 155940), (1964, 581610), (2008, 2450556))

    # read in the words
    words = wordData.readWordFile("z.txt")

    # get the list of words for each year
    wordsByYearList = printedWords.printedWords(words)

    for idx in range(len(WORDS)):
        got = printedWords.wordsForYear(WORDS[idx][0], wordsByYearList)
        assert got == WORDS[idx][1]


if __name__ == "__main__":
    testZ()
