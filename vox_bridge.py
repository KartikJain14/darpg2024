#!/usr/bin/env python3

import argparse
from vox_bridge.utils.ffmpeg import convert_audio
from vox_bridge.utils.transcribe import transcribe_cli
from vox_bridge.utils.translate import translate_cli, download_model
import os
import tempfile
import subprocess

def convert(mp3_path):
    # Create a temporary file for the WAV output
    temp_wav_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    temp_wav_path = temp_wav_file.name
    temp_wav_file.close()
    convert_audio(mp3_path, temp_wav_path)
    return temp_wav_path

def initialize():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    model_script_path = os.path.join(script_dir, "model.py")
    print("Initializing vosk-bridge. This may take a while...")
    try:
        subprocess.run(["python", model_script_path], check=True)
        download_model()
        print("Initialization complete.")

    except subprocess.CalledProcessError as e:
        print(f"Initialization failed: {e}")

def translate(text, lang):
    in_lang = lang
    out_lang = "en"
    if in_lang == "en":
        out_lang = "hi"
    print(translate_cli(text, in_lang, out_lang))

def translate_(text, lang):
    in_lang = lang
    out_lang = "en"
    if in_lang == "en":
        out_lang = "hi"
    return translate_cli(text, in_lang, out_lang)

def transcribe(input_file, lang):
    wav_file = convert(input_file)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    model_dir = os.path.join(script_dir, "vox_bridge", "model")
    hindi_text = transcribe_cli(model_dir, wav_file)
    if lang == "hi":
        print(hindi_text)
    english_text = translate_(hindi_text, "hi")
    if lang == "en":
        print(english_text)
    else:
        result = {
            "en" : english_text,
            "hi" : hindi_text
        }
        print(result)

def main():
    parser = argparse.ArgumentParser(
        description="Vox-Bridge CLI Tool",
        epilog="""
        Examples:

        # Translate text to Hindi:
        vox-bridge translate "Hello, how are you?" -l en

        # Translate text to English:
        vox-bridge translate "नमस्ते, आप कैसे हैं?" -l hi

        # Transcribe an audio file in hindi and english:
        vox-bridge transcribe -i "/path/to/audio.mp3" -l b
        Output:{\"en\": \"english transcription\", \"hi\": \"hindi transcription\"\}

        # Transcribe an audio file, output only in Hindi:
        vox-bridge transcribe -i "/path/to/audio.mp3" -l hi
        Output:hindi transcription

        # Transcribe an audio file, output only in English:
        vox-bridge transcribe -i "/path/to/audio.mp3" -l en
        Output:english transcription
        """,
            formatter_class=argparse.RawDescriptionHelpFormatter # This helps to preserve the formatting of your epilog
    )
    subparsers = parser.add_subparsers(dest="command")

    # Sub-parser for translate command
    parser_translate = subparsers.add_parser('translate', help='Translate text')
    parser_initialize = subparsers.add_parser('initialize', help='Initialize the tool (required at first run)')
    parser_translate.add_argument('text', type=str, help='Text to translate')
    parser_translate.add_argument('-l', '--language', type=str, choices=['hi', 'en'], default='hi', help='Language to translate to (default: hi)')

    # Sub-parser for transcribe command
    parser_transcribe = subparsers.add_parser('transcribe', help='Transcribe audio file')
    parser_transcribe.add_argument('-i', '--input', type=str, required=True, help='Path to audio file')
    parser_transcribe.add_argument('-l', '--language', type=str, choices=['hi', 'en', 'b'], default='b', help='Language of transcription (default: b for both)')

    args = parser.parse_args()

    if args.command == 'initialize':
        initialize()
    elif args.command == 'translate':
        translate(args.text, args.language)
    elif args.command == 'transcribe':
        transcribe(args.input, args.language)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
