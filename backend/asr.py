import whisper

# Load Whisper small model
model = whisper.load_model("small")

def transcribe(audio_path: str) -> str:
    """
    Convert speech to text using Whisper
    """
    result = model.transcribe(audio_path)
    return result["text"]
