
# [Vox Bridge](https://vox.preztyl.tech/)

Vox Bridge is an innovative solution designed to bridge linguistic gaps with state-of-the-art voice recognition and translation technologies. This project leverages the power of the Vosk speech recognition model to offer high-quality, offline voice recognition in Hindi, with plans to expand to more languages in the future. It is a truly opensource program and does not rely on any type of propietary software and requires no api keys to access any service.
This project is offline compatible once all the files are downloaded and set up.

### Visit and use the live demo at [https://vox.preztyl.tech/](https://vox.preztyl.tech/) 

## Features

- **Offline Speech Recognition:** Utilizes the Vosk model for efficient and accurate offline speech recognition.
- **Language Support:** Initially supports Hindi with plans to extend support to multiple languages.
- **Easy Integration:** Designed to be easily integrated into various projects requiring voice recognition capabilities.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or higher
- pip and virtualenv

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/KartikJain14/darpg2024.git
   cd darpg2024

2. **Create virtual environment (optional)**

    ```bash
    python -m venv env
    python activate.py env
    #run the command that will be given as output
    
2. **Download and install dependencies and models**

    ```bash
    pip install -r requirements.txt
    python vosk_bridge.py initialize
    
4. **Run web server**
    
    ```bash
    python wsgi.py

Visit webserver at [localhost](http://localhost:5000) **OR**:

- **CLI Usage**
	```bash
  python vox_bridge.py translate "text in one language" -l [en/hi]
  #-l en in this case because the given text is in english.
  python vox_bridge.py transcribe -i "/path/to/audio.mp3" -l [en/hi/b]
  #-i should be the path to an .MP3 ONLY -l (language you want output in, b=both en & hi)
  python vox_bridge.py -h
  #for more help.

Provide a hindi audio that is .mp3 and wait for 2 minutes and get the output text in hindi and english

### Things to add:
1. Make global package.

2. Better Documentations and presentations.

3. Redesign UI for webapp.

4. Reduce time for proccessing.

###### PS: Please contact me, this can be much well documented and can be a better project but due to errors at submission and lesser time frame available to me due to prior hsc examinations. If in case, more time (~48hrs) be provided, I will be able to provide proper documentation, setup scripts, optimise core, present it and give a video for the same. Please give a confirmation so that I resume work for vox bridge