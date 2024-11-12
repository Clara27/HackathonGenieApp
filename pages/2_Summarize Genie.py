import streamlit as st
from docx import Document
import PyPDF2
import google.generativeai as genai
from google.generativeai import GenerativeModel
import os
from gtts import gTTS  # Importing gTTS for Text-to-Speech conversion
import tempfile

# Custom CSS to change the background color
st.markdown(
"""
    <style>
    /* Main background and text colors */
    .stApp {
        background: linear-gradient(135deg, #81334C, #81334C);
        color: #ffffff;
    }

    /* Headings */
    h1, h2, h3 {
        color: #ffffff !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    /* Paragraphs */
    p {
        font-size: 1.1em;
        line-height: 1.6;
    }

    /* Links */
    a {
        color: #FFB6C1 !important;
        text-decoration: none;
        transition: all 0.3s ease;
    }

    a:hover {
        color: #FFC0CB !important;
        text-decoration: underline;
    }

    /* Buttons */
    .stButton > button {
        background-color: rgba(255, 255, 255, 0.1);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.2);
        transition: all 0.3s ease;
        font-size: 1em;
        padding: 10px 20px;
    }

    .stButton > button:hover {
        background-color: rgba(255, 255, 255, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }

    /* Spacing */
    .block-container {
        padding-top: 3rem !important;
        padding-bottom: 3rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app
#st.title("Summarize Genie")
st.markdown("<h1 style='text-align: center;'>📋 Summarize Genie</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Summarize Genie shall summarize Text and Read aloud! </h2>", unsafe_allow_html=True)


# Input API key
api_key_input = st.text_input("Enter your Gemini API Key", type="password")

# Check if API key is provided
if api_key_input:
    genai.api_key = api_key_input
else:
    st.warning("Please enter your Gemini API Key to proceed.")

# Function to read content from Word documents
def read_word(file):
    doc = Document(file)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

# Function to read content from PDF documents
def read_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    full_text = []
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        full_text.append(page.extract_text())
    return '\n'.join(full_text)

# Function to initialize the Generative Model
def get_model(api_key):
    genai.configure(api_key=api_key)
    # Initialize the Generative Model (Gemini Flash model)
    model = GenerativeModel("gemini-1.5-flash")
    return model

# Function to summarize text using Gemini Flash
def summarize_text(text, api_key):
    model = get_model(api_key)
    try:
        response = model.generate_content(["Summarize this text in a few lines:", text])
        paragraph = " ".join(response.text.splitlines())  # Format the summary into a paragraph
        return paragraph
    except Exception as e:
        return f"Error: {str(e)}"

# Function to convert text to speech using gTTS
def text_to_speech_gtts(text):
    tts = gTTS(text=text, lang='en')
    # Save the speech as an MP3 file
    temp_audio_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_audio_file.name)
    return temp_audio_file.name

# Text area for custom text input
input_text = st.text_area("Paste the text you want to summarize", height=200)

# File uploader widget for Word and PDF documents
uploaded_file = st.file_uploader("Or choose a Word or PDF document", type=["docx", "pdf"])

# Summarize the pasted text when button is pressed (Button will appear when there is text in the input area)
if input_text and api_key_input:
    if st.button("Summarize Pasted Text"):
        summarized_content = summarize_text(input_text, api_key_input)
        st.subheader('Summarized Pasted Text:')
        
        # Display summarized content in multiple lines (st.text_area for multi-line display)
        st.text_area("Summary", summarized_content, height=300)

        # Convert the summarized content to speech using gTTS
        audio_file = text_to_speech_gtts(summarized_content)

        # Provide the download link for the generated speech file
        st.audio(audio_file, format="audio/mp3")

# Handle uploaded document summarization
if uploaded_file and api_key_input:
    # Detect file type and read content accordingly
    if uploaded_file.name.endswith('.docx'):
        document_content = read_word(uploaded_file)
    elif uploaded_file.name.endswith('.pdf'):
        document_content = read_pdf(uploaded_file)

    st.subheader('Original Document Content:')
    st.text(document_content)

    # Summarize the uploaded document content when button is pressed
    if st.button("Summarize Uploaded Document"):
        summarized_content = summarize_text(document_content, api_key_input)
        st.subheader('Summarized Document Content:')
        
        # Display summarized content in multiple lines
        st.text_area("Summary", summarized_content, height=300)

        # Convert the summarized content to speech using gTTS
        audio_file = text_to_speech_gtts(summarized_content)

        # Provide the download link for the generated speech file
        st.audio(audio_file, format="audio/mp3")
