---
title: NexaTalk - Voice Assistant
emoji: 🗣️
colorFrom: pink
colorTo: indigo
sdk: streamlit
sdk_version: 1.36.0
app_file: app.py
pinned: false
license: mit
---

# NexaTalk: Next-Gen Talking Assistant

## Problem Statement
In today’s fast-paced world, users want hands-free, intelligent assistance that can understand and respond to voice queries instantly. Existing assistants like Alexa and Siri are closed ecosystems, limiting integration with custom data or advanced reasoning models.  

There is a need for an open, customizable AI voice assistant that:

- Accurately understands spoken queries in real time.
- Retrieves relevant data from custom knowledge sources.
- Generates human-like, context-aware responses.
- Speaks responses back to the user naturally.

---

## Proposed Solution
**NexaTalk** is a voice-driven AI assistant that:

1. Listens to user queries via microphone.
2. Transcribes speech to text using **Whisper Small**.
3. Enhances queries with **RAG** (Retrieval-Augmented Generation) to include relevant context from your dataset.
4. Generates intelligent responses via **Groq LLM** or **Gemini AI**.
5. Speaks the answer back using **Text-to-Speech (TTS)**.
6. Handles both general and custom domain-specific queries.

---

## Tech Stack
- **Programming Language:** Python  
- **ASR (Speech-to-Text):** OpenAI Whisper Small  
- **RAG:** FAISS (vector database) + local text/CSV/PDF data  
- **LLM:** Groq API or Gemini AI API  
- **TTS (Text-to-Speech):** Google TTS (gTTS) or Coqui TTS  
- **Web Framework:** Streamlit  
- **Backend API:** FastAPI (optional)  
- **Other Libraries:** OpenAI API, PyDub, Sounddevice, Transformers, LangChain  

---

## Project Description
**NexaTalk** is an open-source, AI-powered voice assistant that understands speech, retrieves relevant information, reasons intelligently, and responds naturally.  

**Key Features:**
- 🎙 Real-time speech recognition with Whisper Small
- 📚 Custom knowledge integration via RAG for personalized answers
- 🤖 LLM reasoning with Groq or Gemini AI
- 🔊 Human-like voice replies via TTS
- 🖥 Simple Streamlit web interface

**Use Cases:**
- Personal AI assistant for students & professionals
- Voice-enabled knowledge base for customer support
- Hands-free AI interface for accessibility

