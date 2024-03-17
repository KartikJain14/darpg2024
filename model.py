import os
import requests
import zipfile
import shutil

def download_file(url, local_filename):
    if not os.path.exists(local_filename):
        try:
            print("Downloading model...")
            with requests.get(url, stream=True) as r:
                r.raise_for_status()
                with open(local_filename, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            print("Download complete.")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download the file: {e}")
            return False
    else:
        print("File already exists, skipping download.")
    return True

def extract_zip(zip_path, extract_to):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Check for corrupted zip file
            if zip_ref.testzip() is not None:
                print("Zip file is corrupted.")
                return False
            # Extract files, ensuring directories are properly handled
            for member in zip_ref.infolist():
                # Replace root folder path in member filenames
                target_path = os.path.join(extract_to, member.filename.split('/', 1)[-1])
                # Ensure the target directory exists
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                # Extract if it's a file
                if not member.is_dir():
                    with zip_ref.open(member, 'r') as source, open(target_path, 'wb') as target:
                        shutil.copyfileobj(source, target)
        print(f"Extracted to {extract_to}")
    except zipfile.BadZipFile:
        print("Failed to extract the model: The zip file is corrupted.")
        return False
    return True

if __name__ == "__main__":
    model_url = "https://alphacephei.com/vosk/models/vosk-model-hi-0.22.zip"
    local_filename = "vosk-model-hi-0.22.zip"
    
    if download_file(model_url, local_filename):
        script_location = os.path.dirname(os.path.abspath(__file__))
        extract_to = os.path.join(script_location, "vox_bridge", "model")
        
        if extract_zip(local_filename, extract_to):
            print("Extraction complete.")
            # Optionally, delete the downloaded zip file
            os.remove(local_filename)
            print("Deleted downloaded zip file.")
        else:
            print("Extraction failed.")
    else:
        print("Download failed or was skipped.")