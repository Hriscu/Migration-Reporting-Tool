import time
import json
from lda_model import LDAModel
from get_topic_name import GetTopicName

import pandas as pd
import pyLDAvis
import pyLDAvis.gensim as gensimvis

class Main:
    def __init__(self):
        self.new_document = "US Election results spark debate on economic policy."
        self.df = pd.read_csv("TrainingDataCollector/RawTrainingData/training_data.csv")
        self.df = self.df.dropna(subset=['text'])
        self.train_data = self.df['text'].tolist()
        self.lda_model = LDAModel()
        self.lda_model.set_num_topics(6)

    def run(self):
        # Antrenează modelul LDA
        model, corpus, id2word = self.lda_model.train(self.train_data)

        # Vizualizare LDA folosind pyLDAvis
        vis = gensimvis.prepare(model, corpus, id2word)

        # Salvează vizualizarea într-un fișier HTML
        pyLDAvis.save_html(vis, 'lda_visualisation.html')
        print("LDA visualization saved as lda_visualisation.html")

        # Afișează topic-urile
        topic_distribution = self.lda_model.get_document_topics(self.new_document)
        print(topic_distribution)
        topics = model.print_topics(num_topics=6, num_words=10)  # Ajustează numărul de topic-uri și cuvinte per topic
        for topic in topics:
            print(topic)

        # Salvează modelul
        self.lda_model.model.save(self.lda_model.model_filename)
        print("Model saved.")

if __name__ == "__main__":
    main_program = Main()
    main_program.run()
