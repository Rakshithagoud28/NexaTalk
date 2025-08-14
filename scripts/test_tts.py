# scripts/test_tts.py
from backend.tts import text_to_speech

if __name__ == "__main__":
    text = "Hello! This is NexaTalk testing text-to-speech."
    audio_file = text_to_speech(text, "test_output.mp3")
    print(f"✅ TTS audio saved at: {audio_file}")
