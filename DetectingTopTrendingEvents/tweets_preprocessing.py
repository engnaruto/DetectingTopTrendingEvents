import json
import csv
import re

from remove_emojis import remove_emojis


def preprocess_tweet(tweet):
    text = tweet["text"]
    if text.startswith('RT') or text.startswith('@'):
        return None
        # print(text)
    text = re.sub(r"http\S+", "", text)  # remove hyperlinks
    text = re.sub(r"bit\S+", "", text)  # remove hyperlinks
    text = re.sub(r"pic\S+", "", text)  # remove hyperlinks
    text = re.sub(r"almasryalyoum\S+", "", text)  # remove hyperlinks
    text = re.sub(r"youtube\S+", "", text)  # remove hyperlinks
    text = re.sub(r"ow\S+", "", text)  # remove hyperlinks
    text = re.sub(r"[.:~!#@$%٪^&*()\-_=+\[\]{\}\"';/؟…?\n\t<>,،»«؛|﴿﴾“”`┈•✦ﷺ]", " ", text)
    text = re.sub(r"[٠-٩]+", " ", text)  # remove arabic digits
    text = re.sub(r"\d+", " ", text)  # remove english digits
    text = remove_emojis(text)  # remove emojis
    text = re.sub(r"\s+", " ", text)
    text = text.strip()

    if len(text.split()) <= 3:  # remove tweets < 3 words
        return None

    tweet["text_preproccesed"] = text
    return tweet


def preprocess_tweets():
    count = 0
    with open("data/data.json", "r") as f:
        with open("data/preprocessed_tweets.json", "w") as w:
            for line in f:
                tweet = json.loads(line)

                tweet = preprocess_tweet(tweet)
                if tweet is not None:
                    json.dump(tweet, w, ensure_ascii=False)
                    w.write("\n")
                    count += 1
                    print(count)
                    print("\t", tweet['text_preproccesed'])
                    # print("\t", tweet["text"])
                # if count == 5000:
                #     break


def preprocess_event_tweets():
    count = 0
    with open("data/event_data.csv", "r") as f:
        with open("data/preprocessed_event_tweets.json", "w") as w:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                if row[0] == "username":
                    continue

                tweet = {"created_at": row[1], "timestamp_ms": "0000000000000", "id": row[-2], "text": row[4]}

                tweet = preprocess_tweet(tweet)

                if tweet is not None:
                    json.dump(tweet, w, ensure_ascii=False)
                    w.write("\n")
                    count += 1
                    print(count)
                    print("\t", tweet['text_preproccesed'])


if __name__ == '__main__':
    preprocess_tweets()
    preprocess_event_tweets()
