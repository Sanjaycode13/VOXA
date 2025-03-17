from datetime import datetime
import pyttsx3
import speech_recognition as sr
import pyautogui
from PIL import Image
import pandas as pd
import json
import time
import subprocess

# Load configuration from JSON file
with open('config.json') as config_file:
    config = json.load(config_file)

USERNAME = config['USERNAME']
BOTNAME = config['BOTNAME']

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.now().hour)
    if 6 <= hour < 12:
        speak(f"Good Morning {USERNAME}!")
    elif 12 <= hour < 16:
        speak(f"Good Afternoon {USERNAME}!")
    elif 16 <= hour < 19:
        speak(f"Good Evening {USERNAME}!")
    speak(f"I am {BOTNAME}. How may I assist you?")

def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            return recognizer.recognize_google(audio, language='en-in').lower()
        except Exception:
            speak("I didn't catch that. Please say it again.")
            return "None"

def send_whatsapp_message(contact_file):
    speak("Whom do you want to send the message to?")
    recipient_name = takeCommand().strip().lower()

    try:
        # Load contacts from Excel
        df = pd.read_excel(contact_file)
        contact_row = df[df['Name'].str.lower() == recipient_name]

        if not contact_row.empty:
            speak("What is the message?")
            message = takeCommand()

            # Open WhatsApp Desktop App using subprocess
            subprocess.run(["open", "-a", "WhatsApp"])
            time.sleep(7)  # Slightly longer delay for app to open properly

            # Click on fixed coordinates for the search bar
            search_bar_x, search_bar_y = 227, 92
            pyautogui.click(search_bar_x, search_bar_y)
            time.sleep(1)
            pyautogui.write(recipient_name)
            time.sleep(2)

            # Click on the first contact from the search results
            first_contact_x, first_contact_y = 242, 214
            pyautogui.moveTo(first_contact_x, first_contact_y)
            pyautogui.click()
            time.sleep(2)

            # Type and send the message
            pyautogui.write(message)
            pyautogui.press('enter')

            speak(f"Message sent to {recipient_name}.")

        else:
            speak(f"I couldn't find {recipient_name} in the contacts list.")

    except Exception as e:
        speak(f"Failed to send message: {e}")

if __name__ == "__main__":
    wishme()
    contact_file = 'contacts.xlsx'  # Path to the contacts Excel file

    while True:
        query = takeCommand()

        if 'send message' in query:
            send_whatsapp_message(contact_file)

        elif 'exit' in query or 'bye' in query:
            speak("Goodbye!")
            break
