# 🤖 BERT-Powered Chatbot Using Streamlit

An interactive chatbot built with BERT (Bidirectional Encoder Representations from Transformers) and Streamlit, designed to respond intelligently to user queries by understanding the semantic meaning of text.

# 🧠 Overview

This project demonstrates how to integrate Natural Language Processing (NLP) models into a simple web app.
The chatbot uses BERT embeddings to compare user input with predefined questions and returns the most contextually similar response.

# 🚀 Features

🔹 Context-Aware Chatbot – Understands user input beyond simple keyword matching.

🔹 Interactive Web Interface – Built with Streamlit for quick deployment and clean UI.

🔹 Predefined Question-Answer Pairs – Efficient similarity-based response system.

🔹 Custom Background Support – Uses Base64 encoding for background images.

🔹 Lightweight & Fast – Caches BERT model for performance optimization.

# 🧩 Tech Stack
Component	Description
Language	Python
Framework	Streamlit
Model	BERT (bert-base-uncased)
Libraries	Transformers, PyTorch, scikit-learn, NumPy, base64

# 📂 Project Structure

📁 bert_chatbot
├── bert_chatbot.py      # Main Streamlit app
├── requirements.txt     # Required dependencies
├── background_image.png # Optional background image
└── README.md            # Project documentation

# ⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/<your-username>/bert-chatbot.git
cd bert-chatbot

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit app
streamlit run bert_chatbot.py

# 🧮 How It Works

The chatbot converts both user input and predefined questions into BERT embeddings.

It computes cosine similarity to find the most similar question.

If the similarity score is above a threshold (e.g., 0.7), it returns the predefined response.

Otherwise, it politely says it doesn’t have an answer.

# 🖼️ Demo Screenshot

("<img width="1348" height="817" alt="BERT CHATBOT" src="https://github.com/user-attachments/assets/f94539e9-550e-4163-8883-ef6fc04f9488" />")


# 💡 Example Questions

You can try asking:

“Hello”

“What is BERT?”

“What is AI?”

“Explain Streamlit”

“How does this chatbot work?”

# 🧠 Learning Highlights

Understanding sentence embeddings using BERT.

Building an NLP interface with Streamlit.

Using cosine similarity for semantic text matching.

