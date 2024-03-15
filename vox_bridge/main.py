from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from vox_bridge.utils.ffmpeg import convert_audio
from vox_bridge.utils.transcribe import transcribe_audio
from vox_bridge.utils.translate import translate_text
import os

app = Flask(__name__)
CORS(app)

script_location = os.path.dirname(os.path.abspath(__file__))
model = os.path.join(script_location, "model")  # location of model for transcription
in_audio = os.path.join(script_location, "data", "audio.mp3")  # accepts mp3 files
out_audio = os.path.join(script_location, "data", "audio.wav")  # must be in WAV form, do not change
output_hi = os.path.join(script_location, "data", "output_hi.txt")  # output txt file name to store hindi transcription
output_en = os.path.join(script_location, "data", "output_en.txt")  # output txt file name to store english translation of the transcription

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/api", methods=["POST"])
def api():
    if "audioFile" not in request.files or request.files["audioFile"].filename == "":
        return "No file selected"
    file = request.files["audioFile"]
    if file and file.mimetype == "audio/mpeg":  # passed all the validations, processing the recording now
        print("file received")
        file.save(in_audio)
        # process begins now
        convert_audio(in_audio, out_audio)  # converts .mp3 to specific .wav file
        transcribe_audio(model, out_audio, output_hi)  # transcribes
        translate_text(output_hi, output_en)  # translates Hindi transcription to English
        with open(output_hi, "r", encoding="utf-8") as file:
            text_hi = file.read()
        with open(output_en, "r", encoding="utf-8") as file:
            text_en = file.read()
        return render_template("result.html", text_hi=text_hi, text_en=text_en)
    else:
        return "Invalid file, Please upload an mp3 file."

if __name__ == "__main__":
    app.run()