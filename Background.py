#keeps running in background to detect the hotword to open the main file
import os                             #to start a new file from this file
import speech_recognition as sr       #to listen the command of user
def Listeno():
    m=sr.Recognizer()

    with sr.Microphone() as source:
        print("I am Listening........")
        m.energy_threshold=100
        m.pause_threshold=1
        audio=m.listen(source,0,8) 
        #Listens everything till 8 sec. If we stop before, then it cuts there itself.
    
        
        try:
            print("Recognizing.....")
            query=m.recognize_google(audio,language="en") #Setting language as hindi
        except:
            return "" #If nothing is said
        query=str(query).lower()
        return query


while True:
    p=Listeno()
    if "wake up" in p.lower():        # checks for the required phase
        os.startfile('C:\\Users\\vasoy\\OneDrive\\Desktop\\AI\\Body\\Main.py')    #run the file whose path is given
    else:
        print("No")
