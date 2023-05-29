import pyttsx3 # conversion of text to speech          -pip install pyttsx3 
import speech_recognition as sr #recognizes your voice -pip install speechRecognition
import wikipedia #for wikipedia search                 -pip install wikipedia
import webbrowser #for opening websites                -pip install webbrowser  
from datetime import datetime            
engine = pyttsx3.init('sapi5') 
voices=engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)  #print(voices[0].id) can be used to check voice

def speak(audio):
    engine.say(audio)  # implements the audio
    engine.runAndWait() # without which the audio will not be audible

def greeting():
    speak ("hello human, i am turbo your assistant, how can i assist you?")

def takecommand(): #takes voice from user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

if __name__ =='__main__':
    greeting()
    while True:
        query= takecommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
    
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
    
        elif 'open greeksforgreeks' in query:
            speak("opening geeksforgeekse")
            webbrowser.open("geeksforgeeks.org")
    
        elif 'open twitter' in query:
            speak(" opening twitter")
            webbrowser.open("twitter.com")

        elif 'pinterest' in query:
            speak("opening pinterset")
            webbrowser.open("in.pinterest.com")

        elif 'opera' in query:
            speak("opening opera")
            webbrowser.open("opera.com")

        elif 'instagram' in query:
            speak("opening instagram")
            webbrowser.open("instagram.com")

        elif 'linkedin' in query:
            speak("opening linkedin")
            webbrowser.open("in.linkedin.com")

        elif 'netflix' in query:
            speak("opening netflix")
            webbrowser.open("netflix.com/in/")

        elif 'irctc' in query:
            speak("opening irctc")
            webbrowser.open("irctc.co.in/nget/train-search")

        elif 'the time' in query:
            current_time= datetime.now() 
            speak(current_time)  

        elif "hello" in query:
            speak("hello, is there something i can do for you")  

        elif "who are you" in query or "your name" in query:
            speak("I am Turbo, your dekstop assistant")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "bye" in query:
            speak("bye")
            quit()

        else:
            speak("Sorry i didnt understand")
            speak("Please say it again")

        


        
         
     


