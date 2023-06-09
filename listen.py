# takes audio inputs and coverts them to recognizable form
import speech_recognition as sr  # to get audio input and recognize it into text form
from googletrans import Translator  # to translate hindi to english

# Listen function(Hindi or English)
# To listen in hindi(as it is then given for translation)
def Listen():
    m = sr.Recognizer()

    with sr.Microphone() as source:
        print("I am Listening........")
        m.energy_threshold = 100
        m.pause_threshold = 1
        audio = m.listen(source, 0, 8)
        # Listens everything till 8 sec. If we stop before, then it cuts there itself.

        try:
            print("Recognizing.....")
            query = m.recognize_google(
                audio, language="hi"
            )  # Setting language as hindi
        except:
            return ""  # If nothing is said
        query = str(query).lower()
        return query


# To hear what is said as it is without any translation
def Listeno():
    m = sr.Recognizer()

    with sr.Microphone() as source:
        print("I am Listening........")
        m.energy_threshold = 100
        m.pause_threshold = 1
        audio = m.listen(source, 0, 8)
        # Listens everything till 8 sec. If we stop before, then it cuts there itself.

        try:
            print("Recognizing.....")
            query = m.recognize_google(
                audio, language="en"
            )  # Setting language as hindi
        except:
            return ""  # If nothing is said
        query = str(query).lower()
        return query

    
# Translation function
def Translate_HinToEng(t):
    l = str(t)
    trans = Translator()
    result = trans.translate(l)
    # translate(l,"x"), where x is the lang. in which it has to be translated. defaulf="eng"
    d = result.text
    print(f"You:{d}")
    return d


# Connecting listen and translation
def Execute():
    query = Listen()
    data = Translate_HinToEng(query)
    return data
