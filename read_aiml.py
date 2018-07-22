import aiml
import time
import os
import pyttsx3
from gtts import gTTS
import speech_recognition as sr


def speak(speech):
     engine = pyttsx3.init()
     rate = engine.getProperty('rate')
     engine.setProperty('rate', rate+1)
     engine.say(speech)
     engine.runAndWait()


def gspeak(speech):
    try:
        gtts_gspeak(speech)
    except:
        speak(speech)

def listen():
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Enter_Command ")
        audio = r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            s = (r.recognize_google(audio))
            message = (s.lower())
            print (message)                                                                 
            return message
        except sr.UnknownValueError:
             speak("I couldn't understand what you said! Would you like to repeat?")
             return(listen())
        except sr.RequestError as e:
            print("Could not request results from " + "Google Speech Recognition service; {0}".format(e))                                                                                                    


kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
if os.path.isfile("bot_brain.brn"):
        kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

while True:
    try:
        response = listen()
    except:
        response = input("Please_Enter_Command >>")
    
    say = kernel.respond(response)
    gspeak(say)
