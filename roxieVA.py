import speech_recognition as sr
import pyttsx3
import datetime as dt
import pywhatkit as pk
import wikipedia as wiki

listener = sr.Recognizer()

speaker = pyttsx3.init()

""" RATE"""
rate = speaker.getProperty('rate')   # getting details of current speaking rate                  #printing current voice rate
speaker.setProperty('rate', 150)     # setting up new voice rate

"""VOICE
voices = speaker.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
speaker.setProperty('voice', voices[1].id)   #changing index, cha"""

def speak(text):
    speaker.say('yes boss!,'+text)
    speaker.runAndWait()
def speak_ex(text):
    speaker.say(text)
    speaker.runAndWait()


va_name = "roxie"
speak_ex("I am your " + va_name + ",tell me mam")
def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print("Say something!")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if va_name in command:
                command = command.replace(va_name + " ", '')
               # print(command)
                #speak(command)
    except:
        print("Check your Microphone")
    return command
while True:
    user_command = take_command()
    if 'close' in user_command:
        print("See you. I will be there when ever you call me")
        speak("See you. I will be there when ever you call me")
        break
    elif 'time' in user_command:
        cur_time = dt.datetime.now().strftime('%I:%M %p')
        print(cur_time)
        speak(f"The current time is {cur_time}")
    elif 'play' in user_command:
        user_command = user_command.replace('play', '')
        print('Playing'+user_command)
        speak('Playing' + user_command + '    enjoy boss')
        pk.playonyt(user_command)
        break
    elif 'search for ' in user_command or 'google' in user_command:
        user_name = user_command.replace('search for ', ' ')
        user_name = user_command.replace('google ', '')
        print('Searching for ' + user_name)
        speak('Searching for ' + user_name)
        pk.search(user_command)
    elif 'who is ' in user_command or 'what is ' in user_command:
        user_command = user_command.replace('Who is ', '')
        user_command = user_command.replace('What is ', '')
        info = wiki.summary(user_command, 2)
        print(info)
        speak(info)
    elif 'weather' in user_command:
        weather = pk.search(user_command)
        speak(weather)
    elif 'who are you' in user_command:
        speak_ex('I am your Virtual Assistant ,ask whatever you want')
    else:
        speak_ex('Sorry, I don\'t understand you')