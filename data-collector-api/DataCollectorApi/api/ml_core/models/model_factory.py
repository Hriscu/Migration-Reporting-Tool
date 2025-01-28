from api.ml_core.sentiment_analysis.lexicon_sentiment_model import LexiconSentimentModel
from api.ml_core.sentiment_analysis.bert_sentiment_model import BertSentimentModel
#, LDATopicModel, BERTopicModel


class ModelFactory:
    """
    Factory to create instances of various models, categorized by type (e.g., sentiment, topic).
    """

    _registry = {
        'sentiment': {
            'lexicon': lambda: LexiconSentimentModel(),
            'bert': lambda: BertSentimentModel()
        },
        'topic': {
            'lda': 0,#lambda: LDATopicModel(),
            'bert': 0#lambda: BERTopicModel()
        }
    }

    @staticmethod
    def create_model(category, model_type):
        """
        Creates and returns a model instance based on the category and type.

        :param category: Model category (e.g., 'sentiment', 'topic')
        :param model_type: Specific model type within the category
        :return: An instance of the specified model
        :raises ValueError: If the category or model type is unknown
        """
        if category not in ModelFactory._registry:
            raise ValueError(f"Unknown category: {category}")
        if model_type not in ModelFactory._registry[category]:
            raise ValueError(f"Unknown model type '{model_type}' in category '{category}'")

        return ModelFactory._registry[category][model_type]()

