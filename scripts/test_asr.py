# scripts/test_asr.py
from backend.asr import transcribe

if __name__ == "__main__":
    audio_file = "sample_audio.wav"  # replace with your audio file
    text = transcribe(audio_file)
    print("✅ Transcribed Text:", text)
