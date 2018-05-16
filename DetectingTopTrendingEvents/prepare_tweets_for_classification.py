import json


def prepare_tweets():
    count = 0
    with open("data/stemmed_tweets.json", "r") as f:
        with open("data/classifier_tweets.json", "w") as w:
            for line in f:
                tweet = json.loads(line)
                count += 1
                print(count)
                print("\t", tweet['text'], end="\t")

                input_event = input().strip()

                if input_event == "1":
                    is_event = True
                else:
                    is_event = False

                classified_tweet = {'id': tweet['id'], 'is_event': is_event,
                                    'text': tweet['text'], 'text_stemmed': tweet['text_stemmed']}

                json.dump(classified_tweet, w, ensure_ascii=False)
                w.write("\n")

                if count >= 1500:
                    break


if __name__ == '__main__':
    prepare_tweets()
