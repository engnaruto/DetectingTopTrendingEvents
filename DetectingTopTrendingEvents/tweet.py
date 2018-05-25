class Tweet:

    def __init__(self, tweet):
        self.tweet = tweet

    def __hash__(self):
        return self.tweet['text_preproccesed'].__hash__()

    def __eq__(self, other):
        return self.tweet['text_preproccesed'] == other.tweet['text_preproccesed']

