from stt import transcribe_audio
from retriever import DocumentRetriever
from generator import generate_response
from tts import text_to_speech

if __name__ == "__main__":
    # 1. Voice to Text
    audio_file = "sample_data/input_hi.wav"  # Path to input voice file
    query = transcribe_audio(audio_file)
    print("User Query:", query)

    # 2. Document Retrieval
    retriever = DocumentRetriever("docs")
    context = "\n".join(retriever.search(query))

    # 3. Generate LLM Response
    answer = generate_response(context, query)
    print("Response:", answer)

    # 4. Speak the Response
    text_to_speech(answer, "sample_data/response.wav")
    print("Audio response saved to sample_data/response.wav")
