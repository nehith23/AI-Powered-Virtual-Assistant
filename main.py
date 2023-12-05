import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

print("Initializing batman")
MASTER = "Luke"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#Speak function will speak/Pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

#This funtion will greet according to the corresponding time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour <12:
        speak("Morning!!!" + MASTER)

    elif hour>=12 and hour<18:
        speak("Good afternoon!!!" + MASTER)

    else:
        speak("Good Evening!!!" + MASTER)

    speak("I am your assistant. How may I help you?")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('nehith2002@gmail.com', 'password#1234')
    server.sendmail("lukeskywalker@gmail.com", to, content)
    server.close()

#This function will take input from microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Could you please repeat...")
        query = None

    return query

#main function
def main():
    speak("Initializing batman...")
    wishMe()
    query = takeCommand()

    #Logic for executing tasks as per the query
    if 'wikipedia' in query.lower():
        speak('searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences =2)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        #webbrowser.open('youtube.com')
        url = "youtube.com"
        chrome_path = '' #specify location
        webbrowser.get(chrome_path).open(url)

    elif 'open google' in query.lower():
        #webbrowser.open('youtube.com')
        url = "google.com"
        chrome_path = '' #specify location
        webbrowser.get(chrome_path).open(url)

    elif 'play music' in query.lower():
        songs_dir = "" #specify location
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")

    elif 'open code' in query.lower():
        codePath = "" #specify location
        os.startfile(codePath)
    
    elif 'email to xyz' in query.lower():
        try:
            speak("what to send")
            content = takeCommand()
            to = "xyz123@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent to xyz")
        except Exception as e:
            print(e)

main()