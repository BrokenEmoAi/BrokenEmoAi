from core.luna_engine import LunaEngine
from core.twitter_api import TwitterAPI
import random
import time

# API keys
openai_key = "YOUR_OPENAI_API_KEY"
twitter_keys = {
    "api_key": "YOUR_TWITTER_API_KEY",
    "api_secret_key": "YOUR_TWITTER_API_SECRET_KEY",
    "access_token": "YOUR_TWITTER_ACCESS_TOKEN",
    "access_token_secret": "YOUR_TWITTER_ACCESS_TOKEN_SECRET"
}

def main():
    twitter = TwitterAPI(twitter_keys)
    luna = LunaEngine(openai_key)

    while True:
        # Generate a tweet and post it
        tweet_text = luna.generate_tweet()
        twitter.post_tweet(tweet_text)

        # Randomize posting times: 3-4 posts per hour (randomized interval)
        post_interval = random.randint(900, 1200)  # Random interval between 15 to 20 minutes
        print(f"Waiting {post_interval / 60:.2f} minutes before next tweet...")
        
        time.sleep(post_interval)

if __name__ == "__main__":
    main()
