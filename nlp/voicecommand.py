import speech_recognition as sr

import os

def listening_mic():
    mic = sr.Recognizer()

    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)
        print("please, say something: ")
        audio = mic.listen(source)
    
    try:
        phrase = mic.recognize_google(audio, language='en-US')

        if "browser" in phrase:
            os.system("start Chrome.exe")
            return False
        elif "exit" in phrase:
            return True
    except Exception as exc:
        print("error: {exc}")