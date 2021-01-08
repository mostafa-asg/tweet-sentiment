import unittest
from naive_bayes import NaiveBayesBinaryClassifier


class TestNaiveBayesBinaryClassifier(unittest.TestCase):


    def test_word_frequencies(self):
        c = NaiveBayesBinaryClassifier()

        tweets = [
            ["A", "B", "C", "B", "C", "C"],
            ["A", "E", "D", "C"],
            ["A", "B"],
        ]

        lables = [
            1,
            0,
            1
        ]

        counter = c._build_word_frequencies(tweets, lables)
        
        self.assertEqual((1, 2), counter["A"])
        self.assertEqual((0, 3), counter["B"])
        self.assertEqual((1, 3), counter["C"])
        self.assertEqual((1, 0), counter["D"])
        self.assertEqual((1, 0), counter["E"])

