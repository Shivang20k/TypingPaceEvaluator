
import random
from tkinter import *
from tkinter import messagebox
from datetime import date
import time
from timeit import default_timer as timer
import textwrap
import pyttsx3
import speech_recognition as sr
import os
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

class window:
    messagebox.showinfo("!!IMPORTANT!!","Press \"Enter\" to complete Proctoring.")
    import proct
    check=proct.h
    if check==0:
        sys.exit()
    time.sleep(2)
    messagebox.showinfo("Instructions"," 1. PRESS \"READY\" button then start typing\n 2. PRESS \"SUBMIT\" button when done with typing\n 3. PRESS \"CLEAR\" button to try again")

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def speak(self,audio):
        engine.say(audio)
        engine.runAndWait()
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def takeCommand(ask=False):
        #It takes microphone input from the user and returns string output
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')#hi-IN
            print("User said:",query)
        except Exception as e:
            # print(e)
            print("Say that again please...")
            #speak("Say that again please...")
            sample=["with us lower your error rate and increase your typing speed at the same time","the ten finger method is a very established technique to efficiently use your computer keyboard with some practice and the correct finger positions you can type blindly on the keyboard","this is a sample text incase the your voice is not well captured by the microphone please respeak or use this sample text","the first systems of writing developed and used by the germanic peoples were runic alphabets the runes functioned as letters but they were much more than just letters","ruines were traditionally carved onto stone wood bone metal or some similarly hard surface rather than drawn with ink and pen on parchment this explains their sharp angular form","one of the greatest professional wrestlers of all time the undertaker is a seventime world heavyweight champion having held the championship four times and the world heavyweight championship three times."]
            random.shuffle(sample)

            return sample[1]
        return query

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def getTextInput(self):# takes users inputed text as well time taken for typing
        #==========================logic of time calculation==================================

        self.st=self.start#this gets beginning time from time_cal() i.e. READY
        self.end=time.time()#this takes takes time when submitted
        self.time_taken=round(self.end-self.st)-2# diff. in both times i.e. total time taken
        print("Time taken:",self.time_taken,"sec.")# diff. in both times i.e. total time taken
        self.speak("Time Taken is")
        self.speak(self.time_taken)
        self.speak("seconds ")
        self.speak("and ")

        EntryField_label=Label(root,text=str(self.time_taken)+" sec.",bg="coral1",fg="yellow",font=("times new roman",19,"bold"))
        EntryField_label.place(x=951,y=280)

        #==========================accuracy checking=========================================
        self.result=self.textExample.get(1.0, END+"-1c")#getting user inputted text
        self.list_input=self.result.split()#making a list outof input string,as .split gives liast
        self.list_speechtotext=self.value.split()
        self.ac=len(set(self.list_input)&set(self.list_speechtotext))#get correct no. of words
        self.ac_per=round(self.ac/len(set(self.list_speechtotext))*100)
        print("accuracy is",self.ac_per,"%")
        self.speak("Your accuracy is")
        self.speak(self.ac_per)
        self.speak("percent ")
        self.speak(" and")


        EntryField_label=Label(root,text=str(self.ac_per)+"%",bg="coral1",fg="yellow",font=("times new roman",19,"bold"))
        EntryField_label.place(x=951,y=400)

        #========================WPM check===================================================
        try:
            self.WPM=round(len(self.list_input)/self.time_taken*60)
            print("WPM:",self.WPM)
            self.speak("Your Words Per Minute is")
            self.speak(self.WPM)
        except ZeroDivisionError as err:
            self.WPM=0
            print("WPM: 0")
            self.speak("Your Words Per Minute is ZERO")

        EntryField_label=Label(root,text=str(self.WPM),bg="coral1",fg="yellow",font=("times new roman",19,"bold"))
        EntryField_label.place(x=951,y=508)
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def time_cal(self,i):
        if i==0:
            self.start=time.time()
        else:
            return(self.start)
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def clear(self):
        window(root)

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def __init__(self,root):
        self.root=root
        self.root.geometry("1065x600+0+0")
        self.root.title("Automated Typing Speed Evaluator")
        bg_color="#696969"
        title=Label(self.root,text="TYPING SPEED TEST",bd=9,relief=GROOVE,fg="mint cream",bg="springgreen2",font=("times new roman",30,"bold"),pady=2).pack(fill=X)#adding properties to title block

        #==================varaiables==============================================================================================
        self.EntryField=StringVar()
        self.value = self.takeCommand().lower()#"""This function wraps the input paragraph such that each line in the paragraph is at most width characters long. The wrap method returns a list of output lines. The returned list is empty if the wrapped output has no content."""
                        #remove "hello" in above line & remove hash above
        #===================================upper frame================================================================================================================================
        F1=LabelFrame(self.root,bd=5,relief=GROOVE,text="",font=("times new roman",19,"bold"),fg="white",bg=bg_color)#"f" is frame
        F1.place(x=5,y=68,relwidth=0.992,relheight=0.262)
        #==================================lower left frame============================================================================================================================
        F2=LabelFrame(self.root,bd=5,relief=GROOVE,text="",font=("times new roman",19,"bold"),fg="firebrick",bg="cyan")#"f" is frame
        F2.place(x=5,y=225,relwidth=0.992,relheight=0.669)
        #==================================lower right frame============================================================================================================================
        F3=LabelFrame(self.root,bd=5,relief=GROOVE,text="",font=("times new roman",19,"bold"),fg="firebrick",bg="coral1")#"f" is frame
        F3.place(x=705,y=225,relwidth=0.48,relheight=0.669)


        #====================================entry panel in left frame==========================================================================
        wrapper = textwrap.TextWrapper(width=85)
        self.word_list = wrapper.wrap(text=self.value)
        EntryField_label=Label(F1,text="Text For Verification:",bg=bg_color,fg="gold",font=("times new roman",22,"bold")).grid(row=0,column=0,padx=20,pady=5)
        j=0
        for i in self.word_list:#loop for geetting one line text in different lines wrapping
         EntryField_label=Label(F1,text=i,bg=bg_color,fg="thistle2",font=("times new roman",15,"bold")).grid(row=j,column=1,padx=20,pady=5)#it has text recgnized through speech to text
         j+=1#jugaad for not printing same label again & again on same row
        #=========================text widget input===================
        self.textExample=Text(root, height=10)
        self.textExample.place(x=58,y=280,relwidth=0.474,relheight=0.478)
        READY_BUTTON=Button(root,height=3, width=10, text="READY", command=self.time_cal(0) ,fg="beige",bg="cornflowerblue",bd=7,relief=GROOVE,font="arial 12 bold")
        READY_BUTTON.place(x=576,y=280)
        SUBMIT_BUTTON=Button(root,height=3, width=10, text="SUBMIT", command=self.getTextInput ,fg="beige",bg="cornflowerblue",bd=7,relief=GROOVE,font="arial 12 bold")
        SUBMIT_BUTTON.place(x=576,y=384)
        CLEAR_BUTTON=Button(root,height=3, width=10, text="CLEAR" , command=self.clear,fg="beige",bg="cornflowerblue",bd=7,relief=GROOVE,font="arial 12 bold")
        CLEAR_BUTTON.place(x=576,y=484)

        #========================frame to display your stats==========

        EntryField_label=Label(root,text="TIME TAKEN",bg="coral1",fg='OliveDrab1',font=("times new roman",19,"bold"))
        EntryField_label.place(x=732,y=280)

        EntryField_label=Label(root,text="ACCURACY",bg="coral1",fg='OliveDrab1',font=("times new roman",19,"bold"))
        EntryField_label.place(x=732,y=400)

        EntryField_label=Label(root,text="WPM",bg="coral1",fg='OliveDrab1',font=("times new roman",19,"bold"))
        EntryField_label.place(x=732,y=510)


root=Tk()
obj=window(root)
root.mainloop()
