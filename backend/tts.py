import pyttsx3
import tempfile

def synthesize_speech(text):
    engine = pyttsx3.init()
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    engine.save_to_file(text, tmp_file.name)
    engine.runAndWait()
    return tmp_file.name
