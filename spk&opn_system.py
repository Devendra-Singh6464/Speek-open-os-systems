import speech_recognition as sr
import pyttsx3
import os

# initialize the recongnizer
r = sr.Recognizer()

# function to convert text to
# speech
def Speaksytm(command):
    
    # Indentatize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# loop infinitely for user to
# speak
while(True):
    
    # Exception handling to handle    
    # Exceptions at the Runtime
    try:
        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recorgnizer
            # adjuct the enrgy threshold based on
            r.adjust_for_ambient_noise(source2, duration=0.2)
            
            # listens for the user's input
            audio2 = r.listen(source2)
            
            # using google to recorgnize audio2
            open = r.recognize_google(audio2)
            open = open.lower()
            print("Did you say ", open)
            Speaksytm(open)
            if open == "notepad":
                print("Redy to open Notepade: ")
                os.system("notepad")
            elif open == "calculator":
                print("Redy to open calculator: ")
                os.system("calc")
            elif open == "paint":
                print("Redty to open paint: ")
                os.system("mspaint")


    except sr.RequestError as e:
        print("Could not request result;, {0}".format(e))
    except sr.UnknownValueError:
        print("Unknown error occured")

