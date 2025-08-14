import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import sounddevice as sd
import numpy as np
import tempfile
from scipy.io.wavfile import write
import pyttsx3
import whisper
from groq import Groq
import re

# Load models
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
whisper_model = whisper.load_model("base")

# Text-to-speech
def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Pipeline: audio → text → AI reply
def pipeline(audio_file):
    transcription = whisper_model.transcribe(audio_file)
    user_text = transcription.get("text", "").strip()

    prompt = (
        f"You are NexaTalk, a concise AI assistant. "
        f"Answer directly without repeating the question.\n"
        f"User: {user_text}\nAI:"
    )

    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=200
    )

    ai_reply = response.choices[0].message.content.strip()
    return user_text, ai_reply

# Streamlit UI
st.set_page_config(page_title="NexaTalk", page_icon="🎙", layout="centered")
st.title("🎙 NexaTalk Voice Assistant")

# Show stop words right after title
st.markdown(
    "<p style='color:green; font-weight:bold;'>These are the words to end the convo: Quit, Exit, Stop</p>",
    unsafe_allow_html=True
)

if st.button("🎤 Start Conversation"):
    stop_words = {"stop", "exit", "quit"}

    while True:
        duration = 5
        st.write("🎙 Recording... Speak now!")

        fs = 44100
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype=np.int16)
        sd.wait()

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmpfile:
            write(tmpfile.name, fs, recording)
            audio_path = tmpfile.name

        st.write("✅ Recording complete. Processing...")
        user_text, ai_response = pipeline(audio_path)

        st.markdown(f"*You:* {user_text}")
        st.markdown(f"*AI:* {ai_response}")
        speak_text(ai_response)

        os.remove(audio_path)

        # Check stop condition
        cleaned_text = re.sub(r"[^\w\s]", "", user_text.lower())
        if any(word in cleaned_text for word in stop_words):
            st.markdown(
                "<h1 style='text-align: center; color: red;'>👋 Conversation ended.</h1>",
                unsafe_allow_html=True
            )
            break
