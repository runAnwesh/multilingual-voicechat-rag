import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def generate_response(context, query):
    prompt = f"Context:\n{context}\n\nUser Question:\n{query}\n\nAnswer:"
    response = model.generate_content(prompt)
    return response.text.strip()
