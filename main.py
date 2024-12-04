import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

"""
Disclaimer: Sending unsolicited messages is unethical and may be illegal. 
This script is intended for educational purposes only. 
Use responsibly and only with your own phone number.
"""

def read_file(file_path):
    """Reads the file and returns its content as lines and words."""
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return [], []

    with open(file_path, 'r') as f:
        text = f.read().strip()
        if not text:
            print("Error: File is empty.")
            return [], []
    
    lines = text.splitlines()
    words = text.split()
    return lines, words

def send_message(phone_number, message):
    """Sends a message using an AppleScript command."""
    if not phone_number or not message:
        print("Error: Missing phone number or message.")
        return
    os.system(f'osascript send.scpt {phone_number} "{message}"')

def main():
    # Get the phone number from environment variables
    phone_number = os.getenv('PHONE_NUMBER')
    
    if not phone_number:
        print("Error: PHONE_NUMBER is not set in the .env file.")
        return

    lines, words = read_file('ly.txt')

    # Send each word separately
    for word in words:
        send_message(phone_number, word)

    # Send each line separately
    for line in lines:
        send_message(phone_number, line)

if __name__ == '__main__':
    main()
