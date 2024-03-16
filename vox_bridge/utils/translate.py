import subprocess
import os

def translate_text(hi_text, en_text):
    try:
        with open(hi_text, "r", encoding="utf-8") as file:
            text = file.read()

        # Adjust the command to call the argos-translate without passing text directly as an argument
        command = ["argos-translate", text , "--from-lang", "hi", "--to-lang", "en"]

        # Execute the command and pass the text via stdin
        result = subprocess.run(command, input=text, capture_output=True, text=True, check=True)

        translated_text = result.stdout.strip()

        with open(en_text, "w", encoding="utf-8") as file:
            file.write(translated_text)

    except subprocess.CalledProcessError as e:
        print(f"Translation failed: {e}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

    return True
