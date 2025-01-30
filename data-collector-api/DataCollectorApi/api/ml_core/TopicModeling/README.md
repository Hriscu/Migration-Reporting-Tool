# Environment Setup

```pip install pandas pyLDAvis gensim nltk spacy wordsegment contractions requests python-dotenv```

Also, you have to download NLTK Resources:

```
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
```

You also need an API_KEY
- Create an '.env' file in TopicModeling package
- Add the API key generate from here: https://aistudio.google.com/apikey

# Code Structure
`main.py`: Initializes the application and runs the LDA topic modeling pipeline. Demo file to start the process
`lda_model.py`: Contains the logic for training and managing LDA model
`preprocessor.py`: Handles the text preprocessing tasks
`get_topic_name.py`: Uses Google Gemini API to generate human-readable topic names based on the results from `lda_model.py`
`lda_visualisation_numTopicsNR.html`: Interactive visualisation of the LDA model's topic distribution
`trainig_data_collector.py`: Util for creating a training data CSV file from multiple other files
`SavedModels package`: The package where LDA model is saved after training