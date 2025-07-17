import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def chatbot():
    while True:
        user = input("You: ").lower()
        if user == "hello":
            response = "Hi!"
        elif user == "how are you":
            response = "I'm fine, thanks!"
        elif user == "bye":
            response = "Goodbye!"
            print("Bot:", response)
            speak(response)
            break
        else:
            response = "Sorry, I don't understand."
        print("Bot:", response)
        speak(response)
chatbot()