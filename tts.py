from TTS.api import TTS

def text_to_speech(text, output_path="response.wav"):
    tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False)
    tts.tts_to_file(text=text, file_path=output_path)