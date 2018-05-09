import json
import re

from remove_emojis import remove_emojis


def preprocess_tweet(tweet):
    text = tweet["text"]
    if text.startswith('RT') or text.startswith('@'):
        return None
        # print(text)
    text = re.sub(r"http\S+", "", text)  # remove hyperlinks
    text = remove_emojis(text).strip()  # remove emojis
    text = re.sub(r"\s+", " ", text)

    if len(text.split()) <= 3:  # remove tweets < 3 words
        return None

    tweet["text"] = text
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
                    # print("\t", tweet["text"])
                # if count == 50:
                #     break


if __name__ == '__main__':
    preprocess_tweets()
