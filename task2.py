import streamlit as st
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
import torch
import librosa
import soundfile as sf
import speech_recognition as sr


def resample_audio(file_path, target_sr=16000):
    try:
        # Load audio file with librosa
        audio, sr = librosa.load(file_path, sr=None)
        if sr != target_sr:
            # Resample using librosa
            audio = librosa.resample(audio, orig_sr=sr, target_sr=target_sr)
        return audio, target_sr
    except Exception as e:
        print(f"Error during audio resampling: {e}")
        return None, None

# Function to transcribe using Wav2Vec2
def transcribe_wav2vec2(file_path):
    try:
        # Load Wav2Vec2 processor and model
        processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h-lv60-self")
        model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h-lv60-self")

        # Resample audio to 16000 Hz
        audio, sample_rate = resample_audio(file_path, target_sr=16000)
        if audio is None:
            return "Error during resampling."

        # Process the audio and transcribe it
        input_values = processor(audio, return_tensors="pt", sampling_rate=sample_rate).input_values
        logits = model(input_values).logits
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = processor.decode(predicted_ids[0])
        return transcription
    except Exception as e:
        print(f"Error during transcription: {e}")
        return "Transcription failed."

# Streamlit UI for Speech-to-Text
def main():
    st.title("Speech-to-Text System")
    st.subheader("Choose an audio file and transcription method")

    # File upload
    uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "flac"])

    if uploaded_file is not None:
        file_path = f"temp_audio.{uploaded_file.type.split('/')[1]}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.audio(uploaded_file, format="audio/wav")

        # Choose transcription method
        transcription_method = st.selectbox("Choose transcription method", 
                                           ["Wav2Vec2 (Deep Learning)"])

        # Button to trigger transcription
        if st.button("Transcribe"):
            if transcription_method == "Wav2Vec2 (Deep Learning)":
                st.write("Transcribing with Wav2Vec2...")
                transcription = transcribe_wav2vec2(file_path)
                st.write(f"Transcription (Wav2Vec2): {transcription}")

if __name__ == "__main__":
    main()
