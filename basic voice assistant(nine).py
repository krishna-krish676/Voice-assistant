import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def takecommand():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
    try:
            command = listener.recognize_google(voice)
            command = command.lower()
            print(f"{command}")
            return command
    except:
        return ""


assistant_name = "nine"


def run_assistant():
    command = takecommand()
    print(f"Recognized command: {command}")

while True:
    command=takecommand()
    if command is None:
        continue
    command=command.lower()

    if "stop" in command:
          talk("goodbye")
          break

    if assistant_name.lower() in command:
        command = command.replace(assistant_name.lower(), "").strip()

    if "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f" the time is {time}")

    elif "play" in command:
        song=command.replace("play", "").strip()
        talk(f"playing {song} on youtube")
        pywhatkit.playonyt(song)

    elif "hello" in command:
        talk(f"Hello! {assistant_name} is here. How can I help you?")
    
    else:
        talk(f"{assistant_name} didn't get that. Please say again.")


while True:
    run_assistant()