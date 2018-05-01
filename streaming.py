# -*- coding: UTF-8 -*-
from __future__ import absolute_import, print_function

import codecs
import io
import json
import time
import sys
import datetime

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


filename = "data/data11.json"
interval = datetime.timedelta(minutes=5)



count = 1




def initialize_tweepy():
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return Stream(auth, l)


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """

    def on_status(self, status):
        global count
        # print(status)
        # json_data = json.loads(status)
        if datetime.datetime.now() > date1 + interval:
            return False
        try:
            written_data = {}
            # if "created_at" in status and "text" in status and "text" in status and "timestamp_ms" in status:
            # if "created_at" in status:
            written_data["created_at"] = str(status.created_at)
            # if "id" in json_data:
            written_data["id"] = status.id
            # if "text" in json_data:
            written_data["text"] = status.text
            # if "timestamp_ms" in json_data:
            written_data["timestamp_ms"] = status.timestamp_ms
            # json_string = json.loads(data)["created_at"]["id"]["text"]["timestamp_ms"]
            json.dump(written_data, f, ensure_ascii=False)
            f.write("\n")
            # f.write(json_string)
            print(count)
            print("\t", status.text)
            count += 1
            written_data.clear
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
        return False

    def on_exception(self, exception):
        print(exception)
        return False


if __name__ == '__main__':

    filtering_list = build_filter_list()
    print("Filtering List: " + str(filtering_list))
    print()

    stream = initialize_tweepy()

    date1 = datetime.datetime.now()

    print("Current Time: ", date1)
    print()
    print("Interval to Collect the Tweets: ", interval)
    print()

    
    with open(filename, mode="a") as f:
        while (datetime.datetime.now() <= date1 + interval):

            print()
            print("Streaming has been started...")
            print()

            try:
                stream.filter(track=filtering_list)
            except KeyboardInterrupt:
                print("***KeyboardInterrupt Happened***")
                break
            except:
                print("Unexpected error:", sys.exc_info()[0])

    date2 = datetime.datetime.now()

    print()
    print("Current Time: ", date2)
    print()
    print("Time Taken: ", date2 - date1)
    print("Total tweets: ", count - 1)
