import unittest
import tokenizer

class TestTokenizer(unittest.TestCase):

    def test_tokenize(self):
        tweet = "@Lamb2ja Hey James! How odd :/ Please call our Contact Centre on 02392441234 and we will be able to assist you :) Many thanks!"
        tokens = tokenizer.tokenize(tweet)
        expected_tokens = ['hey', 'james', 'odd', 'please', 'call', 'contact', 'centre', 'able', 'assist', 'many', 'thanks'] 
        self.assertEqual(expected_tokens, tokens)
