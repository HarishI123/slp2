from flask import Flask, render_template, request
from gtts import gTTS
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', audio_src=None)

@app.route('/tts', methods=['POST'])
def text_to_speech():
    text = request.form['text']
    tts = gTTS(text, lang='en')  # You can specify the language here
    audio_file = tts.save("output.mp3")
    with open("output.mp3", "rb") as f:
        audio_data = f.read()
    audio_base64 = base64.b64encode(audio_data).decode('utf-8')
    audio_src = f"data:audio/mpeg;base64,{audio_base64}"
    return render_template('index.html', audio_src=audio_src)

if __name__ == '__main__':
    app.run(debug=True)
