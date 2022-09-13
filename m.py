# import subprocess
from __future__ import print_function
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import numpy
from numpy import *
import re 
import pyttsx3
# import tkinter
import json
# import random
# import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import googlemaps
import os
# import winshell
import pyjokes
# import feedparser
import smtplib
import ctypes
import time
import requests
# import shutil
from twilio.rest import Client
# from client.textui import progress
# from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import wolframalpha
import pywhatkit
import datetime
import pickle
import os.path



engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
#print(voice[0].id)
engine.setProperty('voice',voice[1].id)

rate = engine.getProperty('rate')   
engine.setProperty('rate', 145)

def speak(audio):
     engine.say(audio)
     engine.runAndWait()


  



def wishMe():
     hour= int(datetime.datetime.now().hour)
     if hour>=0 and hour<12:
          speak("Good Morning")

     elif hour>=12 and hour<18:
           speak("Good Afternoon")        
     else:
          speak("Good Evening")     

     speak("Sam here, how may I help you")     

def takeCommand():
   r=sr.Recognizer()
   with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1
         audio= r.listen(source)
   try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')    
        print(f"User Said:{query}\n")
          
   except Exception as e:
       # print(e)
        print("Say That Again Please...")
        return "None"      
   return query 
if __name__=="__main__":
  wishMe()
  while(True):
          
        query = takeCommand().lower()
        if "wikipedia" in query:
          query = query.replace("wikipedia", "")
          results = wikipedia.summary(query)
          speak(results)

        elif 'youtube' in query:
             webbrowser.open("youtube.com")

        elif 'google' in query:
             webbrowser.open("google.com")  
        elif 'stack overflow' in query:
             webbrowser.open("stackoverflow.com")    
  
        elif 'podcast' in query:
            webbrowser.open("podcasts.google.com")
       
        elif 'translate' in query:
             webbrowser.open("translate.google.co.in")    
  
        elif 'search' in query or 'play' in query:             
          #   query = query.replace("search", "")
          #   query = query.replace("play", "")         
          #   webbrowser.open(query)
          query = query.replace("play","")
          song = query.replace("play","")
          pywhatkit.playonyt(song)

          #pywhatkit.playonyt(song)

        elif 'the time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"The Time {strTime}")  

        elif "calculate" in query:             
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client('K2GH2J-E8QPH2758Y')
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)  

        # elif 'doubt' or 'problems' in query:
        #     speak("Is it releated to Mathematics Or Science")
        #     db=takeCommand()
        #     if 'maths'in db:
        #         speak("here is some website that might help you")
        #         webbrowser.open("https://www.mathdoubts.com/")    
        #         webbrowser.open("https://www.doubtnut.com/")
        #         break
        #     elif 'science' in db:
        #         speak("here is some website that might help you")
        #         webbrowser.open("https://www.doubtnut.com/")
        #         webbrowser.open("https://www.quora.com/What-are-some-of-the-most-interesting-science-questions-how-why-what-to-know")
        #         break 
        #     break   
           
     
        elif 'how are you' in query:
                speak("I am fine, Thank you")
                speak("How are you")
        elif 'joke' in query:
                speak(pyjokes.get_joke()) 
                print(pyjokes.get_joke())     

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")    

   

        elif "note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('note.txt', 'w')
            speak("Sir, Should i include date and time")
            query = takeCommand()
            if 'yes' in query or 'sure' in query:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
 
   
        elif "wikipedia" in query:
                webbrowser.open("wikipedia.com") 

        elif "i love you" in query:
            speak("It's hard to understand, love is complicated these days")

       

      
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")  

        elif 'lock window' in query:
                speak("doing it right way")
                ctypes.windll.user32.LockWorkStation()

        elif "what is" in query or "who is" in query or "how to" in query or "what does" in query:             
            client = wolframalpha.Client("K2GH2J-E8QPH2758Y")
            res = client.query(query)
             
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")

                
        elif "attendance" in query:
            speak("login using your mail id and go to the attendance page")
            webbrowser.open("https://academia.srmist.edu.in/#Page:My_Attendance")


        elif 'exit'in query or 'thanks' in query or 'thank you' in query:
            speak("Thanks for giving me your time")
            exit()    
       