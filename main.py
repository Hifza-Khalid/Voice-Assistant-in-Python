import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return ""
    except sr.RequestError:
        print("Could not request results, check your internet connection.")
        return ""

def assistant():
    speak("Hello! How can I assist you?")
    while True:
        command = listen()
        
        if "time" in command:
            now = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {now}")
        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        elif "exit" in command or "bye" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I didn't understand that.")

if __name__ == "__main__":
    assistant()
