from dataclasses import dataclass
from typing import List

@dataclass
class TweetRecord:
    tweet_tokens: List[str]
    label: int