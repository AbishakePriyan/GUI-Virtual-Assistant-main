import pyjokes
import pywhatkit
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia


r = sr.Recognizer()
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 160)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('This is Kate, how can i help you?')
engine.runAndWait()

def talk(text):
    engine.say(text)
    print(text)
    engine.runAndWait()

def take_command():
    try:
        print("Listening...")
        with sr.Microphone() as source:
            r.energy_threshold = 100000
            r.adjust_for_ambient_noise(source, 1.2)
            voice = r.listen(source)
            command = r.recognize_google(voice)
            command = command.lower()
            print("Recognized voice: " + command)
            if 'kate' in command:
                print(command)
    except:
        pass
    return command

def run_kate():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    if 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        talk('Current time is ' + time)
    if 'who is' in command:
        z = command.replace("who is", '')
        person = wikipedia.summary(z,1)
        talk(person)
    if 'joke' in command:
        x = pyjokes.get_joke()
        talk(x)
    if 'what is mean by' in command:
        a = command.replace("what is mean by",'')
        word = wikipedia.summary(a,1)
        talk(word)
    if 'who programmed you' in command:
        talk('Abhishek , Giri and, Tharoon , The Students Of ARISTO PUBLIC SCHOOL')

while True:
    run_kate()