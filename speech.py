# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 16:37:31 2020

@author: shrey
"""
import os
import playsound
from gtts import gTTS
from time import ctime

speech = gTTS("awwwwwwwwwww")
print(speech)
a = speech.save('awW!.mp3')

import speech_recognition as sr
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening..")
        audio = r.listen(source,phrase_time_limit = 5)
    data = ""
    try:
        data = r.recognize_google(audio,language='en-US')
        print("You said:"+data)
    except sr.UnknownValueError:
        print("I cannot hear you")
    except sr.RequestError as e:
        print("Request Failed")
    return data
def respond(String):
    print(String)
    tts = gTTS(text=String,lang="en")
    tts.save("speech.mp3")
    playsound.playsound("speech.mp3")
    os.remove("speech.mp3")

def voice_assistant(data):
    if "how are you" in data:
        listening =True
        respond("I am doing good")
    if "time" in data:
        listening = True
        respond(ctime())
        

    
respond("Hello shrey,what can i do for you?")
listening = True
while listening == True:
    data = listen()
    listening = voice_assistant(data)