import json

from py4j.java_gateway import JavaGateway


def initialize_stemmer():
    gateway = JavaGateway()
    stemmer = gateway.entry_point.getStemmer()
    return stemmer


def stem_tweets():
    count = 0
    with open("data/preprocessed_tweets.json", 'r') as f:
        with open("data/stemmed_tweets.json", 'w') as w:
            for line in f:
                tweet = json.loads(line)
                text = tweet['text_preproccesed']
                stemmed_text = stemmer.stem(text)
                count += 1
                tweet['text_stemmed'] = stemmed_text
                json.dump(tweet, w, ensure_ascii=False)
                w.write('\n')
                print(count)


def stem_event_tweets():
    count = 0
    with open("data/preprocessed_event_tweets.json", 'r') as f:
        with open("data/stemmed_event_tweets.json", 'w') as w:
            for line in f:
                tweet = json.loads(line)
                text = tweet['text_preproccesed']
                stemmed_text = stemmer.stem(text)
                count += 1
                tweet['text_stemmed'] = stemmed_text
                json.dump(tweet, w, ensure_ascii=False)
                w.write('\n')
                print(count)


if __name__ == '__main__':
    stemmer = initialize_stemmer()
    stem_tweets()
    stem_event_tweets()
