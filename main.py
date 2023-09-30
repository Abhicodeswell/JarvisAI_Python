import webbrowser

import speech_recognition as sr
import openai
from config import apiKey
import os
import datetime

import win32com.client


def chat(prompt):
    openai.api_key = apiKey
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    ans = response["choices"][0]["text"]

    print(response["choices"][0]["text"])
    return ans


def ai(prompt):
    ans = f"OpenAI response for {prompt}\n*******************************************\n\n"
    openai.api_key = apiKey
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=347,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )



    print(response["choices"][0]["text"])
    ans += response["choices"][0]["text"]
    say("Do you want to save this file..Enter 'Y' to save 'N' to dismiss")
    x = input("Enter your option")
    if x=='Y':
        say("Saving File.....")
        if not os.path.exists("OpenAi"):
            os.mkdir("OpenAi")
        with open(f"OpenAi/{''.join(prompt.split('AI')[1:])}.txt", "w") as f:
            f.write(ans)
        say("File Saved successfully...")
        print("File saved Successfully...")
    else:
        say("OK no problem....")




def say(s):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(s)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language="en-in")
            print(f"User Said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I did not understand. Please repeat.")

            return "Unknown Value Error"
        except sr.RequestError as e:
            print(f"Error connecting to Google Speech Recognition service; {e}")
            return "Request Error"
        except Exception as e:
            print(f"An error occurred: {e}")
            return "Some Error Occurred!"










say("I am Jarvis AI What can i do for you sir...")
while True:
    print("Listening...")
    text = takeCommand()
    sites = [["youtube" , "https://youtube.com"] , ["google" , "https://www.google.com"], ["wikipedia","https://www.wikipedia.com"],["lottie","https://https://lottiefiles.com/"],["chat GPT","https://chat.openai.com/"]]
    for site in sites:
        if f"open {site[0]}".lower() in text.lower():
            say(f"Opening {site[0]} Sir!..")
            webbrowser.open(site[1])

    if "even numbers" in text:
        path = r"C:\Users\Arpit Singh\Downloads\meme_video.mp4"

        say("I am diverting this request to your father....")
        os.startfile(path)

        exit()

    elif "show networks" in text:
        say("Opening connected networks..")
        command = "netsh wlan show profile"
        os.system(command)
        say("Want to know Passwords...")
        p = input("Enter 'Y' to know password and 'N' to exit")
        if 'Y' in p:
            say("Enter network name..")

            net = input("Enter network..")
            say("Fetching Password...")
            os.system(command + " " + net + " key = clear")
            say("Password is KEY CONTENT in Security Settings..")
        else:
            say("Quiting..")
    elif "exit" in text:
        path = r"C:\Users\Arpit Singh\Downloads\meme2_video.mp4"
        os.startfile(path)
        break
    elif "open memes" in text:
        say("Opening memes..")
        webbrowser.open("https://memes.co.in/meme-templates/video/975/bhai-yaha-pe-kya-ho-raha-hai-meme-download-arpit-bala")

    elif "open camera" in text:
        path = r"C:\Users\Arpit Singh\Downloads\puneet_meme.mp4"
        say("Opening Camera...")
        os.system("start microsoft.windows.camera:")
    elif "control panel" in text:
        say("Opening Control Panel..")
        os.system("control panel")

    elif "open downloads" in text:
        say("Opening Downloads...")
        os.startfile(r"C:\Users\Arpit Singh\Downloads")

    elif "time" in text:
        say("Sir the time is...")
        hour = datetime.datetime.now().strftime("%H")
        min = datetime.datetime.now().strftime("%M")
        sec = datetime.datetime.now().strftime("%S")
        print(f"{hour}:{min}:{sec}")
        say(f"{hour} hours.. {min} minutes..")

    elif "make mood" in text:
        path = r"C:\Users\Arpit Singh\Downloads\tejaswi.mp3"
        os.startfile(path)

    elif "using AI" in text:
        say(f"Using artificial Intelligence generating{text.split('AI')[1:]}")
        ai(text)

    elif "bhai paise de do" in text:
        path = r"C:\Users\Arpit Singh\Downloads\puneet_meme.mp4"
        os.startfile(path)

    else:
         say(chat(text))












