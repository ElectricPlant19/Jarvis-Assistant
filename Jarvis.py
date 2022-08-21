from asyncio import QueueEmpty, SendfileNotAvailableError
from csv import excel
import datetime
from email.mime import audio
from html.entities import name2codepoint
from imp import source_from_cache
from operator import truediv
import py_compile
from re import I
from tkinter import E, W
from turtle import st
from unicodedata import name
from unittest.mock import sentinel
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import getpass

engine =  pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Jarvis Sir . Please tell me how can i help you")

def takeCommand():

    ''' 
    it takes microphone input from the 
    user and returns a string output 

    '''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio , language='en-in')
        print(f"User said : {query} \n")
    
    except Exception as e:
        
        #print(e)

        print(" Say that again please...")
        return "None"
    return query






if __name__ == "__main__":

    wishme()
    
    while True:

        query = takeCommand().lower()
         
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences = 3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open geeks for geek' in query:
            webbrowser.open('geeksforgeek.com')

        elif 'play music' in query:
            music_dir = "C:\\Users\\User\\Music\\MyMusic"
            songs = os.listdir(music_dir)
            print(songs)
            x = random.choice(list(range(0,(len(songs)-1))))
            os.startfile(os.path.join(music_dir, songs[x]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak ( f"sir the time is {strTime}" )

        elif 'open code editor' in query:
            codePath = "C:\\Users\\User\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(codePath)

        elif 'open excel' in query:
            excelPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"
            os.startfile(excelPath)


        elif '73' in query or 'best number' in query:
            with open('Seventy three.txt' , 'r') as file:
                text = file.read()
                print(text)
                speak(text)

        elif 'ultimate question' in query:
            with open('Forty Two.txt', 'r') as answer:
                text = answer.read()
                print(text)
                speak(text)

            

        elif 'stop' in query:
            speak("Glad to help you sir! May the force be with you !")
            break

        