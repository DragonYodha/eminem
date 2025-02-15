from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import PromptTemplate
from langchain import LLMChain
import streamlit as st
import os

# Set your Google API key using Streamlit secrets
os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']

# Streamlit App Title with Emojis and Colors
st.markdown(
    """
    <style>
    .title {
        font-size: 40px !important;
        color: #FF4B4B !important;
        text-align: center;
    }
    .subheader {
        font-size: 20px !important;
        color: #1F51FF !important;
        text-align: center;
    }
    .lyrics-output {
        background-color: #F0F2F6;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        white-space: pre-line; /* Preserve line breaks in lyrics */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="title">🎤 Rap Lyrics Generator - VK 🎤</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subheader">Generate 🔥 rap lyrics in the style of your favorite artists using AI 🎶</p>',
    unsafe_allow_html=True
)

# Create prompt template for generating rap lyrics
lyrics_template = """
Write {length} lines of rap lyrics in the style of {artist} about {theme}.
"""

lyrics_prompt = PromptTemplate(
    template=lyrics_template,
    input_variables=['length', 'artist', 'theme']
)

# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")

# Create LLM chain using the prompt template and model
lyrics_chain = LLMChain(llm=gemini_model, prompt=lyrics_prompt)

# Streamlit UI
st.markdown("### 🎨 Customize Your Rap Lyrics")
theme = st.text_input("Enter the theme of the rap lyrics (e.g., struggle, success, love): 🎯")
artist = st.selectbox(
    "Choose the artist's style: 🎤",
    ["Eminem", "Tupac", "Snoop Dogg", "Kendrick Lamar", "Nicki Minaj", "Custom"]
)
length = st.slider("Number of lines in the rap lyrics: 📏", min_value=4, max_value=20, value=8, step=2)

if st.button("Generate Rap Lyrics 🎶", key="generate_button"):
    if theme and artist and length:
        # Invoke the chain to generate the rap lyrics
        with st.spinner("Generating your rap lyrics... 🎤"):
            rap_lyrics = lyrics_chain.run({"length": length, "artist": artist, "theme": theme})
        
        # Display the generated rap lyrics with styling
        st.markdown("### 🎤 Your Generated Rap Lyrics:")
        st.markdown(f'<div class="lyrics-output">{rap_lyrics}</div>', unsafe_allow_html=True)
    else:
        st.error("❌ Please provide a theme, artist, and length.")
