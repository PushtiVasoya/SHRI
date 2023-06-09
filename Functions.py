# all tasks to be performed
import AppOpener as ao  # for opening the apps
import webbrowser  # to open the urls in browser
import pyjokes  # to tell jokes

# For opening apps and websites
l = [
    "anydesk",
    "calculator",
    "clock",
    "microsoft excel",
    "notepad",
    "paint",
    "microsoft power point",
    "spotify",
    "microsoft store",
    "microsoft word",
    "terminal",
]
d = {
    "google": "http://www.google.com",
    "gmail": "http://www.gmail.com",
    "youtube": "http://www.youtube.com",
    "facebook": "http://www.facebook.com",
    "instagram": "http://www.instagram.com",
    "linkedin": "http://www.linkedin.com",
    "amazon": "http://www.amazon.com",
    "wikipedia": "http://www.wikipedia.org",
    "twitter": "http://www.twitter.com",
    "netflix": "http://www.netflix.com",
    "stackoverflow": "http://www.stackoverflow.com",
    "whatsapp": "http://www.whatsapp.com",
    "github": "http://www.github.com",
}


def openit(c):
    for a in c.split(" "):
        if a in l:
            ap = ao.open(a)
            Speako(f"Opening {a}")

        if a in d:
            ap = webbrowser.open(d[a])
            Speako(f"Opening {a}")


def closeit(c):
    for a in c.split(" "):
        if a in l:
            ap = ao.close(a)
            Speako(f"Closing {a}")

        if a in d:
            ap = webbrowser.open("http://www.chrome.com")
            Speak(f"Closing {a}")


# youtube search
def youtube(c):
    if "for" in c:
        s = c.split("for")[-1]
    elif "play" in c:
        s = c.split("play")[-1]
    elif "on" in c:
        s = c.split("play")[1]
    url = "https://www.youtube.com/results?search_query=" + s
    webbrowser.open(url)
    Speak("Here is what I found for " + s + " on youtube.")


# google search
def google(c):
    s = c.split("for")[-1]
    url = "https://google.com/search?q=" + s
    webbrowser.open(url)
    Speak("Here is what I found for " + s + " on google.")


# google maps
def maps(c):
    if "is" in c:
        s = c.split("is")[-1]
    elif "of" in c:
        s = c.split("of")[-1]
    url = "https://www.google.com/maps/place/" + s
    webbrowser.open(url)
    Speak("Here is what I found for " + s + " on google maps.")


# spotify search
def song(c):
    if "song" in c:
        s = c.split("song")[-1]
    elif "play" in c:
        s = c.split("play")[-1]
    url = "https://open.spotify.com/search/" + s
    webbrowser.open(url)
    Speak(f"Playing " + s)


# jokes
def joke():
    j = pyjokes.get_joke()
    Speak(j)


def commands():
    greet()
    while True:
        try:
            c = Execute()
            cd = c.lower()

            if "how are you" in cd:
                Speak("I am fine. Thank you!")
                Speak("How are you?")

            elif "your name" in cd:
                Speak("My name is Shri.")

            elif ("who are you" in cd) or ("about you" in cd):
                Speak(
                    "I am Shri - a Smart Human Replicating Intelligence. I am here to make your life easy. Yes,I can't take away your pains but can do your work."
                )

            elif "what is my name" in cd:
                Speak(f"Your name is {name}.")

            elif "is it going" in cd:
                Speak("I am going good. What about you?")

            elif "open" in cd:
                openit(cd)

            elif "close" in cd:
                closeit(cd)
            elif ("joke" in cd) or ("entertain") in cd:
                joke()

            elif "date" in cd:
                t = date.today()
                Speak(
                    f"Today is {t.day}th day of {t.month}th month of the year {t.year}"
                )

            elif "time" in cd:
                t = datetime.now()
                Speak(
                    f"Time is {t.hour} hour {t.minute} minutes and {t.second} seconds."
                )

            elif "spotify" in cd:
                song(cd)

            elif (
                ("search" in cd)
                or ("google" in cd)
                or ("more" in cd)
                or ("show" in cd)
                or ("tell" in cd)
                or ("know" in cd)
            ):
                google(cd)

            elif ("location" in cd) or ("where" in cd):
                maps(cd)

            elif ("youtube" in cd) or ("play" in cd):
                youtube(cd)

            elif ("bye" in cd) or ("exit" in cd) or ("quit" in cd) or ("sleep" in cd):
                Speak("Have a great day!!")
                break
        except:
            Speak("Sorry, I cannot do that.")


commands()
