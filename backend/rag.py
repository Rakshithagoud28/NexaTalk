def generate_response(user_text: str) -> str:
    """
    Generate a response for the assistant.
    Right now, a simple dummy response mimicking GPT.
    Later, replace this with real RAG or GPT API call.
    """
    # Simple dummy logic for testing
    if "name" in user_text.lower():
        return f"Hello {user_text.split()[-1]}! Nice to meet you."
    elif "how are you" in user_text.lower():
        return "I'm just a voice assistant, but I'm doing great! How about you?"
    else:
        return f"You said: '{user_text}' — I'm still learning to respond properly!"
