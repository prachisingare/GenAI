import streamlit as st
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# ---------------------------
# Load environment variables
# ---------------------------
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY", "")

# ---------------------------
# Streamlit App UI
# ---------------------------
st.set_page_config(page_title="Gemini Translator & Text Generator", layout="centered")
st.title("💬 Gemini AI Translator & Text Generator")

# Display info about API key status
if os.getenv("GOOGLE_API_KEY"):
    st.success("✅ Google API Key loaded successfully from .env file.")
else:
    st.warning("⚠️ Google API Key not found. Please add it to your .env file.")

# Initialize model only if API key is available
if os.getenv("GOOGLE_API_KEY"):
    model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

    # Task selection
    task = st.radio("Select Task", ["Text Generation", "Translation"])

    # Text input
    user_text = st.text_area("✍️ Enter your text", height=150)

    if task == "Translation":
        target_lang = st.selectbox(
            "🌐 Select target language",
            ["Hindi", "Marathi", "Tamil", "Telugu", "Odia", "English", "French", "Spanish"],
        )

    # Action button
    if st.button("🚀 Generate Output"):
        if not user_text.strip():
            st.warning("Please enter some text.")
        else:
            with st.spinner("Processing with Gemini model..."):
                try:
                    if task == "Text Generation":
                        response = model.invoke(user_text)
                    else:
                        # Build translation prompt using template
                        system_template = "Translate the following from English into {language}"
                        prompt_template = ChatPromptTemplate.from_messages([
                            ("system", system_template),
                            ("user", "{text}")
                        ])
                        prompt = prompt_template.invoke({"language": target_lang, "text": user_text})
                        response = model.invoke(prompt)

                    st.success("✅ Response received:")
                    st.write(response.content if hasattr(response, 'content') else response)

                except Exception as e:
                    st.error(f"⚠️ Error: {str(e)}")
else:
    st.info("👆 Please create a .env file with your GOOGLE_API_KEY before using the app.")

# Footer
st.markdown("---")
st.caption("Built with LangChain + Gemini 2.5 Flash + Streamlit 🚀")