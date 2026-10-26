import numpy as np
import sounddevice as sd
import whisper
import tempfile
import wave
import pyttsx3
import threading

# Load the whisper model ('tiny', 'base', 'small', 'medium', 'large')
# 'base' or 'small' is usually a great sweet spot for speed and accuracy on a personal computer
print("📥 Loading Whisper model...")
model = whisper.load_model("base")

SAMPLE_RATE = 16000

def record_audio(DURATION=20):
    """Record audio for DURATION seconds and return the temp wav file path."""
    print(f"🎤 Recording for {DURATION} seconds... Speak now!")
    audio_data = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype=np.int16)
    sd.wait()
    print("⏹️ Recording finished. Saving to temp file...")
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_wav:
        with wave.open(temp_wav.name, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(SAMPLE_RATE)
            wf.writeframes(audio_data.tobytes())
        temp_filename = temp_wav.name
        print(temp_filename)
    return temp_filename

def audio_transcribe(tmp_audio_file):
    """Transcribe the given wav file using Whisper and return the text."""
    result = model.transcribe(audio=tmp_audio_file)
    return result["text"]

# Backwards compatibility: record_and_transcribe uses the new functions
def record_and_transcribe():
    DURATION = 20
    temp_file = record_audio(DURATION)
    return audio_transcribe(temp_file)

def text_to_speech(text):
    """Speak the provided text using pyttsx3 asynchronously.

    Parameters
    ----------
    text : str
        The text to be spoken.
    """
    if not text:
        return ""

    def _speak():
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        engine.stop()

    # Run the TTS in a separate daemon thread so it doesn't block the caller
    thread = threading.Thread(target=_speak, daemon=True)
    thread.start()
    return text

if __name__ == "__main__":
    transcript = record_and_transcribe()
    print("\n✨ Transcription Result:")
    print(transcript)
    # Speak the transcript
    text_to_speech(transcript)
    # Pass 'transcript' to your python-based AI tool here!