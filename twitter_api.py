import tweepy

class TwitterAPI:
    def __init__(self, keys):
        auth = tweepy.OAuthHandler(keys["api_key"], keys["api_secret_key"])
        auth.set_access_token(keys["access_token"], keys["access_token_secret"])
        self.api = tweepy.API(auth)

    def post_tweet(self, tweet_text):
        try:
            self.api.update_status(tweet_text)
            print(f"Tweet posted: {tweet_text}")
        except tweepy.TweepError as e:
            print(f"Error: {e}")
