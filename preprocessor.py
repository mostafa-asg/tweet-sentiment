import re

TICKER = re.compile(r"\$\w*")
RT = re.compile(r"^RT\s+")
URL = re.compile(r"https?://[-a-zA-Z0-9+&@#\/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]")
HASHTAG = re.compile(r"#[\w_-]+")
MENTION = re.compile(r"@[\w_-]+")
XML = re.compile(r"&[a-zA-Z]*;")
SPACE = re.compile(r"\s+")
EMOJI = re.compile(r"(?:[<>]?[:;=8][\-o*']?[)\](\[dDpP/:}{@|\\]|[)\](\[dDpP/:}{@|\\][\-o*']?[:;=8][<>]?|<3)")
LEFT_OVER = re.compile("[^a-zA-Z_-]")

def remove_tickers(input: str) -> str:
    """
    Remove stock market tickers like $GE
    """
    return TICKER.sub("", input)


def remove_RT(input: str) -> str:
    """
    remove old style retweet text "RT"
    """
    return RT.sub("", input)


def remove_urls(input: str) -> str:
    return URL.sub("", input)


def remove_hashtags(input: str) -> str:
    return HASHTAG.sub("", input)


def remove_mentions(input: str) -> str:
    return MENTION.sub("", input)


def remove_xml_encodings(input: str) -> str:
    """
    Remove XML encodings like &amp;
    """
    return XML.sub("", input)


def remove_extra_spaces(input: str) -> str:
    return SPACE.sub(" ", input)


def remove_emojis(input: str) -> str:
    return EMOJI.sub("", input)


def replace_leftover_with_space(input: str) -> str:
    return LEFT_OVER.sub(" ", input)
