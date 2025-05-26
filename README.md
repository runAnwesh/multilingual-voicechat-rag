# 🗣️ Multilingual Voice Chat RAG System

This project is a prototype for a **Multilingual Voice Chat Retrieval-Augmented Generation (RAG) System** designed for accessible content search and transformation. Built as part of the Flickdone AI Platform Developer assessment, it enables visually impaired users to interact with digital content in multiple languages using voice input.

---

## 🌟 Features

✅ Multilingual **Speech-to-Text** (STT) using Whisper  
✅ **Semantic Retrieval** from local document corpus (FAISS + SentenceTransformers)  
✅ **Natural Language Response Generation** using Google Gemini 2.5 Pro  
✅ **Text-to-Speech** (TTS) output with Coqui TTS  
✅ Accessible, voice-based interaction in multiple languages

---

## 🚀 How to Run

1. **Clone the repo** and install dependencies:
   ```bash
   pip install -r requirements.txt
   ````

2. **Set your Gemini API Key**:

   ```bash
   export GOOGLE_API_KEY="your-api-key"
   ```

3. **Start the Streamlit app**:

   ```bash
   streamlit run streamlit_app.py
   ```

4. **Upload an audio file** (`.wav` or `.mp3`) and interact with the system!

---

## 📁 Project Structure

```
├── stt.py           # Speech-to-Text (Whisper)
├── retriever.py     # Document embedding + retrieval (FAISS)
├── generator.py     # Gemini-based answer generation
├── tts.py           # Coqui TTS for spoken responses
├── main.py          # Interactive demo app
├── docs/            # Local document corpus
├── sample_data/     # Sample input/output audio
└── README.md
```

---

## 🗂️ Example Data

* **Sample documents**: `docs/health_tips_en.txt`, `docs/covid_info_hi.txt`, etc.
* **Sample audio input**: `sample_data/input_hi.wav`, `input_en.wav`

---

## ⚙️ Notes

* The system is **on-premise ready** except for Gemini LLM calls (API-based).
* Supports **multilingual voice** input and output.
* **Intended for accessibility**: empowers visually impaired users.

---



