import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def ask_llm(prompt: str) -> str:
    """
    Send the query to Groq/Gemini AI LLM and get response
    """
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {"prompt": prompt, "max_tokens": 200}
    response = requests.post("https://api.groq.com/v1/llm", headers=headers, json=data)
    return response.json().get("text", "")
