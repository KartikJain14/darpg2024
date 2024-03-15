import sys
import os
from vosk import Model, KaldiRecognizer
import wave
import json

def transcribe_audio(model_path, audio_path, output_text_path):
    # Check if model exists
    if not os.path.exists(model_path):
        print(f"The model path '{model_path}' does not exist. Exiting.")
        sys.exit(1)
    
    # Load the Vosk model
    model = Model(model_path)
    
    # Open the audio file
    with wave.open(audio_path, "rb") as wf:
        # Check if audio file is compatible
        if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
            print("Audio file must be WAV format mono PCM.")
            sys.exit(1)
        
        # Create a recognizer with the model
        recognizer = KaldiRecognizer(model, wf.getframerate())
        
        # Initialize an empty result string
        result_text = ""
        
        # Process the audio file
        while True:
            data = wf.readframes(16000)
            if len(data) == 0:
                break
            if recognizer.AcceptWaveform(data):
                partial_result = json.loads(recognizer.Result())
                result_text += partial_result['text'] + " "
        
        # Get any remaining text after processing is finished
        final_result = json.loads(recognizer.FinalResult())
        result_text += final_result['text']
        
        # Write the transcription to the output text file
        with open(output_text_path, "w", encoding="utf-8") as out_file:
            out_file.write(result_text)
        
        print(f"Transcription completed. Output saved to '{output_text_path}'.")