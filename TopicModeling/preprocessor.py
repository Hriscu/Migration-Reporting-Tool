import re
import string

import contractions
import gensim.corpora as corpora
import gensim.utils
import spacy
from gensim.models import TfidfModel
from nltk.corpus import stopwords
from wordsegment import segment, load

# INITIALIZING NLTK RESOURCES (RUN ONLY THE FIRST TIME)
# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

load()
nlp = spacy.load("en_core_web_sm")


class Preprocessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])

    def url_elimination(self, data):
        return re.sub(r'http\S+', '', data)

    def hashtag_extraction(self, data):
        hashtags = re.findall(r'#\w+', data)
        for hashtag in hashtags:
            hashtag_text = hashtag.replace('#', '')
            split_hashtag = " ".join(segment(hashtag_text))
            data = data.replace(hashtag, split_hashtag)
        return data

    def emoji_elimination(self, data):
        emoji_pattern = re.compile(
            "["
            u"\U0001F600-\U0001F64F"  # Emoticons
            u"\U0001F300-\U0001F5FF"  # Symbols & Pictographs
            u"\U0001F680-\U0001F6FF"  # Transport & Map Symbols
            u"\U0001F1E0-\U0001F1FF"  # Flags
            u"\U00002500-\U00002BEF"  # Other symbols
            u"\U00002702-\U000027B0"  # Dingbats
            u"\U000024C2-\U0001F251"  # Enclosed characters
            "]+",
            flags=re.UNICODE,
        )
        return emoji_pattern.sub(r'', data)

    def lowercase(self, data):
        return data.lower()

    def punctuation_elimination(self, data):
        return data.translate(str.maketrans('', '', string.punctuation))

    def expand_contractions(self, data):
        return contractions.fix(data)

    def lemmatization(self, data, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
        doc = self.nlp(data)
        new_text = []
        for token in doc:
            if token.pos_ in allowed_postags:
                new_text.append(token.lemma_)
        return " ".join(new_text)

    def gen_words(self, data):
        tokens = gensim.utils.simple_preprocess(data)
        return tokens

    def bigrams_trigrams(self, data, min_count = 5, threshold = 5):
        bigram_phrases = gensim.models.Phrases(data, min_count=min_count, threshold=threshold)
        trigram_phrases = gensim.models.Phrases(bigram_phrases[data], threshold=threshold)

        bigram = gensim.models.phrases.Phraser(bigram_phrases)
        trigram = gensim.models.phrases.Phraser(trigram_phrases)

        data_bigrams = [bigram[doc] for doc in data]
        data_trigrams = [trigram[bigram[doc]] for doc in data_bigrams]

        return data_trigrams

    def remove_frequent_words(self, data_trigram):
        id2word = corpora.Dictionary(data_trigram)
        texts = data_trigram
        corpus = [id2word.doc2bow(text) for text in texts]

        tfidf = TfidfModel(corpus, id2word=id2word)
        low_value = 0.01
        words = []
        words_missing_in_tfidf = []
        for i in range(0, len(corpus)):
            bow = corpus[i]
            low_value_words = []
            tfidf_ids = [id for id, value in tfidf[bow]]
            bow_ids = [id for id, value in bow]
            low_value_words = [id for id, value in tfidf[bow] if value < low_value]
            drops = low_value_words + words_missing_in_tfidf
            for item in drops:
                words.append(id2word[item])
            words_missing_in_tfidf = [id for id in bow_ids if id not in tfidf_ids]
            new_bow = [b for b in bow if b[0] not in low_value_words and b[0] not in words_missing_in_tfidf]
            corpus[i] = new_bow
        return corpus, id2word

    def preprocessing_pipeline(self, data):
        data = self.url_elimination(data)
        data = self.hashtag_extraction(data)
        data = self.emoji_elimination(data)
        data = self.lowercase(data)
        data = self.punctuation_elimination(data)
        data = self.expand_contractions(data)

        data = self.lemmatization(data)
        tokens = self.gen_words(data)

        return tokens
