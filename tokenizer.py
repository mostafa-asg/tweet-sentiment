from typing import List
import preprocessor

stopWords = { "i", "m", "t", "re", "ve", "me", "my", "myself", "we", "our", "ours", "ourselves", "you",
        "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it",
        "its", "itself", "they", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom",
        "this", "that", "these", "those", "am", "is", "isn", "are", "aren", "was", "were", "weren", "be", "been",
        "being", "have", "has", "had", "hadn", "having", "do", "does", "did", "didn", "doing", "a", "an", "the", "and",
        "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against",
        "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in",
        "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where",
        "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not",
        "only", "own", "same", "so", "than", "too", "very", "s", "can", "will", "won", "just", "don", "should",
        "shouldn", "now" }


def _clean(tweet: str) -> str:
    tweet = preprocessor.remove_emojis(tweet)
    tweet = preprocessor.remove_hashtags(tweet)
    tweet = preprocessor.remove_mentions(tweet)
    tweet = preprocessor.remove_RT(tweet)
    tweet = preprocessor.remove_tickers(tweet)
    tweet = preprocessor.remove_urls(tweet)
    tweet = preprocessor.remove_xml_encodings(tweet)
    tweet = preprocessor.replace_leftover_with_space(tweet)
    tweet = preprocessor.remove_extra_spaces(tweet)
    tweet = tweet.lower() 
    return tweet.strip()


def tokenize(tweet: str) -> List[str]:
    tweet = _clean(tweet)
    return [token for token in tweet.split(" ") if not token in stopWords]