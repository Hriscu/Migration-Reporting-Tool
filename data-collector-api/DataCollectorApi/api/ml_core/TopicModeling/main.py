import pandas as pd  
from .lda_model import LDAModel
from django.conf import settings
import pyLDAvis
import pyLDAvis.gensim as gensimvis
import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DataCollectorApi.settings')
django.setup()
from api.services.RedditService import RedditService


class Logger:
    def __init__(self, file_path):
        self.terminal = sys.stdout
        self.log_file = open(file_path, "w", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)
        self.log_file.write(message)

    def flush(self):
        self.terminal.flush()
        self.log_file.flush()

    def close(self):
        self.log_file.close()


class Main:
    def __init__(self):
        self.subreddit_name = "IWantOut"  
        self.reddit_service = RedditService()
        self.comments = self.reddit_service.get_comments_from_subreddit(self.subreddit_name)
        
        self.train_data = [self.reddit_service.preprocessor.preprocess_post(comment) for comment in self.comments]

        self.lda_model = LDAModel()
        self.lda_model.set_num_topics(6)

        script_directory = os.path.dirname(__file__)  
        saved_models_directory = os.path.join(script_directory, "SavedModels")  
        if not os.path.exists(saved_models_directory):
            os.makedirs(saved_models_directory)  

        self.log_filename = os.path.join(saved_models_directory, "lda_topics_humans.txt")

    def run(self):
        logger = Logger(self.log_filename)
        sys.stdout = logger

        try:
            model, corpus, id2word = self.lda_model.train(self.train_data)

            vis = gensimvis.prepare(model, corpus, id2word)

            visualisations_directory = os.path.join(os.path.dirname(__file__), "Visualisations")  
            if not os.path.exists(visualisations_directory):
                os.makedirs(visualisations_directory)  

            html_filename = os.path.join(visualisations_directory, 'lda_visualisation_topics_humans.html')

            pyLDAvis.save_html(vis, html_filename)
            print(f"LDA visualization saved!")

            topics = model.print_topics(num_topics=6, num_words=10)  
            for topic in topics:
                print(topic)

            self.lda_model.model.save(self.lda_model.model_filename)
            print(f"Model saved!")

        finally:
            sys.stdout = logger.terminal
            logger.close()


if __name__ == "__main__":
    main_program = Main()
    main_program.run()
