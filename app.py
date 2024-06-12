import streamlit as st
import pyttsx3
import os

# Initialize the pyttsx3 engine
engine = pyttsx3.init()
# Function to get available voices
def get_voices():
    voices = engine.getProperty('voices')
    voice_list = [(voice.id, voice.name) for voice in voices]
    return voice_list

# Function to set the selected voice
def set_voice(voice_id):
    engine.setProperty('voice', voice_id)

# Function to set the speech rate
def set_rate(rate):
    engine.setProperty('rate', rate)

# Streamlit app layout
st.title("Text-to-Speech Web App (Offline)")
text_input = st.text_area("Enter text here...")

voice_list = get_voices()
voice_id = st.selectbox("Choose a voice", [voice[1] for voice in voice_list])
selected_voice = next(voice for voice in voice_list if voice[1] == voice_id)

rate = st.slider("Select speech rate", min_value=50, max_value=300, value=150)

if st.button("Speak"):
    if text_input:
        set_voice(selected_voice[0])
        set_rate(rate)

        # Convert text to speech and save to a file
        engine.save_to_file(text_input, 'output.mp3')
        engine.runAndWait()

        # Read the audio file and play it in the Streamlit app
        audio_file = open('output.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')
    else:
        st.warning("Please enter some text to convert to speech.")
