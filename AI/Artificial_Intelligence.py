import pyjokes
import pyttsx3
# pip install pyttsx3
import speech_recognition as sr
# pip install speechRecognition
import datetime
import wikipedia
# pip install wikipedia
import webbrowser
import os

import Alarm.Voice_Alarm
import Volume_Control.HandControlVolume
import screenshot.screenshot_AI
import weather.weather_AI
import Mouse_Gesture.virtual_mouse
import screen_brightness.Gesture_brightness
from Mouse_Gesture import virtual_mouse
from screen_brightness import Gesture_brightness
from screenshot import screenshot_AI
from Volume_Control import HandControlVolume
from weather import weather_AI

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon!")

    elif hour>=16 and hour<19:
        speak("Good Evening!")
    else:
        speak("good Night Sir!")
    speak("I am shreya sir . What could i do for you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'What do you mean by' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open c compiler' in query:
            webbrowser.open("https://www.onlinegdb.com/online_c_compiler")

        elif 'open java compiler' in query:
            webbrowser.open("https://www.jdoodle.com/online-java-compiler/")

        elif 'open gana' in query:
            webbrowser.open("https://gaana.com")

        elif 'play music' in query:
            music_dir = 'C:\\AK\\Audio'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "open control panel" in query:
            control = 'C:\\Users\\hp\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel'
            os.startfile(os.path.join(control))

        elif "command prompt" in query:
            pathw = 'C:\\Users\\hp\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt'
            os.startfile(os.path.join(pathw))

        elif "open run" in query:
            pathwq = 'C:\\Users\\hp\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Run'
            os.startfile(os.path.join(pathwq))

        elif "open Windows Administrative Tools" in query:
            pthn = 'C:\\Users\\hp\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Windows Administrative Tools'
            os.startfile(os.path.join(pthn))


        elif 'tell me the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, the time is {strTime}")

        elif 'set the alarm' in query:
            Alarm.Voice_Alarm.Alarm_code()

        elif 'take screenshot' in query:
            screenshot.screenshot_AI.take_screenshot()

        elif 'activate the mouse' in query:
            Mouse_Gesture.virtual_mouse.virtualmouse()

        elif 'screen brightness' in query:
            screen_brightness.Gesture_brightness.screen_bright_controlled()

        elif 'volume control' in query:
            Volume_Control.HandControlVolume.Volume_Control()

        elif 'tell me the weather' in query:
            weather.weather_AI.Get_weather()

        elif 'crack me a joke' in query:
            speak(pyjokes.get_joke())

        elif 'shut down the system' in query:
            speak("shut down sequence has been activated")
            os.system("shutdown /s /t 3")

        elif 'restart the system' in query:
            speak("restart sequence has been started")
            os.system("restart /r /t 3")

        elif "don't do anything" in query:
            print("Okay Sir")
            speak("Okay Sir. You can Call Me Anytime")
            break