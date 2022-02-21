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
        
