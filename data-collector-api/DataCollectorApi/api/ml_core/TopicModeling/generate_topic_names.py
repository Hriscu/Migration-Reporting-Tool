import json
import os
from .lda_model import LDAModel
from .get_topic_name import GetTopicName

lda_model = LDAModel()
get_topic_name = GetTopicName()

# Încarcă modelul existent (fără a-l reantrena)
model, corpus, id2word = lda_model.train([])

topics = model.print_topics(num_topics=6, num_words=10)

topic_names = {}

for topic_id, topic in topics:
    # Extrage cuvintele din topic
    keywords = ", ".join([word.split('*')[1].replace('"', '') for word in topic.split(" + ")])
    prompt = f"Give a short, meaningful name for a topic with these words: {keywords}. Please provide a concise title."

    # Obține numele topicului folosind modelul
    response = get_topic_name.get_content(prompt)

    if 'candidates' in response and len(response['candidates']) > 0:
        topic_title = response['candidates'][0]['content']['parts'][0]['text'].strip()
        if len(topic_title) > 50:  # Limitează la 50 de caractere
            topic_title = topic_title[:50] + "..."
    else:
        topic_title = f"Topic {topic_id}"

    topic_names[topic_id] = topic_title

# Construiește calea completă pentru fișierul topic_names.json în SavedModels
script_directory = os.path.dirname(__file__)  # Directorul scriptului curent
saved_models_directory = os.path.join(script_directory, "SavedModels")  # Calea către folderul SavedModels

# Creează directorul SavedModels dacă nu există
if not os.path.exists(saved_models_directory):
    os.makedirs(saved_models_directory)

# Calea completă pentru fișierul topic_names.json
topic_names_filename = os.path.join(saved_models_directory, "topic_names.json")

# Salvează topicurile cu numele lor în fișierul topic_names.json
with open(topic_names_filename, "w", encoding="utf-8") as f:
    json.dump(topic_names, f, indent=4, ensure_ascii=False)

print(f"Topic names saved!")
