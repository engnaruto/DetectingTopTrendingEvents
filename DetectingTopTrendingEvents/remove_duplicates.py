import json
from tweet import Tweet


def remove_duplicates2():
    with open("data/classifier_tweets.json", 'r') as f:
        for line in f:
            tw = json.loads(line)
            t = Tweet(tw)
            for e in tweet_set:
                if e.tweet['is_event'] != tw['is_event'] and \
                        e.tweet['text_preproccesed'] == tw['text_preproccesed']:
                    print(tw)
                    break
            tweet_set.add(t)

    print(len(tweet_set))


def remove_duplicates():
    with open("data/classifier_tweets.json", 'r') as f:
        with open("data/classifier_tweets_no_duplicates.json", 'w') as w:

            for line in f:
                tw = json.loads(line)
                t = Tweet(tw)
                if t not in tweet_set:
                    tweet_set.add(t)
                    json.dump(tw, w, ensure_ascii=False)
                    w.write("\n")

    print(len(tweet_set))


def count_tweets():
    true_count = 0
    false_count = 0
    for t in tweet_set:
        if t.tweet['is_event']:
            true_count += 1
        else:
            false_count += 1

    print("True Count: ", true_count)
    print("False Count: ", false_count)


if __name__ == "__main__":
    tweet_set = set()
    remove_duplicates()
    count_tweets()
