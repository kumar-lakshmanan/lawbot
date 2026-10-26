from flask import Flask, request, jsonify, render_template
import s3_ask
import voice_controller

app = Flask(__name__, static_folder='static', template_folder='templates')

# ----------------------------------------------------
# Dummy backend logic – replace with your real engine
# ----------------------------------------------------
def process_query(user_text: str):
    """
    Simulates a time‑consuming legal‑analysis routine.
    Returns the sample JSON you supplied after a small delay.
    """
    print("Got new request...")
    return s3_ask.legal_query(user_text)

# ----------------------------------------------------
# Routes
# ----------------------------------------------------
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():

    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify(error='Missing input'), 400

    voice_controller.text_to_speech("Please wait, Analyzing your legal query...")
    fullresponse = process_query(data['text'])

    table_data, speech_data = fullresponse.split("<<SPLITTER>>")
    table_data, speech_data = str(table_data).strip(), str(speech_data).strip()

    voice_controller.text_to_speech(speech_data)
    print("----")
    print('-Response Table-')
    print("----")
    print(str(table_data))
    print("----")
    print('-Response Speech-')
    print("----")
    print(speech_data)

    return jsonify({"markdown": str(table_data)})

@app.route('/record', methods=['GET'])
def record():
    """Trigger voice recording and transcription.
    Returns JSON with the transcribed text.
    """
    try:
        transcript = voice_controller.record_and_transcribe()
        return jsonify({'text': transcript})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/record_audio', methods=['GET'])
def record_audio_route():
    """Record audio for a given duration and return temp file name."""
    try:
        duration = int(request.args.get('duration', 20))
        temp_file = voice_controller.record_audio(duration)
        return jsonify({'temp_file': temp_file})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/transcribe', methods=['POST'])
def transcribe_route():
    """Transcribe the given temp wav file and return the text."""
    data = request.get_json()
    if not data or 'file' not in data:
        return jsonify({'error': 'Missing file'}), 400
    try:
        text = voice_controller.audio_transcribe(data['file'])
        return jsonify({'text': text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ----------------------------------------------------
# Run
# ----------------------------------------------------
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)