from tkinter import *
from tkinter import ttk
from tkinter import font
import winsound
import time
import calendar
import datetime
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
minute=0
def annoy(): for i in range(1, 10): winsound.Beep(i * 100, 200)

def current_time():
    seconds= calendar.timegm(time.gmtime())
    current_seconds=seconds%60
    minutes=seconds//60
    current_minutes=minutes%60
    hours=minutes//60
    current_hour=hours%24
    if current_hour >= 12:
        tag="PM"
    else:
        tag="AM"
    #set the time zone
    current_hour=current_hour -6
    #format the output
    timex=str(current_hour)+":" + str(current_minutes)+":"+str(current_seconds)+" "+tag
    #xreturn the output
    return timex
def quit(*args):
    root.destroy()
def show_time():
    time=current_time()
    #show the time
    txt.set(time)
    #trigger the tick after 1000ms
    root.after(1000,show_time)
    




#use tkinter lib for showing the clock
root=Tk()
root.attributes("-fullscreen", False)
root.configure(background='Blue')
root.bind("x",quit)
root.after(1000, show_time)

fnt=font.Font(family='Helvetic', size=80, weight='bold')
txt=StringVar()
if(minutes> 20): annoy())
lbl=ttk.Label(root, textvariable=txt, font=fnt, foreground="black", background="green")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
