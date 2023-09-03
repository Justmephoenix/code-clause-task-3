import speech_recognition as sr
from time import ctime
import webbrowser
import time
import playsound
import os
from gtts import gTTS
import random
from random import randint

r=sr.Recognizer()
def record_audio(ask=False):
    with sr.Microphone() as source:
        optimus_speak('Now say Something ')
        if ask:
            optimus_speak(ask)
        audio=r.listen(source)
        voice_data=''
        try:
            voice_data=r.recognize_google(audio)
        except sr.UnknownValueError:
            optimus_speak("Sorry , I did not get that")
        except sr.RequestError():
            optimus_speak("Sorry My speech services is down for a little bit ")
    return voice_data
def optimus_speak(audio_string):
    tts=gTTS(text=audio_string,lang='en')
    r=randint(1,1000000000)
    audio_file='audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
def respond(voice_data):
    if "what is your name" in voice_data  :
        optimus_speak('My Name is Optimus Prime ')
    if "What time is it" in voice_data:
        optimus_speak(ctime())
        
    if 'search' in voice_data:
        search=record_audio('what do you want to search for ')
        url='https://google.com/search?q='+search
        webbrowser.get().open(url)
        optimus_speak("here is what i found for "+search) 
    if 'find location' in voice_data:
        location=record_audio('where is the location ?? ')
        url='https://google.nl/maps/place/'+location+'/&amp;'
        webbrowser.get().open(url)
        optimus_speak("here is the location  "+location) 
    if 'exit' in voice_data:
        exit()
 
time.sleep(1)       
optimus_speak("How can I Help You ???")
while 1:
    voice_data=record_audio()
    respond(voice_data)