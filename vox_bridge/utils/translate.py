import subprocess

def translate_text(hi_text, en_text):
    try:
        with open(hi_text, "r", encoding="utf-8") as file:
            text = file.read()
        
        # Construct command as a list to avoid using the shell
        command = ["argos-translate", "--from", "hi", "--to", "en", text]
        
        # Execute command without shell=True
        result = subprocess.run(command, capture_output=True, text=True, check=True)

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
