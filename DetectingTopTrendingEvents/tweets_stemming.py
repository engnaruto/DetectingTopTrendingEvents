import json

from py4j.java_gateway import JavaGateway


def initialize_stemmer():
    gateway = JavaGateway()
    stemmer = gateway.entry_point.getStemmer()
    return stemmer


def run():
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


if __name__ == '__main__':
    stemmer = initialize_stemmer()
    run()
