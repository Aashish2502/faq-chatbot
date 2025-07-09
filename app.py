import streamlit as st
import json
import random
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load intents
with open("data.json") as file:
    data = json.load(file)

# Load SBERT model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Precompute embeddings for patterns
pattern_texts = []
pattern_tags = []
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        pattern_texts.append(pattern)
        pattern_tags.append(intent["tag"])

pattern_embeddings = model.encode(pattern_texts)

# Streamlit UI
st.title("💬 FAQ Chatbot")
st.write("I'm Groot! Tell me what brings you here today.")

user_input = st.text_input("You:")

if user_input:
    user_embedding = model.encode([user_input])
    similarities = cosine_similarity(user_embedding, pattern_embeddings)[0]

    best_match_idx = similarities.argmax()
    best_tag = pattern_tags[best_match_idx]

    # Find the matched intent and respond
    for intent in data["intents"]:
        if intent["tag"] == best_tag:
            st.markdown(f"**Groot:** {random.choice(intent['responses'])}")
            break
