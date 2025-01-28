from nltk.sentiment.vader import SentimentIntensityAnalyzer

from api.ml_core.sentiment_analysis.sentiment_model_interface import SentimentModelInterface


class LexiconSentimentModel(SentimentModelInterface):
    """
    LexiconSentimentModel class is responsible for analyzing the sentiment of text using lexicon-based methods.
    """

    def __init__(self):
        """
        Initializes the LexiconSentimentModel with a pre-trained VADER sentiment analyzer.
        """
        super().__init__()
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze(self, text):
        """
        Analyzes the sentiment of the input text using lexicon-based methods.

        :param text: Text to analyze
        :return: Sentiment score computed based on lexicon values
        """
        sentiment_scores = self.analyzer.polarity_scores(text)
        return sentiment_scores
