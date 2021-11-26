# Importing required modules
import os
import pyttsx3
import speech_recognition as sr


# Creating class
class Shutdown:

    # Method to take choice commands as input
    def takeCommands(self):

        # Using Recognizer and Microphone Method for input voice commands
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening')

            # Number of seconds of non-speaking audio before
            # a phrase is considered complete
            r.pause_threshold = 0.7
            audio = r.listen(source)

            # Voice input is identified
            try:

                # Listening voice commands in indian english
                print("Recognizing")
                Query = r.recognize_google(audio, language='en-in')

                # Displaying the voice command
                print("the query is printed='", Query, "'")

            except Exception as e:

                # Displaying exception
                print(e)
                # Handling exception
                print("Say that again sir")
                return "None"
        return Query

    # Method for voice output
    def Speak(self, audio):

        # Constructor call for pyttsx3.init()
        engine = pyttsx3.init('sapi5')

        # Setting voice type and id
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(audio)
        engine.runAndWait()


    # Method to self shut down system
    def quitSelf(self):
        self.Speak("Hello Aditya, choose the commands for, first shutting down the computer, second restarting the computer")

        # Input voice command
        take = self.takeCommands()
        choice = take

        if choice == 'shutdown the computer':
            # Shutting down
            print("Shutting down the computer")
            self.Speak("Shutting down the computer sir")
            os.system("shutdown /s /t 5")

        if choice == 'restart the computer':
            print("restarting the computer")
            self.Speak("Restarting the computer sir")
            os.system("shutdown /r /t 5")

        if choice == "don't do anything":
            # Idle
            print("Thank u sir")
            self.Speak("Thank u sir")
# Driver code
if __name__ == '__main__':
    Maam = Shutdown()
    Maam.quitSelf()
