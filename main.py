import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("Initializing T.A.R.J.A.N.")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Boss, what's the plan for today..")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Boss, what's the plan for today..")
    else:
        speak("Good Evening Boss, what's the plan for today..")

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        
    try:
        print("listening")
        query = r.recognize_google(audio, language= 'en-in')

    except Exception as e:
        speak("Sorry Boss, I didn't get that..")
        query = None
    
    return query

speak("Initializing TARJAN as Setting up all preferences from the System and now you are good to go...")
wishMe()
query = command()
if 'wikipedia' in query.lower():
    query = query.replace("Wikipedia", "")
    print(query)
    results = wikipedia.summary(query, sentences = 2)
    speak(results)

elif 'open youtube' in query.lower():
    url = "youtube.com"


# https://www.youtube.com/watch?v=4k9CphTdnWE