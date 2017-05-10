import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import sys
import threading
# note that there are many other schedulers available
from apscheduler.schedulers.background import BackgroundScheduler
from subprocess import call


def some_job():
    print('Every 10 seconds')
    return_code = call(["/Applications/Emacs.app/Contents/MacOS/Emacs -nw -q -l /Users/kgarg/.emacs.d/init.el /Users/kgarg/todo.txt"], shell=True)
    return return_code

        
def popup_bonus():
    win = tk.Toplevel()
    win.wm_title("Window")

    l = tk.Label(win, text="Input")
    l.grid(row=0, column=0)

    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)


def enter_log():
    # open mentioned file and write ok and whatever text I wrote here
    pass

def open_emacs():
    # open the file
    pass


def popup_showinfo():
    showinfo("Window", "Hello World!")


def hello_timer(mins=1.0/6):
    secs = 60*mins
    threading.Timer(int(secs), popup_showinfo).start()


class Application(ttk.Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.pack()

        self.button_bonus = ttk.Button(self, text="Bonuses", command=popup_bonus)
        self.button_bonus.pack()

        self.button_showinfo = ttk.Button(self, text="Show Info", command=popup_showinfo)
        self.button_showinfo.pack()
        #hello_timer()

root = tk.Tk()

app = Application(root)

sched = BackgroundScheduler()
# seconds can be replaced with minutes, hours, or days
sched.add_job(some_job, 'interval', seconds=10)
sched.start()


root.mainloop()
        
sched.shutdown()

