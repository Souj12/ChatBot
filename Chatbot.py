import tkinter as tk
from PIL import Image, ImageTk  # Pillow is required for handling images in Tkinter
import random
from text_to_speech import speak_response
from speech_to_text import listen_for_command

# Define the chatbot responses
responses = {
    "hi": ["Hello!", "Hi there!", "Greetings!"],
    "how are you": ["I'm just a bot, but I'm doing well!", "I'm here to assist you!", "I'm fine, thank you!"],
    "what is your name": ["I am a chatbot created by you!", "I'm just a nameless bot.", "You can call me ChatBot."],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "what is my student id number":["Your student ID number is typically provided in your admission letter or can be found on your student ID card. You can also find it by logging into your student portal."],
    "where can i find the academic calendar":["The academic calendar is usually available on your institutions website under the “Academic” or “Registrar” section. It includes important dates such as semester start and end dates, holidays, and exam periods."],
    "how do i join a study group":["Join a study group by contacting fellow students in your class or by checking with your courses online platform for group study options. You can also inquire at the academic support center for study group opportunities."],
    "how do i find out about campus events":["Campus events are typically listed on your institutions website under the “Events” or “Student Life” section. You can also check bulletin boards around campus or subscribe to campus newsletters."],
    "what is the process for changing my contact information":[" Update your contact information through your student portal under the Personal Information section. Make the necessary changes and save them."],
    "default": ["I'm sorry, I don't understand that.", "Can you please rephrase?", "I'm not sure what you mean."]
}

# Function to get the chatbot's response
def get_response(user_input):
    user_input = user_input.lower()
    
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    return random.choice(responses["default"])

# Function to handle the "Speak" button click
def on_speak_button_click():
    user_input = listen_for_command()

    if user_input == "unknown":
        return

    chat_window.insert(tk.END, "You: " + user_input + "\n", "user")

    if "bye" in user_input.lower():
        response = "Goodbye!"
        speak_response(response)
        chat_window.insert(tk.END, "ChatBot: " + response + "\n", "bot")
        root.after(2000, root.destroy)
        return

    response = get_response(user_input)
    chat_window.insert(tk.END, "ChatBot: " + response + "\n", "bot")
    speak_response(response)

# Function to handle the "Submit" button click
def on_submit_button_click():
    user_input = text_entry.get()
    if user_input:
        chat_window.insert(tk.END, "You: " + user_input + "\n", "user")
        text_entry.delete(0, tk.END)
        
        if "bye" in user_input.lower():
            response = "Goodbye!"
            speak_response(response)
            chat_window.insert(tk.END, "ChatBot: " + response + "\n", "bot")
            root.after(2000, root.destroy)
            return
        
        response = get_response(user_input)
        chat_window.insert(tk.END, "ChatBot: " + response + "\n", "bot")
        speak_response(response)

# Set up the main application window
root = tk.Tk()
root.title(" Voice-Enabled ChatBot")

# Load and set the background image
background_image = Image.open("background.jpg")
background_image = background_image.resize((800, 600), Image.Resampling.LANCZOS)  # Resize image to fit window
bg_image = ImageTk.PhotoImage(background_image)

# Create a Canvas widget to hold the background image
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_image, anchor="nw")

# Chat window to display the conversation
chat_window = tk.Text(root, bd=1, bg="light yellow", width=50, height=20, font=("Arial", 12), wrap="word")
chat_window_window = canvas.create_window(50, 50, anchor="nw", window=chat_window)

# Add tags for color
chat_window.tag_config("user", foreground="dark blue", font=("Arial", 12, "bold"))
chat_window.tag_config("bot", foreground="dark green", font=("Arial", 12, "italic"))

# Text entry for user input
text_entry = tk.Entry(root, width=40, font=("Arial", 12))
text_entry_window = canvas.create_window(50, 500, anchor="nw", window=text_entry)

# "Submit" button to handle text input
submit_button = tk.Button(root, text="Submit", width=10, command=on_submit_button_click, bg="dark green", fg="white", font=("Arial", 12, "bold"))
submit_button_window = canvas.create_window(450, 500, anchor="nw", window=submit_button)

# "Speak" button to activate voice input
speak_button = tk.Button(root, text="Speak", width=10, command=on_speak_button_click, bg="dark orange", fg="white", font=("Arial", 12, "bold"))
speak_button_window = canvas.create_window(350, 400, anchor="nw", window=speak_button)

# Run the application
root.mainloop()
 