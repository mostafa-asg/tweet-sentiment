from typing import List, AnyStr, Tuple
import json
import random
import tokenizer
from tweet_record import TweetRecord
from naive_bayes import NaiveBayesBinaryClassifier

def _extract_tweet_from_jsons(tweets: List[AnyStr]) -> List[AnyStr]:
    return [json.loads(tweet).get("text", "") for tweet in tweets]


def train_test_split(dataset: List[TweetRecord], test_size: float = 0.2) -> Tuple[List[TweetRecord], List[TweetRecord]]:
    shuffled_dataset = random.shuffle(dataset)
    train_size = int(len(dataset) * (1 - test_size))

    train_dataset = dataset[0: train_size]
    test_dataset = dataset[train_size:]

    return train_dataset, test_dataset


def main():
    positive_tweet_path = "./data/positive_tweets.json"
    negative_tweet_path = "./data/negative_tweets.json"

    positive_tweets: List[TweetRecord] = []
    negative_tweets: List[TweetRecord] = []
    full_dataset: List[TweetRecord] = []

    with open(positive_tweet_path) as f:
        tweets = _extract_tweet_from_jsons(f.readlines())
        positive_tweets = [TweetRecord(tokenizer.tokenize(tweet), 1) for tweet in tweets]


    with open(negative_tweet_path) as f:
        tweets = _extract_tweet_from_jsons(f.readlines())
        negative_tweets = [TweetRecord(tokenizer.tokenize(tweet), 0) for tweet in tweets]
    
    full_dataset = positive_tweets + negative_tweets

    # Splitting the data into training set and test set
    train_data, test_data = train_test_split(full_dataset)

    # Splitting Tweet records into features and targets (X and Y) for the classifier
    trainX = [data.tweet_tokens for data in train_data]
    trainY = [data.label for data in train_data]
    testX = [data.tweet_tokens for data in test_data]
    testY = [data.label for data in test_data]

    classifier = NaiveBayesBinaryClassifier()
    classifier.train(trainX, trainY)
    print(f"Naive Bayes Sentiment Classifier Accuracy: {classifier.score(testX, testY)}")


if __name__ == "__main__":
    main()