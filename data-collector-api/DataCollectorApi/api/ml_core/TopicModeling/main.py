import pandas as pd 
from .lda_model import LDAModel
from django.conf import settings
import pyLDAvis
import pyLDAvis.gensim as gensimvis
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DataCollectorApi.settings')
django.setup()
from api.services.RedditService import RedditService


class Main:
    def __init__(self):
        self.subreddit_name = "aliens"  
        self.reddit_service = RedditService()
        self.comments = self.reddit_service.get_comments_from_subreddit(self.subreddit_name)
        
        self.train_data = [self.reddit_service.preprocessor.preprocess_post(comment) for comment in self.comments]

        self.lda_model = LDAModel()
        self.lda_model.set_num_topics(6)

    def run(self):
        model, corpus, id2word = self.lda_model.train(self.train_data)

        vis = gensimvis.prepare(model, corpus, id2word)

        # Construiește calea către directorul Visualisations
        script_directory = os.path.dirname(__file__)  # Directorul scriptului curent
        visualisations_directory = os.path.join(script_directory, "Visualisations")  # Calea către folderul Visualisations
        if not os.path.exists(visualisations_directory):
            os.makedirs(visualisations_directory)  # Creează directorul dacă nu există

        # Calea completă pentru fișierul HTML
        html_filename = os.path.join(visualisations_directory, 'lda_visualisation_numTopics5.html')

        # Salvează vizualizarea LDA în fișierul HTML
        pyLDAvis.save_html(vis, html_filename)
        print(f"LDA visualization saved!")

        topics = model.print_topics(num_topics=6, num_words=10)  
        for topic in topics:
            print(topic)

        # Salvează modelul
        self.lda_model.model.save(self.lda_model.model_filename)
        print("Model saved.")

if __name__ == "__main__":
    main_program = Main()
    main_program.run()
