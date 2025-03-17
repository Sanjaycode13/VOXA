import pyautogui
import time
import pyttsx3

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

speak("Move your mouse to the position of which the coordinates are required, within the next 5 seconds.")
time.sleep(5)
position = pyautogui.position()
speak(f"The mouse position is: {position}")
