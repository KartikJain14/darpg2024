from flask import Flask, render_template, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from vox_bridge.utils.ffmpeg import convert_audio
from vox_bridge.utils.transcribe import transcribe_audio
from vox_bridge.utils.translate import translate_text
import os

app = Flask(__name__)

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

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
@limiter.limit("10 per hour")
def api():
    if "file" not in request.files or request.files["file"].filename == "":
        return jsonify(message="No file selected"), 400
    file = request.files["file"]
    if file and file.mimetype == "audio/mpeg": #passed all the validations, processing the recording now
        print("file recieved")
        file.save(in_audio)
        #process begins now
        convert_audio(in_audio, out_audio) #converts .mp3 to specific .wav file
        transcribe_audio(model, out_audio, output_hi) #transcribes
        translate_text(output_hi, output_en) #translates hindi transcription to english
        with open(output_hi, "r", encoding="utf-8") as file:
            text_hi = file.read()
        with open(output_en, "r", encoding="utf-8") as file:
            text_en = file.read()
        return render_template("result.html", text_hi=text_hi, text_en=text_en)
    else:
        return jsonify(message = "Invalid file, Please upload an mp3 file.")

@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify(error="You have been rate limited, come back after an hour."), 429

if __name__ == "__main__":
    app.run()
