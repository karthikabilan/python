from hashlib import new
from importlib.resources import path
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib




print("Initializing Jarvis..............")
MASTER="tony"
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    print(hour)
    if hour>=0 and hour<12:
        speak("Good Morning.."+MASTER)
    elif hour>=12 and hour<18:
        speak("Good Afternoon.. "+MASTER)
    else:
        speak("GoodEvening.."+MASTER)
   
    speak("Hi I am jarvis......,how may I help you............................?")

def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio=r.listen(source)

    try:
        print("Recognizing")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        print("say that again please")
        query=None
    return (query)

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('jarvis.hackathon1@gmail.com','jarvis@123')
    server.sendmail("elonmusk.hackathon1@gmail.com",to,content)
    server.close()
speak("Initializing Jarvis....................... ")
wishMe()
query=takeCommand()

if 'wikipedia'in query.lower():
    speak('Searching wikipedia...')
    query= query.replace("wikipedia", "")
    results=wikipedia.summary(query,sentences=2)
    print(results)
    speak(results)
 

elif 'open youtube' in query.lower():
    webbrowser.open("youtube.com")

elif 'open google' in query.lower():
    webbrowser.open("google.com")
    
elif 'open reddit' in query.lower():
    webbrowser.open("reddit.com")

elif 'open instagram' in query.lower():
    webbrowser.open("instagram.com")

elif 'open spotify'in query.lower():
    webbrowser.open("spotify.com")

elif'open telegram'in query.lower():
    webbrowser.open("telegram.com")

elif'open text book'in query.lower():
    webbrowser.open("https://www.tntextbooksonline.in/p/home.html")



elif 'play music' in query.lower():
    songs_dir = "C:\\Users\\DELL\\Desktop\\music"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir,songs[0]))

elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{MASTER} the time is {strTime}")

elif "who made you" in query or "who created you" in query:
            speak("I have been created by rj boys......")

elif 'open code'  in query.lower():
    codePath="C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
    os.startfile(codePath)

elif 'how are you' in query:
    speak("I am fine, Thank you")
    speak("How are you,Sir")
    
elif 'hi Jarvis' in query:
    speak("hello sir glad to meet you...")

elif 'fine' in query or "good" in query:
    speak("It's good to know that your fine........")

elif "where is" in query:
            query = query.replace("where is", "")
            location =query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.co.in/maps/place/" + location + "")
elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

elif 'email to tom' in query.lower():
    try:
        speak("What should I send")
        content = takeCommand()
        to = "karthikabilan.01@gmail.com"
        sendEmail(to,content)
        speak("Email has been sent sucessfully")

    except Exception as e:
        print(e)
    



    
    



    


