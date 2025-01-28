class SentimentModelInterface:
    """
    SentimentModelInterface class is responsible for providing an interface to analyze the sentiment of text using
    different sentiment analysis models.

    """
    def analyze(self, text):
        """
        Analyzes the sentiment of the input text using a specific sentiment analysis model.

        :param text: Text to analyze
        :return: Sentiment score derived from the analysis
        """
        pass
