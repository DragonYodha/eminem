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
    .rap-output {
        background-color: #F0F2F6;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="title">🎤 Rap Song Generator 🎤</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subheader">Generate rap songs in the style of famous artists using Generative AI 🎶</p>',
    unsafe_allow_html=True
)

# Create prompt template for generating rap songs
rap_template = """
Write a {length}-line rap song in the style of {artist} about {theme}.
"""

rap_prompt = PromptTemplate(
    template=rap_template,
    input_variables=['length', 'artist', 'theme']
)

# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")

# Create LLM chain using the prompt template and model
rap_chain = LLMChain(llm=gemini_model, prompt=rap_prompt)

# Streamlit UI
st.markdown("### 🎨 Customize Your Rap Song")
theme = st.text_input("Enter the theme of the rap song (e.g., struggle, success, love): 🎯")
artist = st.selectbox(
    "Choose the artist's style: 🎤",
    ["Eminem", "Tupac", "Snoop Dogg", "Kendrick Lamar", "Nicki Minaj", "Custom"]
)
length = st.slider("Number of lines in the rap song: 📏", min_value=4, max_value=20, value=8, step=2)

if st.button("Generate Rap Song 🎶", key="generate_button"):
    if theme and artist and length:
        # Invoke the chain to generate the rap song
        with st.spinner("Generating your rap song... 🎤"):
            rap_song = rap_chain.run({"length": length, "artist": artist, "theme": theme})
        
        # Display the generated rap song with styling
        st.markdown("### 🎤 Your Generated Rap Song:")
        st.markdown(f'<div class="rap-output">{rap_song}</div>', unsafe_allow_html=True)
    else:
        st.error("❌ Please provide a theme, artist, and length.")