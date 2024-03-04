import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening..........')
            voice = listener.listen(source,0,8)
            command = listener.recognize_google(voice)
            if 'Crown' in command:
                command = command.replace('Crown', '')
                print(command)
            

    except:
        pass
    return command

def run_crown():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                print(time)
                talk('Current time is' + time )
                
run_crown()