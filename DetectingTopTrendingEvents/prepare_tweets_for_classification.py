import json


def prepare_tweets():
    with open("data/classifier_tweets.json", "a") as w:
        count = 0

        with open("data/stemmed_tweets.json", "r") as f:
            print("Enter the number of tweets to escape:", end="\t")
            escape_tweets = int(input().strip())

            for line in f:
                if count < escape_tweets:
                    count += 1
                    continue

                tweet = json.loads(line)
                count += 1
                print(count)
                print("\t", tweet['text_preproccesed'], end="\t")

                input_event = input().strip()

                if input_event == "1":
                    is_event = True
                elif input_event == "x":
                    break
                else:
                    is_event = False

                classified_tweet = {'id': tweet['id'], 'is_event': is_event,
                                    'text': tweet['text'], 'text_stemmed': tweet['text_stemmed']}

                json.dump(classified_tweet, w, ensure_ascii=False)
                w.write("\n")

                if count >= 700:
                    break
        count = 0
        with open("data/stemmed_event_tweets.json", "r") as f:
            print("Enter the number of tweets to escape:", end="\t")
            escape_tweets = int(input().strip())

            for line in f:
                if count < escape_tweets:
                    count += 1
                    continue

                tweet = json.loads(line)
                count += 1
                print(count)
                print("\t", tweet['text_preproccesed'], end="\t")

                input_event = input().strip()

                if input_event == "1":
                    is_event = False
                elif input_event == "x":
                    break
                else:
                    is_event = True

                classified_tweet = {'id': tweet['id'], 'is_event': is_event,
                                    'text': tweet['text'], 'text_stemmed': tweet['text_stemmed']}

                json.dump(classified_tweet, w, ensure_ascii=False)
                w.write("\n")

                if count >= 1500:
                    break


if __name__ == '__main__':
    prepare_tweets()
