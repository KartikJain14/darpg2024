import os
import requests
import zipfile
import shutil

def download_file(url, local_filename):
    """
    Downloads a file from a given URL and saves it locally.
    """
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

def extract_zip(zip_path, extract_to):
    """
    Extracts a zip file to a specified directory, specifically removing any known subdirectory from the path.
    """
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Determine the name of the subdirectory (assuming there's only one)
        root_folder = zip_ref.namelist()[0].split('/')[0]
        # Ensure the target directory exists
        if not os.path.exists(extract_to):
            os.makedirs(extract_to)

        for member in zip_ref.infolist():
            # Build the path for this item, excluding the root folder
            target_path = os.path.join(extract_to, member.filename.replace(root_folder + '/', '', 1))
            if target_path.endswith('/'):
                # It's a folder path, ensure directory exists
                os.makedirs(target_path, exist_ok=True)
            else:
                # It's a file, extract it
                with zip_ref.open(member, 'r') as source, open(target_path, 'wb') as target:
                    shutil.copyfileobj(source, target)
    print("Extracted to {0}".format(extract_to))

if __name__ == "__main__":
    model_url = "https://alphacephei.com/vosk/models/vosk-model-hi-0.22.zip"
    local_filename = "vosk-model-hi-0.22.zip"
    
    # Download the model
    print("Downloading model...")
    download_file(model_url, local_filename)
    print("Download complete.")
    
    # Define the path to extract the model to
    script_location = os.path.dirname(os.path.abspath(__file__))
    extract_to = os.path.join(script_location, "vox_bridge", "model")
    
    # Extract the model
    print("Extracting model...")
    extract_zip(local_filename, extract_to)
    print("Extraction complete.")
