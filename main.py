from data_collection.twitter_scraper import TwitterScraper
from nlp_analysis.sentiment_analysis import SentimentAnalyzer


def main():
    # Twitter'dan veri çek
    scraper = TwitterScraper()
    tweets = scraper.fetch_tweets("Solana meme coin", count=5)

    # Duygu analizi yap
    analyzer = SentimentAnalyzer()
    for tweet in tweets:
        sentiment = analyzer.analyze(tweet)
        print(f"Tweet: {tweet}\nSentiment: {sentiment}\n")


if __name__ == "__main__":
    main()