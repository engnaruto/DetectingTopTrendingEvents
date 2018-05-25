import nltk
import json
import random


def load_dataset():
    tweets_list = []
    with open('data/classifier_tweets_no_duplicates.json', 'r') as f:
        for line in f:
            tweet = json.loads(line)
            if bool(tweet['is_event']):
                label = 'EVENT'
            else:
                label = 'NOT_EVENT'
            tokenized_tweet = str(tweet['text_stemmed']).split()
            words_set = set()
            for word in tokenized_tweet:
                words_set.add(word)
            tweets_list.append((words_set, label))
            # tweets.append(({tweet['text_stemmed']: 'tweet'}, label))

    random.shuffle(tweets_list)

    return tweets_list


def prepare_dictionary():
    words_dictionary = set()
    for tweet, _ in tweets:
        words = tweet
        # print(words)
        for word in words:
            words_dictionary.add(word)
    return words_dictionary


def prepare_dataset():
    tweets_features = []
    for tweet, label in tweets:
        features = {word: word in tweet for word in dictionary}
        tweets_features.append((features, label))
    return tweets_features


def train(training_tweets):
    nb_classifier = nltk.NaiveBayesClassifier.train(training_tweets)
    return nb_classifier


def test(testing_tweets):
    # for tweet, label in testing_tweets:
    #     print(classifier.classify(tweet))
    print(nltk.classify.accuracy(classifier, testing_tweets))
    print(classifier.show_most_informative_features(20))


# print(classifier.accuracy(arr))


def prepare_weka_training_file():
    with open("data/weka_input.arff", "w") as w:
        with open("data/classifier_tweets_no_duplicates.json", 'r') as f:
            w.write("@relation 'Tweet_Dataset'\n\n")
            w.write("@attribute 'words' string\n")
            w.write("@attribute 'type' {'EVENT', 'NOT_EVENT'}\n\n")
            w.write("@data\n\n")

            for line in f:
                tweet = json.loads(line)
                if bool(tweet['is_event']):
                    l = "\"" + tweet["text_stemmed"] + "\"" + " , \"EVENT\"\n"
                else:
                    l = "\"" + tweet["text_stemmed"] + "\"" + " , \"NOT_EVENT\"\n"

                w.write(l)


def clustering():
    pass
    # clusterer = nltk.cluster.GAAClusterer()


if __name__ == '__main__':
    tweets = load_dataset()
    dictionary = prepare_dictionary()
    print(dictionary)
    tweets_with_features = prepare_dataset()
    print("-----------------------------------------")

    splitting_index = 1200
    classifier = train(tweets_with_features[:splitting_index])
    test(tweets_with_features[splitting_index:])
