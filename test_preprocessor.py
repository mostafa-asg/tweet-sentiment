import preprocessor
import unittest


class TestPreprocessor(unittest.TestCase):

    def test_remove_tickers(self):
        input = "some text $GF some text $RT"
        expected = "some text  some text "
        actual = preprocessor.remove_tickers(input)

        self.assertEqual(expected, actual)


    def test_remove_RT(self):
        input = "RTsome RT text"
        expected = "RTsome RT text"
        actual = preprocessor.remove_RT(input)
        self.assertEqual(expected, actual)

        input = "RT some RT text RT"
        expected = "some RT text RT"
        actual = preprocessor.remove_RT(input)
        self.assertEqual(expected, actual)


    def test_remove_urls(self):
        input = "some text http://192.168.1.1:8000 some text https://a-b/a/d/r:9090 some text http://g.com"
        expected = "some text  some text  some text "
        actual = preprocessor.remove_urls(input)
        self.assertEqual(expected, actual)


    def test_remove_hashtags(self):
        input = "#important some text #AA_BB some text #123"
        expected = " some text  some text "
        actual = preprocessor.remove_hashtags(input)
        self.assertEqual(expected, actual)


    def test_remove_mentions(self):
        input = "@user1 some text @AA_BB some text @123"
        expected = " some text  some text "
        actual = preprocessor.remove_mentions(input)
        self.assertEqual(expected, actual)
    

    def test_remove_mentions(self):
        input = "&amp;&gt; some text &lt; &LT; some text &commat;"
        expected = " some text   some text "
        actual = preprocessor.remove_xml_encodings(input)
        self.assertEqual(expected, actual)


    def test_remove_extra_spaces(self):
        input = " some text   some text "
        expected = " some text some text "
        actual = preprocessor.remove_extra_spaces(input)
        self.assertEqual(expected, actual)
        

    def test_remove_emojis(self):
        input = "some text (; some text :) :D "
        expected = "some text  some text   "
        actual = preprocessor.remove_emojis(input)
        self.assertEqual(expected, actual)


    def test_remove_leftovers(self):
        input = "   some  :)3214 ; 32 () text :    "
        expected = "   some                 text      "
        actual = preprocessor.replace_leftover_with_space(input)
        self.assertEqual(expected, actual)
