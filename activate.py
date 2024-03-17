import os
import platform
import sys

def generate_activation_command(venv_name):
    if platform.system() == "Windows":
        # For Windows, the activate script is located in the Scripts folder.
        activation_command = f"{venv_name}\\Scripts\\activate"
    else:
        # For Unix-like systems, the activate script is in the bin folder.
        activation_command = f"source {venv_name}/bin/activate"

    return activation_command

def main():
    if len(sys.argv) != 2:
        print("Usage: python activate.py <venv_name>")
        sys.exit(1)
    
    venv_name = sys.argv[1]
    activation_command = generate_activation_command(venv_name)
    print("To activate the virtual environment, run the following command:")
    print(activation_command)

if __name__ == "__main__":
    main()
