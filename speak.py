#Speak
# Windows-pip install pyttsx3
##remove Windows adv-fast,offline   disadv-cannot overspeak,less voice variety

import pyttsx3
#Speak with printing
def Speak(t):
    e=pyttsx3.init("sapi5")
    v=e.getProperty('voices')
    e.setProperty('voices',v[0].id)
    e.setProperty('rate',170)
    print("")
    print(f"AI:{t}")
    print("")
    e.say(t)
    e.runAndWait()
#Speak without printing
def Speako(t):
    e=pyttsx3.init("sapi5")
    v=e.getProperty('voices')
    e.setProperty('voices',v[0].id)
    e.setProperty('rate',170)
    print("")
    print("")
    e.say(t)
    e.runAndWait()
def greet():
    Speak("Jai Shree Krishna")
    Speak("What is your name?")
    name=Listeno()
    t=datetime.now()

    #s.Speak("How was your day? How do you feel?")
    #feel=l.Execute()
    #add how it feels
    if 1<=t.hour<12:
        w="Good Morning"
    elif 12<=t.hour<=16:
        w="Good Afternoon"
    else:
        w="Good Evening"
    Speak(f"{w},{name}. How may I help you??")