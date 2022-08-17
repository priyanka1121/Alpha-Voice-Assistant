import pygame
import os
import datetime
import random
import psutil
import socket
import threading
import pyttsx3
from GoogleFeatures import googlecalenderfeatures, googlenewsfeatures, googleTranslate
from googletrans import Translator
from tkinter import *
from tkinter import simpledialog, Tk
from PIL import ImageTk, Image
import speech_recognition as sr
from AppFeatures import features, wolframalph
import smtplib
import wikipedia
import pyjokes
import pyautogui
import random
import json
import requests
from urllib.request import urlopen
import wolframalpha
import time
import sys
import subprocess
import cv2
import webbrowser as wb
import ssl

destroy= False
state = 0
user_panel_flag = False
REMOTE_SERVER = "1.1.1.1"
HEIGHT, WIDTH = 350, 250
X_POS, Y_POS = '500', '0'
app_music = ['open-ended', 'unsure', 'when', 'sorted']
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
wolframalpha_app_id = 'KWEUK9-LUPRRKAP58'
pygame.mixer.init()


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def speak(audio):
    print('Alpha:', audio)
    engine.say(audio)
    engine.runAndWait()





def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6
        r.phrase_threshold = 0.290
        r.energy_threshold = 368
        audio = r.listen(source)
        said = ''
        try:
            said = r.recognize_google(audio, language='en-in')
            print("You say : " + said)

        except Exception as e:
            print("Exception: Sorry...I couldn't  recognize what u said " + str(e))
            (print('Say that again please ....'))
            speak('Could u please say that again ...')
            said = myCommand()
    return said


def wake_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Waiting to be called \
             Listening...")
        r.pause_threshold = 0.7
        r.phrase_threshold = 0.3
        r.energy_threshold = 375
        audio = r.listen(source)
        try:
            wake_cmd = r.recognize_google(audio, language='en-in')
            print("U said : " + wake_cmd)

        except Exception as e:
            wake_cmd = wake_command()
    return wake_cmd


def wakeWord(text):
    WAKE_WORDS = ['hey', 'hi', 'hello','hola']
    text = text.lower()
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True

    return False


def wishMe():
    all_checks_flag = True
    internet_connection_status = check_internet_connection()
    battery_percent, plugged = get_battery_status()

    GREETING_INPUTS = ['hey there', 'wassup', 'Hello']
    GREETING_RESPONSES = ['hello', 'hey there']
    HELP_GREET_RESPONSES = ['how may I help you..', 'I am now ready to take your commands..',
                            'Please tell me what I can do for you ?']

    hour = int(datetime.datetime.now().hour)
    if 0 < hour < 12:
        speak(random.choice(GREETING_INPUTS))
        speak('Good Morning...')
        speak('I am Alpha... Your Virtal Assistant')
        #speak(features.getDate())
        if internet_connection_status:
            # speak(features.getweather('Noida'))
            if battery_percent <= 25 and plugged == 'Not Plugged In':
                speak("I can see that your battery is less than 25%/"
                      "I would advice you to plug in you charger")
                speak(random.choice(HELP_GREET_RESPONSES))
                # return all_checks_flag
            else:
                speak(random.choice(HELP_GREET_RESPONSES))
                # return all_checks_flag
        else:
            speak("I can see that you are not connect to Internet/"
                  "I would suggest you to connect to internet for seemless service")
            all_checks_flag = False
            # return all_checks_flag


    elif 12 <= hour <= 18:
        speak(random.choice(GREETING_INPUTS))
        speak('Good Afternoon...')
        speak('I am Alpha.... Your Virtal Assistant')
        #speak(features.getDate())
        if internet_connection_status:
            # speak(features.getweather('Noida'))
            if battery_percent <= 25 and plugged == 'Not Plugged In':
                speak("I can see that your battery is less than 25%\
                          I would advice you to plug in you charger")
                speak(random.choice(HELP_GREET_RESPONSES))
                # return all_checks_flag
            else:
                speak(random.choice(HELP_GREET_RESPONSES))
                # return all_checks_flag
        else:
            speak("I can see that you are not connect to Internet/"
                  "I would suggest you to connect to internet for seemless service")
            all_checks_flag = False
            # return all_checks_flag

    else:
        speak(random.choice(GREETING_INPUTS))
        speak('Good Evening..')
        speak('I am Alpha... Your Virtal Assistant')
        #speak(features.getDate())
        if internet_connection_status:
            # speak(features.getweather('Noida'))
            if battery_percent <= 25 and plugged == 'Not Plugged In':
                speak("I can see that your battery is less than 25%"
                      "I would advice you to plug in you charger")
                speak(random.choice(HELP_GREET_RESPONSES))
                # return all_checks_flag
            else:
                speak(random.choice(HELP_GREET_RESPONSES))
                # return all_checks_flag
        else:
            speak("I can see that you are not connect to Internet/"
                  "I would suggest you to connect to internet for seemless service")
            all_checks_flag = False
            # return all_checks_flag


def get_typed_query():
    query = simpledialog.askstring("", "Please type your command ")
    #print(query)
    return str(query)


def get_battery_status():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    if not plugged:
        plugged = "Not Plugged In"
    else:
        plugged = "Plugged In"
    print(str(percent) + '% | ' + plugged)
    return percent, plugged


def get_battery_image_name(battery_percent, plugged_status):
    if plugged_status == "Plugged In":
        return "battery_charging.png"
    else:
        if battery_percent <= 25:
            return "battery_25.png"
        elif battery_percent <= 50:
            return "battery_50.png"
        elif battery_percent <= 75:
            return "battery_75.png"
        else:
            return "battery_100.png"


def check_internet_connection():
    try:
        host = socket.gethostbyname(REMOTE_SERVER)
        s = socket.create_connection((host, 80), 2)
        s.close()
        return True
    except:
        pass
    return False


def get_internet_connection_img(connection_status):
    if connection_status:
        return "wifi.png"
    else:
        return "no-wifi.png"

notification_folder = resource_path('Notification_sounds')
IMAGE_PATH = resource_path('Images/Background/APP-BG.jpg')

class Widget:

    def __init__(self):
        battery_percent, plugged = get_battery_status()
        connection_status = check_internet_connection()
        self.root = Tk()
        self.root.geometry('{}x{}+{}+{}'.format(HEIGHT, WIDTH, X_POS, Y_POS))
        self.root.resizable(0, 0)
        self.root.iconbitmap(resource_path("C:/Users/hp/AI UI/alpha-master/icon.ico"))

        img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((HEIGHT, WIDTH - 120), Image.ANTIALIAS))




        panel_main = Label(self.root, image=img)
        panel_main.pack(expand="no", side='top')
        self.root.title('Alpha')


        battery_img_file = get_battery_image_name(battery_percent, plugged)
        print(resource_path("Images/Battery_status\\") + battery_img_file)
        battery_img = ImageTk.PhotoImage(file=resource_path("Images/Battery_status\\") + battery_img_file)

        internet_connection_img_file = get_internet_connection_img(connection_status)
        internet_connection_img = ImageTk.PhotoImage(
            file=resource_path("Images/Connection_status\\") + internet_connection_img_file)

        mike_img = ImageTk.PhotoImage(Image.open(resource_path("Images/Button_img/mike/mike.png")))
        close_button_img = PhotoImage(file=resource_path("Images/Button_img\\force_stop\\force-stop.png"))

        self.voice_command_on = PhotoImage(file=resource_path("Images/Button_img/listen_button\\toggle_on.png"))
        self.voice_command_off = PhotoImage(file=resource_path("Images/Button_img/listen_button\\toggle_off.png"))

        self.enable_keep_listening = Label(self.root, text="Enable Listening ", bg='gray26',
                                           font=('Black Ops One', 10, 'bold'),
                                           fg='white')
        self.enable_keep_listening.place(x=5, y=30)
        Battery_label = Label(self.root, text='Battery        ', font=('Black ops one', 10, 'bold'), bg='gray26',
                              fg='white').place(x=0, y=65)
        Connection_label = Label(self.root, text='Connection', font=('Black ops one', 10, 'bold'), bg='gray26',
                                 fg='white').place(x=0, y=85)
        self.Connection_img_label = Label(self.root, image=internet_connection_img).place(x=78, y=85)
        self.Battery_img_label = Label(self.root, image=battery_img).place(x=78, y=65)



        self.t_btn = Button(self.root, image=self.voice_command_off, border=0, bg='gray26',
                            activebackground='gray26', command=self.voice_command_activation_switch)
        self.t_btn.place(x=20, y=5)

        self.mike_button = Button(self.root, image=mike_img, font=('Black ops one', 10, 'bold'), bg='gray62',
                                  height='35',
                                  width='25', border=0, command=self.clicked)
        self.mike_button.place(x=310, y=15)
        self.type_query_button = Button(self.root, text="Type Command", font=('Black ops one', 10, 'bold'), bg='white',
                                        border=0,
                                        command=self.typed)
        self.type_query_button.place(x=150, y=15)
        close_button = Button(self.root, image = close_button_img, border= 0,font=('Black Ops One', 10, 'bold'), bg='deepSkyBlue', fg='white',
                      command=self.destroy_root).place(x=310,y=65)


        self.userText = StringVar()
        self.userText.set('Click on Mic Button to Give commands \
                          or use Type Button to Type Commands')

        userFrame = LabelFrame(self.root, text="USER", font=('Black ops one', 10, 'bold'))
        userFrame.pack(fill="both", expand="yes", side='bottom')

        User_Message = Message(userFrame, textvariable=self.userText, bg='gray24', fg='white')
        User_Message.config(font=("Comic Sans MS", 10, 'bold'))
        User_Message.pack(fill='both', expand='no', )

        wishMe()
        self.root.mainloop()

    def destroy_root(self):
        destroy = True
        sys.exit()
        self.root.destroy()

    def sendEmail(to,content):
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        #for this function,you must enable low security in your gmail which you are going to  use as sender

        server.login('masteralphaassistant122@gmail.com','qwer@43221')
        server.sendmail('masteralphaassistant122@gmail.com',to,content)
        server.close()

    
        
    
    

    def TakeCommand():
        r=sr.Recognizer()
        with sr.Microphone() as source:
            
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        try:
            
            query = r.recognize_google(audio,language='en-US')
            print(query)

        except Exception as e:
            print(e)
            print("Say that again please.......")
            return "None"
        return query

    def execute(self, query):
        if not destroy:
            query = query.lower()
            if 'wikipedia' in query:
                self.userText.set("USER:" + query)
                self.root.update()
                speak('searching that on wikipedia')
                # query = query.replace("wikipedia", "")
                wiki_result = features.searchonWiki(query.replace("wikipedia","").replace("on" , ""))
                speak("According to wikipedia  " + wiki_result)
                self.userText.set("According to wikipedia  " + wiki_result)
                self.root.update()
                return False  

            elif 'open google' in query:
                self.userText.set("USER:" + query)
                self.root.update()
                speak('Opening Google for you')
                self.userText.set('Opening Google for you')
                self.root.update()
                features.openGoogle()
                return False


            elif 'open youtube' in query:
                self.userText.set("USER:" + query)
                self.root.update()
                speak('opening Youtube for you ')
                self.userText.set('opening Youtube for you')
                self.root.update()
                features.openYoutube()
                return False

            
            elif 'search youtube' in query:
                speak('what should i search?') 
                search_Term = myCommand().lower()
                speak("Here we go to YOUTUBE!") 
                wb.open('https://www.youtube.com/results?search_query='+search_Term)
            

            elif 'search in chrome' in query:
                speak('What should i search?') 
                #chromepath is location of chrome's installation on computer
                search = myCommand().lower()
                speak("here we go")
                wb.open('https://www.google.com/search?q='+search)


            elif 'close chrome' in query:
                os.system("taskkill /f /im " + "chrome.exe")
                speak("Closed Chrome Browser")
                return False



            elif 'tell me the weather' in query:
                speak('Of Which location ?')
                city_name = myCommand()
                features.getweather(city_name)
                return False

            elif 'tell me weather' in query:
                speak('of which location ?')

                city_name = myCommand()
                features.getweather(city_name)
                return False

            elif "show my events" in query:
                # googlecalenderfeatures.googleCalender()
                speak("how many event you want")
                query = myCommand().lower()
                service = googlecalenderfeatures.google_calender()
                googlecalenderfeatures.get_events(query, service)
                return False


            elif 'Open ms office' in query:
                speak("opening MS Word")
                power = "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Microsoft Office 2013/Word 2013.lnk"
                os.startfile(power)


            elif "news" in query:
                speak("Of which region")
                region = myCommand().lower()
                news_list = googlenewsfeatures.getgooglenews(5, region)
                speak("Presenting you todays headlines...")

                for news in news_list:
                    print(news)
                    speak(news)
                    self.userText.set(news)
                    self.root.update()
                speak("That's all for today")
                return False

            elif "save my event" in query:
                speak("event summary ")
                summary = myCommand().lower()
                speak("event start date")
                #speak("say like on or from january 2nd event start date sir")
                startDate = myCommand().lower()

                speak("and event end date ")
                endDate = myCommand().lower()
                service = googlecalenderfeatures.set_event(summary, startDate, endDate)

            

            elif "translate " in query:
                statement = query.replace('translate ', '')
                speak("In which language?")
                dest = myCommand()
                speak(googleTranslate.langTranslator(statement, dest))
                return False
                self.userText.set(dest)
                self.root.update()

            

            elif 'activate alpha' in query:
                speak("Alpha mode activated")
                query = myCommand()
                while True:
                    speak(wolframalph.wolframalphafunc(query))
                    query = myCommand().lower()
                    if 'deactivate alpha' in query:
                        speak("Alpha mode deactivated...")
                        break
                    else:
                        continue
                return False

            elif 'search on google' in query:
                speak('What should i search?')
                search_Term = myCommand().lower()
                speak('Searching.......')
                wb.open('https://www.google.com/search?q='+search_Term) 

            elif 'stop listening' in query:
                speak('Please call me whenever needed')
                return True


            elif 'write a note' in query:
                speak("What should i write?") 
                notes= myCommand()
                file= open('notes.txt','w')
                speak("Should I Include Date and Time?")
                ans= myCommand()
                if 'yes' in ans or 'sure' in ans:
                    strTime= datetime.datetime.now().strftime("%H:%M:%S")
                    file.write(strTime)
                    file.write(":-")
                    file.write(notes)
                    speak('Done taking notes!')
                else:
                    speak("okay done taking notes")
                    file.write(notes)    


            elif 'show note' in query:
                  speak('Showing notes')
                  file=open('notes.txt','r')
                  print(file.read())
                  speak(file.read())
                  self.userText.set(file.read())
                  self.root.update() 

            elif 'screenshot' in query:
                    screenshot()


            elif 'cpu' in query:
                    usage = str(psutil.cpu_percent())
                    speak('CPU is at'+usage)
                    battery = psutil.sensors_battery()
                    speak('Battery is at')
                    speak(battery.percent)
                    speak('percent')                       
                    self.userText.set(battery)
                    self.root.update()  


            elif 'joke' in query:
                my_joke = speak(pyjokes.get_joke())
                
            elif 'who made you' in query or 'who created you' in query or 'who discovered you' in query:
                speak('I was built by Khushi Sharma and Priyanka Gupta')
                print('I was built by Khushi Sharma and Priyanka Gupta')

            elif 'how are you' in query:
                speak('I am perfectly fine, and i hope you too!')  

            elif 'remember that' in query:
                speak("What should i remember?")
                memory=myCommand()
                speak("You asked me to remember that"+memory)
                remember = open('memory.txt','w')
                remember.write(memory)
                remember.close()

            elif 'do you remember anything' in query:
                remember=open('memory.txt','r') 
                speak('You asked me to remember that'+remember.read())

            elif 'where is' in query:
                query = query.replace("where is","")
                location = query
                speak("User asked to locate"+location)
                wb.open_new_tab("https://www.google.com/maps/place/"+location)


            elif 'calculate' in query:
                client = wolframalpha.Client(wolframalpha_app_id)
                indx = query.lower().split().index('calculate')
                query = query.split()[indx + 1:]
                res = client.query(''.join(query))
                answer = next(res.results).text
                print('The answer is: '+answer)
                speak('The answer is '+answer)
                self.userText.set(answer)
                self.root.update() 

            elif 'what is' in query or 'who is' in query:
                client = wolframalpha.Client(wolframalpha_app_id)
                res = client.query(query) 

                try:
                    print(next(res.results).text)
                    speak(next(res.results).text)
                except StopIteration:
                    speak("Sorry no result found")
                    print("No Results")

            elif 'stop listening' in query:
                speak('For how many second you want me to stop listening to your commands?') 
                ans = int(TakeCommand()) 
                time.sleep(ans)
                print(ans)    


            elif 'log out' in query:
                os.system("shutdown -l") 
            elif 'restart' in query:
                os.syste("shutdown /r /t 1") 
            elif 'shutdown' in query: 
                os.system("shutdown /s /t 1")


            elif 'install library' in query:
                 subprocess.run(input(" "),shell=True)

            elif 'click photo' in query:
                video = cv2.VideoCapture(0)
                while True:
                    check,frame = video.read()
                    grey=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    cv2.imshow("Master",grey)
                    cv2.waitKey(0)
                    time.sleep(5)
                video.release()
                cv2.destroyAllWindowws()

            elif 'send email' in query:
                try:
                    speak("What should i say")
                    content=myCommand()
                    #provide receiver email address
                    to = "priyankagupt211@gmail"
                    sendEmail(to,content)
                    speak(content)
                    speak("Email has been sent!")

                except Exception as e:
                    print(e)
                    speak("Unable to send Email.")


            elif 'tell me date' in query:
                today = datetime.date.today()
                speak(today)        

            elif 'tell me time' in query:
                t = time.localtime()
                current_time = time.strftime("%H:%M:%S", t)
                speak(current_time)
                
            elif 'open presentation' in query:
                speak("opening Power Point presentation")
                power = r"C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Microsoft Office 2013/PowerPoint 2013.lnk"
                os.startfile(power)

            elif 'open Word' in query:
                speak("opening ms word...")
                power = r"C:/Users/hp/Desktop/Priyanka/alphaMaster/doc1.docx"
                os.system(power)


            elif 'open prompt' in query:
                speak("Opening command prompt")
                os.system("start /wait cmd /k /c {command}")

            elif 'stock price' in query:
                speak("what should I search")
                search_term = myCommand().lower()
                url = "https://www.google.com/search?q=stock+price+of= " + search_term
                wb.get().open(url)
                speak("Here is what I found for " + search_term + " on google")

            elif 'play music' in query or "play song" in query:
                speak("Here what I found")
                # music_dir = "G:\\Song"
                music_dir = "C:/Users/hp/Desktop/Priyanka/alphaMaster/music"
                songs = os.listdir(music_dir)
                print(songs)    
                random = os.startfile(os.path.join(music_dir, songs[1]))        

            elif 'please quit' in query or 'ok bye' in query or 'stop' in query:
                speak('Goodbye and Have a nice day')
                sys.exit()

    def clicked(self):
       print("in clicked")
       pygame.mixer.music.load(notification_folder + '/' + app_music[2] + '.mp3')
       pygame.mixer.music.set_volume(1.5)
       pygame.mixer.music.play()

       self.t_btn.config(state='disabled')
       self.type_query_button.config(state='disabled')
       self.root.update()

       self.userText.set('Listening...')
       query = myCommand()
       print(query)
       self.userText.set(query)
       query = query.lower()

       self.execute(query)

       self.t_btn.config(state='normal')
       self.type_query_button.config(state='normal')
       self.root.update()
       return

    def typed(self):
        print("in typed")
        pygame.mixer.music.load(notification_folder + '/' + app_music[1] + '.mp3')
        pygame.mixer.music.set_volume(1.5)
        pygame.mixer.music.play()

        self.t_btn.config(state='disabled')
        self.mike_button.config(state='disabled')
        self.root.update()

        query = get_typed_query()
        if query != 'None':
            self.execute(query)

        self.t_btn.config(state='normal')
        self.mike_button.config(state='normal')
        self.root.update()
        return

    def voice_command_activation_switch(self):
        global state
        internet_connection_status = check_internet_connection()
        if internet_connection_status:

            if state == 0:
                print("in state == 0 of vcas")
                pygame.mixer.music.load(notification_folder + '/' + app_music[1] + '.mp3')
                pygame.mixer.music.set_volume(1.5)
                pygame.mixer.music.play()
                self.t_btn.config(image=self.voice_command_on)
                self.t_btn.config(state='disabled')
                self.mike_button.config(state='disabled')
                self.enable_keep_listening.config(text="Listening..", font=('Black Ops One', 10, 'bold'))
                self.t_btn.config(state='disabled')
                self.root.update()
                state = 1

                # self.listen_continuously()
                threading.Thread(target=self.listen_continuously()).start()
                self.t_btn.config(state='normal')
                self.mike_button.config(state='normal')
                self.root.update()
                return
        else:
            speak("I can see that you are not connected to Internet...."
                  "I would suggest you to connect to Internet for seemless service")
            self.t_btn.config(image=self.voice_command_off)
            self.enable_keep_listening.config(text=" Enable Listening", font=('Black Ops One', 10, 'bold'))
            self.root.update()
            state = 0

    def listen_continuously(self):
        global state ,destroy
        #print("state in listen continuouslly fn is :" + str(state))
        while True and not destroy :
            query = wake_command()
            #print("in listen continuously query recieved is:" + query)
            if state == 1 and 'stop listening' not in query:
                #print("state in listen continuouslly fn if loop is :" + str(state))

                if wakeWord(query):
                    print("waked up successfully")
                    speak("How may I help you sir")
                    command = myCommand()
                    stop_flag = self.execute(command)
                    if stop_flag:
                        break
                    else:
                        continue

                else:
                    continue
            else:
                speak('Listening has been stoped now')
                self.t_btn.config(image=self.voice_command_off)
                self.t_btn.config(state='normal')
                pygame.mixer.music.load(notification_folder + '/' + app_music[2] + '.mp3')
                pygame.mixer.music.set_volume(1.5)
                pygame.mixer.music.play()
                self.enable_keep_listening.config(text=" Enable Listening", font=('Black Ops One', 10, 'bold'))
                state = 0
                break
        self.t_btn.config(image=self.voice_command_off)
        self.t_btn.config(state='normal')
        pygame.mixer.music.load(notification_folder + '/' + app_music[2] + '.mp3')
        pygame.mixer.music.set_volume(1.5)
        pygame.mixer.music.play()
        self.enable_keep_listening.config(text=" Enable Listening", font=('Black Ops One', 10, 'bold'))
        self.root.update()
        state = 0


if __name__ == '__main__':
    widget = Widget()

