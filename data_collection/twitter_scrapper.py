import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

class TwitterScraper:
    def __init__(self):
        self.auth = tweepy.OAuth1UserHandler(
            os.getenv("TWITTER_API_KEY"),
            os.getenv("TWITTER_API_SECRET"),
            os.getenv("TWITTER_ACCESS_TOKEN"),
            os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
        )
        self.api = tweepy.API(self.auth)

    def fetch_tweets(self, query, count=10):
        try:
            tweets = self.api.search_tweets(q=query, count=count)
            return [tweet.text for tweet in tweets]
        except Exception as e:
            print(f"Twitter veri çekme hatası: {e}")
            return []