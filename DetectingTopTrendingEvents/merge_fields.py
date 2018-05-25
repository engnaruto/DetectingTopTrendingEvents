import json


def merge_fields():
    count = 0
    with open("data/classifier_tweets_new.json", "w") as w:
        with open("data/classifier_tweets.json", "r") as f2:
            with open("data/preprocessed_tweets.json", "r") as f1:
                while True:
                    full_tweet = json.loads(f1.readline())
                    if full_tweet == {}:
                        break
                    tweet = json.loads(f2.readline())

                    if tweet['id'] == full_tweet['id']:
                        count += 1
                        print(count)
                        tweet['text_preproccesed'] = full_tweet['text_preproccesed']
                        json.dump(tweet, w, ensure_ascii=False)
                        print(tweet)
                        w.write("\n")
                    else:
                        break
                    print(tweet['id'], full_tweet['id'])

            print("************************************")
            with open("data/preprocessed_event_tweets.json", "r") as f1:
                while True:
                    full_tweet = json.loads(f1.readline())
                    print(tweet['id'], full_tweet['id'])
                    if tweet['id'] == full_tweet['id']:
                        count += 1
                        print(count)
                        tweet['text_preproccesed'] = full_tweet['text_preproccesed']
                        json.dump(tweet, w, ensure_ascii=False)
                        w.write("\n")
                    else:
                        break

                    line = f2.readline()
                    if line == "":
                        break
                    tweet = json.loads(line)


if __name__ == "__main__":
    merge_fields()
