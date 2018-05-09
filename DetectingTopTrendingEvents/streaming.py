# -*- coding: UTF-8 -*-
from __future__ import absolute_import, print_function

import datetime
import json
import sys

from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener

from filter_list import build_filter_list

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key = "YwEQPCKFQ17Uy8pv4yQgRfwB7"
consumer_secret = "AVdCvDK5jlaR6tZS693TzVew3rSajEcCgzNnQQRFVlNMosFYYN"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token = "444025613-IcF1FeKW6n90NwlPaDIP0gsmDVzFwOS1qDMhIKNN"
access_token_secret = "y9KxmpYON0PhLuMTC5uHamThxc0ruOJDeHawKrlKvQpDR"

filename = "data/data.json"
interval = datetime.timedelta(minutes=30)

count = 1


def initialize_tweepy():
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return Stream(auth, l)


def print_remaining_time():
    remaining = final_time - datetime.datetime.now()
    print()
    print("**********************************************************************************")
    print("Remaining Time: ", remaining)
    print("**********************************************************************************")
    print()


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """

    def on_status(self, status):
        global count

        if datetime.datetime.now() > final_time:
            return False

        try:
            written_data = {}
            written_data["created_at"] = str(status.created_at)
            written_data["timestamp_ms"] = status.timestamp_ms
            written_data["id"] = status.id
            written_data["text"] = status.text
            # written_data["retweet_count"] = status.retweet_count
            # written_data["favorite_count"] = status.favorite_count

            json.dump(written_data, f, ensure_ascii=False)
            f.write("\n")
            print(count)
            print("\t", status.text)
            count += 1
            written_data.clear()

            if count % 100 == 0:
                print_remaining_time()

        # If some error occurs
        except Exception as e:
            # Print the error
            print(e)
            # and continue
            pass
        return

    # When an error occurs
    def on_error(self, status_code):
        # Print the error code
        print('Encountered error with status code:', status_code)
        print_remaining_time()
        return False

    def on_exception(self, exception):
        print(exception)
        print_remaining_time()
        return False


if __name__ == '__main__':

    filtering_list = build_filter_list()
    print("Filtering List:")
    print(str(filtering_list))
    print()

    stream = initialize_tweepy()

    date1 = datetime.datetime.now()

    final_time = date1 + interval

    print("Current Time: ", date1)
    print()
    print("Interval to Collect the Tweets: ", interval)
    print()

    with open(filename, mode="a") as f:
        while datetime.datetime.now() <= final_time:

            print("Streaming has been started...")
            print()

            try:
                stream.filter(track=filtering_list)
            except KeyboardInterrupt:
                print("***KeyboardInterrupt Happened***")
                break
            except:
                print("Unexpected error:", sys.exc_info()[0])
                print_remaining_time()

    date2 = datetime.datetime.now()

    print()
    print("Current Time: ", date2)
    print()
    print("Time Taken: ", date2 - date1)
    print("Total Tweets: ", count - 1)
