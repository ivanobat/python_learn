from tweet_data import load_tweets
from exercises import *

def test_load_tweets():
    tweets = load_tweets('tweets.json')
    assert len(tweets) == 500
    assert isinstance(tweets[0], dict)


def test_get_language_counts():
    tweets = [{'lang': 'es'}, {'lang': 'es'}, {'lang': 'uk'}]
    langs = get_language_counts(tweets)
    assert langs == {'es': 2, 'uk': 1}

    tweets = load_tweets('tweets.json')
    langs = get_language_counts(tweets)
    assert langs['es'] == 228
    assert langs['en'] == 54
    assert langs['ca'] == 10

def test_get_hashtag_counts():
    tweets = load_tweets('tweets.json')
    counts = get_hashtag_counts(tweets)
    assert counts['coronavirus'] == 2
    assert counts['Barcelona'] == 1
