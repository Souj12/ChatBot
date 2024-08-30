# text_to_speech.py

import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak out the chatbot's response
def speak_response(response):
    engine.say(response)
    engine.runAndWait()
