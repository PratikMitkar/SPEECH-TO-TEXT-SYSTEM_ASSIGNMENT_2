# SPEECH-TO-TEXT-SYSTEM_ASSIGNMENT_1

**COMPANY**: CODTECH IT Solutions

**NAME**: Pratik Mitkar

**INTERN ID**: CT08GJB

**DOMAIN**: Artificial Intelligence

**BATCH DURATION**: January 5th, 2025 to February 5th, 2025

**MENTOR NAME**: NEELA SANTHOSH

## Project Description

The **Speech-to-Text System** project is a practical application designed to convert spoken audio into written text using state-of-the-art natural language processing (NLP) models. This tool utilizes pre-trained models like **Wav2Vec2** from Hugging Face and the **SpeechRecognition** library to transcribe short audio clips into text. The system features an easy-to-use web interface built with **Streamlit**, allowing users to upload audio files, trigger transcriptions, and view results in real-time.

The core functionality of this project revolves around converting audio files (like MP3 or WAV) to text. The system is capable of resampling audio files to the required sample rate and transcribing the content using **Wav2Vec2**, a deep learning-based model optimized for speech recognition tasks. The model was fine-tuned with thousands of hours of spoken data and is capable of handling various accents and speech variations.

### Key Features:
1. **Audio File Support**: The system can handle MP3 and WAV audio files, ensuring compatibility with a wide range of formats.
2. **Audio Preprocessing**: Automatically resamples audio to the required 16kHz sample rate, ensuring compatibility with the model.
3. **Speech-to-Text Conversion**: Uses the **Wav2Vec2** model for accurate transcription of audio files.
4. **Streamlit Web Interface**: Provides a user-friendly UI where users can upload files, view transcriptions, and manage errors.

### Development Process

The development of the Speech-to-Text System involved several stages:

1. **Research and Understanding of Wav2Vec2**: I explored how Wav2Vec2 works for automatic speech recognition (ASR), understanding its architecture and pre-training approach.
2. **Model Integration**: I integrated the pre-trained Wav2Vec2 model with Python code to handle audio input and perform transcriptions.
3. **Audio Preprocessing**: Developed preprocessing scripts to resample audio files to the correct sample rate (16kHz), which is essential for accurate transcription.
4. **Building the Web Interface**: Used **Streamlit** to build an intuitive user interface where users can easily upload audio files, initiate transcriptions, and see the output immediately.
5. **Error Handling and Testing**: Implemented error-handling mechanisms to manage different cases like unsupported audio formats and model inference issues.

### Skills Gained
- **Speech Recognition**: Hands-on experience with Wav2Vec2, one of the leading models for speech-to-text tasks.
- **Python and Streamlit**: Gained expertise in using Streamlit to create interactive web applications, along with handling model inference in real-time.
- **Audio Processing**: Acquired knowledge of audio resampling and its significance in speech recognition tasks.
- **Machine Learning Integration**: Familiarized with integrating pre-trained NLP models into production-level applications.

### Future Enhancements
- **Multi-Language Support**: Expanding the system to handle different languages for broader use cases.
- **Real-Time Transcription**: Implementing real-time transcription for live audio inputs.
- **Noise Handling**: Improving the system’s ability to handle noisy audio files and produce more accurate transcriptions in varied environments.

## Installation Details

To run the Speech-to-Text System, follow these steps:

1. **Clone the Repository**:
   ```bash
   https://github.com/PratikMitkar/SPEECH-TO-TEXT-SYSTEM_ASSIGNMENT_2.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd SPEECH-TO-TEXT-SYSTEM_ASSIGNMENT_2
   ```

3. **Set Up a Virtual Environment (Optional but Recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Streamlit Application**:
   ```bash
   streamlit run task1.py
   ```

6. **Access the Application**:
   Open the provided URL (e.g., `http://localhost:8501`) in your web browser.
