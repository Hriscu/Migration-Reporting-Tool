import json
from lda_model import LDAModel
from get_topic_name import GetTopicName

lda_model = LDAModel()
get_topic_name = GetTopicName()

model, corpus, id2word = lda_model.train([])  # Nu reantrenăm, doar încărcăm modelul existent

topics = model.print_topics(num_topics=6, num_words=10)

topic_names = {}

for topic_id, topic in topics:
    keywords = ", ".join([word.split('*')[1].replace('"', '') for word in topic.split(" + ")])
    prompt = f"Give a short, meaningful name for a topic with these words: {keywords}. Please provide a concise title."

    response = get_topic_name.get_content(prompt)

    if 'candidates' in response and len(response['candidates']) > 0:
        topic_title = response['candidates'][0]['content']['parts'][0]['text'].strip()
        if len(topic_title) > 50:  
            topic_title = topic_title[:50] + "..."
    else:
        topic_title = f"Topic {topic_id}" 

    topic_names[topic_id] = topic_title

with open("SavedModels/topic_names.json", "w", encoding="utf-8") as f:
    json.dump(topic_names, f, indent=4, ensure_ascii=False)

print("Topic names saved to topic_names.json!")
