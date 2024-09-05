import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

# get voices of engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    # speak function for speak the string
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good Morning jv!")

    elif hour >=12 and hour <18:
        speak("Good Afternoon jv!")

    else:
        speak("Good evening jv!")

    speak("How may I help you")

def takeCommand():
    # it take your command as input and return string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"you say : {query}\n")

    except Exception as e:

        print("Say that again ....")
        return "none"
    return query
    
if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query :
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=3)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open code' in query:
            code ="C:\\Users\\Lenovo\\Downloads\\Microsoft VS Code\\Code.exe"
            os.startfile(code)
            