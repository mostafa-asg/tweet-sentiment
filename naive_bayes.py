from typing import List, Dict, Tuple
from collections import Counter
import math

class NaiveBayesBinaryClassifier:


    def __init__(self):
        self.vocabulary: Dict[str, float] = dict()
        self.log_prior: float = 0


    def _build_word_frequencies(self, tweets: List[List[str]], targets: List[int]) -> Dict[str, Tuple[int, int]]:
        """
        Returns frequency table of word to tuple[negative (0) count , positive (1) count]
        """
        zipped = list(zip(tweets, targets))
        negative_tweets = [item for item in zipped if item[1] == 0]        
        positive_tweets = [item for item in zipped if item[1] == 1]

        negative_words = [word for item in negative_tweets for word in item[0]]
        positive_words = [word for item in positive_tweets for word in item[0]]

        negative_words_counter = Counter(negative_words)
        positive_words_counter = Counter(positive_words)

        result = { word: (negative_words_counter[word], 0) for word in negative_words_counter.keys() }
        for word in positive_words_counter.keys():
            negative_count, positive_count = result.get(word, (0,0))
            result[word] = (negative_count, positive_words_counter[word])

        return result


    def _computeLogLambdas(self, freq: Dict[str, Tuple[int, int]]) -> Dict[str, float]:
        all_positives_count = sum(map(lambda t: t[1], freq.values()))
        all_negatives_count = sum(map(lambda t: t[0], freq.values()))
        total_words_count = len(freq)

        result: dict[str, float] = dict()
        for word in freq.keys():
            negative, positive = freq[word]
            pos_prob = (positive + 1.0) / (all_positives_count + total_words_count)
            neg_prob = (negative + 1.0) / (all_negatives_count + total_words_count)
            result[word] = math.log(pos_prob / neg_prob)

        return result

    
    def _predict_likelihood(self, tokens: List[str]) -> float:
        return self.log_prior + sum(map(lambda word: self.vocabulary.get(word, 0.0), tokens))

    
    def predicate_label(self, tokens: List[str]) -> int:
        return 1 if self._predict_likelihood(tokens) >= 0 else 0
    
    
    def train(self, trainX: List[List[str]], trainY: List[int]):
        assert len(trainX) == len(trainY), "Size of X doesn't match size of Y"        
        
        counter = Counter(trainY)
        positive_count = counter[1]
        negative_count = counter[0]

        self.vocabulary = self._computeLogLambdas(self._build_word_frequencies(trainX, trainY))
        self.log_prior = math.log(positive_count / negative_count)


    def score(self, testX: List[List[str]], testY: List[int]) -> float:
        assert len(testX) == len(testY), "Size of X doesn't match size of Y"

        predictY = map(lambda tokens: self.predicate_label(tokens), testX)
        correct_answers = Counter(map(lambda t: t[0] == t[1], zip(testY, predictY)))[True]
        return correct_answers / len(testY)