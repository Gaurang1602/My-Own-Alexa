#pip install SpeechRecognition
#pip install pyttsx3-->> python text to speech
#pip install PyAudio
#pip install pywhatkit
#pip install pyjokes

import datetime
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
listener =sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)

    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('Current time is'+time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person,  2)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry , I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'who are you' in command:
        talk('I am Alexa , your AI Assistant')
    elif 'what can you do for me' in command:
        talk('I can play a song for you, I can tell you time , I can tell you jokes , I can tell you information about any person you want')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again')

while True:
    run_alexa()
    
    
