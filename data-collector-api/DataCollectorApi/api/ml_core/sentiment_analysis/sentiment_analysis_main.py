from api.ml_core.models.model_factory import ModelFactory

import nltk

if __name__ == '__main__':
    # Ensure VADER lexicon data is downloaded
    nltk.download('vader_lexicon')

    # Example usage
    texts = ["He went to the park and had a great time!",
             "She failed her exam and felt miserable.",
             "I am going outside."]

    # Lexicon-based analysis
    lexicon_model = ModelFactory.create_model('sentiment', 'lexicon')
    print(lexicon_model.analyze(texts[0])) # compound provides an overall sentiment score from -1 (most negative) to +1 (most positive).

    # Deep learning analysis
    bert_model = ModelFactory.create_model('sentiment', 'bert')
    for text in texts:
        print(bert_model.analyze(text))
