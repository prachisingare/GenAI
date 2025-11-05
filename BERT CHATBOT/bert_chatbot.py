import streamlit as st
from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
import base64
import numpy as np

# Function to set background
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Call background function
set_background(r"C:\Users\Prachi\Desktop\PoerBi dashboard.avif")

# Load BERT tokenizer and model (cached for performance)
@st.cache_resource
def load_bert_model():
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')
    return tokenizer, model

tokenizer, model = load_bert_model()

# Predefined questions and responses
qa_pairs = {
    "Hello": "Hi there! How can I assist you today?",
    "what is your name?": "I am a Streamlit-based chatbot powered by BERT.",
    "how are you?": "I'm just a program, but thanks for asking!",
    "What can you do?": "I can answer your questions based on predefined responses using BERT embeddings.",
    "What is Bert?": "BERT is a transformer-based model designed to understand the context of words in search queries.",
    "How does this chatbot work?": "This chatbot uses BERT embeddings to find the most similar predefined question to your input and returns the corresponding answer.",
    "Explain Streamlit?": "Streamlit is an open-source app framework for Machine Learning and Data Science teams to create web apps easily.",
    "What is AI?": "AI stands for Artificial Intelligence, which is the simulation of human intelligence processes by machines.",
    "What is Streamlit?": "Streamlit is an open-source app framework for Machine Learning and Data Science teams.",
    "How to install Streamlit?": "You can install Streamlit using pip: pip install streamlit.",
    "What is BERT?": "BERT stands for Bidirectional Encoder Representations from Transformers, a transformer-based machine learning technique for natural language processing."
}

# Function to get BERT embeddings
def get_bert_embedding(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy().reshape(1, -1)

# Precompute embeddings for predefined questions
predefined_embeddings = {q: get_bert_embedding(q) for q in qa_pairs.keys()}

# Chatbot response function
def chatbot_response(user_input):
    user_embedding = get_bert_embedding(user_input)
    similarities = {q: cosine_similarity(user_embedding, predefined_embeddings[q])[0][0] for q in qa_pairs.keys()}
    best_match = max(similarities, key=similarities.get)
    
    if similarities[best_match] > 0.7:
        return qa_pairs[best_match]
    else:
        return "I'm sorry, I don't have an answer for that."

# Streamlit Frontend
st.title("🤖 BERT-Powered Chatbot")
st.subheader("Ask me anything!")

user_input = st.text_input("You:", placeholder="Type your question here...")

if user_input:
    response = chatbot_response(user_input)
    st.text_area("Chatbot:", value=response, height=200)

st.markdown("---")
st.markdown("Developed with ❤️ using BERT + Streamlit")
