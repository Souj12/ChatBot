# speech_to_text.py

import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to capture voice input
def listen_for_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I did not catch that. Please repeat.")
            return "unknown"
        except sr.RequestError:
            print("Sorry, I couldn't reach the recognition service.")
            return "unknown"
