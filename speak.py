# convets text to speech and speaks
import pyttsx3  # to convert text to speech
from datetime import date, datetime  # to fetch date and time


# Speak
# Speak with printing
def Speak(t):
    e = pyttsx3.init("sapi5")
    v = e.getProperty("voices")
    e.setProperty("voices", v[0].id)
    e.setProperty("rate", 170)
    print("")
    print(f"SHRI:{t}")
    print("")
    e.say(t)
    e.runAndWait()


# Speak without printing
def Speako(t):
    e = pyttsx3.init("sapi5")
    v = e.getProperty("voices")
    e.setProperty("voices", v[0].id)
    e.setProperty("rate", 170)
    print("")
    print("")
    e.say(t)
    e.runAndWait()


def greet():
    Speak("Jai Shree Krishna")
    Speak("What is your name?")
    global name
    name = Listeno()
    t = datetime.now()
    if 1 <= t.hour < 12:
        w = "Good Morning"
    elif 12 <= t.hour <= 16:
        w = "Good Afternoon"
    else:
        w = "Good Evening"
    Speak(f"{w},{name}. How may I help you??")
