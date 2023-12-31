import speech_recognition as sr  
import pyttsx3 
import pywhatkit
import wikipedia
import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.say("Hi juan, I am Alexa, what do you want to listen today?")
engine.runAndWait ()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print ("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print (command)
    except:
        pass
    return command

def run_alexa():
    command = take_command ()
    print (command)
    if "play" in command:
        song = command.replace("play", "")
        talk("playning" + song )
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk("The current time is " + time )
        print(time)
    elif "who is" in command:
        person = command.replace("who is ", "")
        info = wikipedia.summary(person, 1)
        print (info)
        talk(info)
    elif "bye" in command:
        quit
    else:
        talk("Please say the command again")

while True:
    run_alexa()
