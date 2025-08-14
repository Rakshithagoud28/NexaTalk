import os
from groq import Groq
import whisper

# Initialize Groq API
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Load Whisper model once
whisper_model = whisper.load_model("base")

def pipeline(audio_path):
    """
    1. Transcribe speech to text
    2. Send text to Groq LLM
    3. Return (user_text, ai_text)
    """
    try:
        # Step 1: Transcribe
        transcription = whisper_model.transcribe(audio_path)
        user_text = transcription.get("text", "").strip()

        if not user_text:
            return "", "I couldn't hear anything. Please try again."

        # Step 2: AI response
        chat_response = groq_client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are a helpful voice assistant."},
                {"role": "user", "content": user_text}
            ],
            temperature=0.7,
            max_tokens=200
        )

        ai_text = ""
        if chat_response and chat_response.choices:
            ai_text = chat_response.choices[0].message.content.strip()

        # Always return exactly two values
        return user_text, ai_text

    except Exception as e:
        return "", f"Error: {str(e)}"
