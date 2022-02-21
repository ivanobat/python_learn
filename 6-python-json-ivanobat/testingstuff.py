import json

def load_tweets(path):
    
    data = []
    with open(path) as json_file:
        for line in json_file:
            try:
                data.append(json.loads(line))
            except:
                raise ValueError('Could not parse json')

    return data

def get_language_counts(dictionaries):
    language_count = {}
    key = 'lang'
    for item in dictionaries:
        if key in item:
            language_count[item[key]] = language_count.get(item[key],0) + 1
    #print(language_count)
    return language_count

def get_hashtag_counts(dictionaries):
    hashtag_count = {}
    key = 'entities'

    #print(dictionaries[0]['entities']['hashtags'][0]['text'])

    for rows in dictionaries:
        for tags in rows['entities']['hashtags']:
            hashtag_count[tags['text']] = hashtag_count.get(tags['text'], 0) + 1
    print(hashtag_count)
    return hashtag_count

tweets = load_tweets('tweets.json')
langs = get_language_counts(tweets)
langs = get_hashtag_counts(tweets)