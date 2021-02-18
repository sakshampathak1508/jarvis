import pyttsx3
import datetime
import speech_recognition as sr
import os
import webbrowser,wikipedia
import pywhatkit as kit
import smtplib
from googlesearch import search
# time
# search 
# wikipedia
# search youtube 
# play youtube
# spotify
# send whatsapp message

phone_nums = {
    "Enter name" : "Enter your phone number",
}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def say(query):
    engine.say(query)
    engine.runAndWait()

def start():
    h_time = int(datetime.datetime.now().hour)
    if h_time>=0 and h_time<12:
        say("Good morning")
    elif h_time>=12 and h_time<=19:
        say("Good Afternoon")
    else:
        say("Good Evening")
    say("Hi i am jarvis. how may i help you")

def take_command():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Getting Your Voice...")
        rec.pause_threshold = 1
        audio = rec.listen(source)
    try:
        print("Listening")
        query = rec.recognize_google(audio,language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        print("Not able to hear say that again please")
        return "none"
    return query

def send_email(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('YourEMAILId@gmail.com', 'Your Password')
    server.sendmail('YourEMAILId@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    data = take_command().lower()
    if 'hi jarvis' or 'hey jarvis' in data:
        start()
    while True:
        my_query = take_command().lower()

        if 'search youtube' in my_query:
            say("What you want to search")
            data = take_command().lower()
            webbrowser.open('https://www.youtube.com/results?search_query='+data)
        
        elif 'play youtube' in my_query:
            say("What you want to play")
            data = take_command().lower()
            kit.playonyt(data)

        elif 'open' in my_query:
            web = take_command()
            webbrowser.open(web+".com")

        elif 'search' in my_query:
            say("Here are the browser results")
            webbrowser.open("https://www.google.com/?#q="+my_query[6:])
            for j in search(my_query, tld="co.in", num=10, stop=10, pause=2):
                print(j)

        elif 'wikipedia' in my_query:
            say('Searching Wikipedia...')
            my_query = my_query.replace("wikipedia", "")
            results = wikipedia.summary(my_query, sentences=1)
            say("According to Wikipedia")
            print(results)
            say(results)

        elif 'the time' in my_query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {strTime}")
            say(f"Sir, the time is {strTime}")

        elif 'play spotify' in my_query:
            path = "C:\\Users\\Vivek\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(path)

        elif 'send message' in my_query:
            try:
                say("Who is the reciever")
                reciever = take_command().lower()
                say("What is the message")
                msg = take_command()
                if reciever in phone_nums:
                    kit.sendwhatmsg("+91"+phone_nums[reciever],msg,int(datetime.datetime.now().hour), int(datetime.datetime.now().minute)+1)
                else:
                    say("The reciever is not in your contact list")
            except Exception as e:
                say("sorry sir . i am not able to send this message ")

        elif 'send email' in my_query:
            try:
                say("What should I say?")
                content = take_command()
                to = input("Enter email address: ")    
                send_email(to, content)
                say("Email has been sent!")
            except Exception as e:
                print(e)
                say("Sorry sir . I am not able to send this email")    

        elif 'quit' in my_query:
            say("thank you i would be pleased to help again")
            exit(1)
        


