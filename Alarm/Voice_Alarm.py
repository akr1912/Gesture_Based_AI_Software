import os
import pyttsx3
from datetime import datetime
import speech_recognition as sr

def Alarm_code():
    with sr.Microphone() as source:
        r = sr.Recognizer()
        print("Say Your Name")
        speak = pyttsx3.init()
        print("Listening")
        audio_data = r.record(source,duration=5)
        print("Recognizing...")
        text = r.recognize_google(audio_data)
        Name = text
        print(Name)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time is: ", current_time)
    with sr.Microphone() as source:
        r = sr.Recognizer()
        print("Say The Alarm Time (HH:MM) only")
        speak = pyttsx3.init()
        text = speak.say("Starting the Alarm" + Name)
        print("Listening")
        audio_data = r.record(source,duration=5)
        print("Recognizing...")
        time = r.recognize_google(audio_data)
        abhi = time[0] + time[1] + ":" + time[2] + time[3]
        print(abhi)

    while True:
        Standard_time = datetime.now().strftime("%H:%M")
        if abhi == Standard_time:
            count = 0
            while count <= 2:
                count = count + 1
                engine = pyttsx3.init()
                engine.say("Wake up" + Name)
                music_dir = 'C:\\AK\\Audio'
                songs = os.listdir(music_dir)
                # we have 30 songs so we can choose a number between 0 - 29 to play what song we like
                engine.runAndWait()
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            break

if __name__ == "__main__":
    Alarm_code()