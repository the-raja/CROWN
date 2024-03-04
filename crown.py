import  pyttsx3
import speech_recognition as sr

def speak(text):
        engine = pyttsx3.init()
        Id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
        engine.setProperty('voice',Id)
        engine.say(text=text)
        engine.runAndWait()
    
speak("Welcome Back RAJA, how can i help you")

def speechrecognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...........")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language="en")
        return query.lower()
    
    except:
         return  ""

print(speechrecognition())