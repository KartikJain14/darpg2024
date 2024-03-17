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

- Unix based system (support for windows coming soon)
- Python 3.6 or higher
- pip and virtualenv

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/KartikJain14/darpg2024.git
   cd darpg2024

2. **Download and install dependencies and models**

    ```bash
    #setup and activate venv already if required
    pip install -r requirements.txt
    argospm update
    argospm install translate-hi_en
    python model.py
    
5. **In case using a virtual environment**
   vox_bridge/utils/translate.py >> edit _command_ to:
   ```bash
   command = ["/path/to/venv/bin/python3", "/path/to/venv/bin/argos-translate", text, "--from-lang", "hi", "--to-lang", "en"]

Example:

    command = ["/home/user/darpg2024/venv/bin/python3","/home/user/darpg2024/venv/bin/argos-translate", text, "--from-lang", "hi", "--to-lang", "en"]

4. **Run web server**
    
    ```bash
    python wsgi.py

Visit webserver at [localhost](http://localhost:5000)

Provide a hindi audio that is .mp3 and wait for 2 minutes and get the output text in hindi and english

### Things to add:
1. Support Windows

2. CLI support

3. Unit Tests

4. Better Documentations and presentations.

5. Redesign UI for webapp.

6. Reduce time for proccessing.

###### PS: Please contact me, this can be much well documented and can be a better project but due to errors at submission and lesser time frame available to me due to prior hsc examinations. If in case, more time (~48hrs) be provided, I will be able to provide proper documentation, setup scripts, optimise core, present it and give a video for the same. Please give a confirmation so that I resume work for vox bridge