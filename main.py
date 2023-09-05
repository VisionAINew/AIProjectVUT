import speech_recognition as sr
import pyttsx3

# Initialize recognizer
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# get the available voice
voices = engine.getProperty('voices')

# choose a voice based on the voice id
engine.setProperty('voice', voices[1].id)

# change speech rate
engine.setProperty('rate', 180)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_for_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            speak("I'm Vaal University of Technology Program Infirmary",)
            speak("But you can simply call me Assistant. How may I help you?")
            speak("what can i do for you?")
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            if 'Assistant' in command:
             command = command.replace('Assistant', '')
             print(command)

    except sr.UnknownValueError:
            speak("Sorry, I couldn't understand that")
            speak("or maybe try to say something")
    return command

def process_command():
    while True:
        command = listen_for_command()
        if "hey" in command:  # Adjust the trigger phrase as needed
                response="What are your symptoms? Where do you feel pain? Please describe your symptoms."
                print(response)
                speak(response)

        elif "symptoms" in command:
                    recommendation = ("Based on your description, I recommend taking a painkiller."
                                      " However, it's important to consult a medical professional for accurate advice.")
                    print(recommendation)
                    speak(recommendation)

        elif "Thanks" in command:
                    farewell = "You're welcome! Feel free to come back if you need anything."
                    print(farewell)
                    speak(farewell)
        else:
            print("Sorry, I couldn't hear your symptoms.")

            # End the loop after handling the command
        break
while True:
    process_command()




