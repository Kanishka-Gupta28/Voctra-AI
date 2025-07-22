import speech_recognition as sr
import webbrowser
import pyttsx3
import MusicLibrary
import requests

#pip install pocketsphinx
recognizer=sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    newsapi="d5733ea166be4f1e85dadbe089d4747e"

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = MusicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=d5733ea166be4f1e85dadbe089d4747e")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])


if __name__ == "__main__":
    speak("Initializing jarvis...")
    while True:
        #listen for the wake word jarvis
        #obtain audio from the microphone
        r=sr.Recognizer()
        

        print("recognizing")
        try:
            with sr.Microphone() as source:
                print("listening...")
                audio=r.listen(source, timeout=2 , phrase_time_limit=1)
            word=r.recognize_google(audio)
            if(word.lower() =="jarvis"):
                speak("ya")
                #listen for command
                with sr.Microphone() as source:
                    print("jarvis active...")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
            print("error; {0}".format(e))