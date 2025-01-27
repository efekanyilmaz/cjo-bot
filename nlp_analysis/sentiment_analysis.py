from textblob import TextBlob

class SentimentAnalyzer:
    @staticmethod
    def analyze(text):
        analysis = TextBlob(text)
        return analysis.sentiment.polarity  # -1 (olumsuz) ile +1 (olumlu) arası