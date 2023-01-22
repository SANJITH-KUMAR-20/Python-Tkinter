import tkinter as t
from tkinter import ttk,messagebox
import time
import multiprocessing
import threading
#lists for combobox
hrs_list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
15, 16, 17, 18, 19, 20, 21, 22, 23, 24]#list of hours
mins_secs_list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 
30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44,
45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 
]#list of minutes/seconds
class countdowntimer:
    def __init__(self):
        self.window=t.Tk()
        self.window.geometry('800x800')
        self.window.title("Countdown Timer")
        self.stoploop=False#used as a flag to stop the cowntdown
        #labels for hours,mins and seconds and the head label
        label=t.Label(self.window,text="SET TIME",font=("Helvatica",20,"bold")).pack()
        hlabel=t.Label(self.window,text="HOURS",font=("Helvatica",15)).place(x=50,y=70)
        mlabel=t.Label(self.window, text="MINUTES",font=("Helvatica",15)).place(x=200,y=70)
        slabel =t.Label(self.window, text="SECONDS",font=("Helvatica",15)).place(x=350,y=70)
        #setting comboboxes for hours,minutes and seconds
        self.hour=t.IntVar()
        self.hcbox=ttk.Combobox(self.window,height=12,textvariable=self.hour,width=6)
        self.hcbox['values']=hrs_list
        self.hcbox.current(0)
        self.hcbox.place(x=50,y=100)
        self.minute=t.IntVar()
        self.mcbox=ttk.Combobox(self.window,height=12,textvariable=self.minute,width=6)
        self.mcbox['values']=mins_secs_list
        self.mcbox.current(0)
        self.mcbox.place(x=200,y=100)
        self.second=t.IntVar()
        self.scbox=ttk.Combobox(self.window,height=12,textvariable=self.second,width=6)
        self.scbox['values']=mins_secs_list
        self.scbox.current(0)
        self.scbox.place(x=350,y=100)
        resetbutton =t.Button(self.window, text='RESET',font=('Helvetica',12,'bold'), bg="white", fg="black",command=self.reset)
        resetbutton.place(x=150, y=150)
        #settingbutton
        setbutton =t.Button(self.window, text='SET',font=('Helvetica',12,'bold'), bg="white", fg="black",command=self.settime)
        setbutton.place(x=50, y=150)
        #destroybutton
        destroybutton =t.Button(self.window, text='EXIT',font=('Helvetica',12,'bold'), bg="white", fg="black",command=self.destroy)
        destroybutton.place(x=200, y=200)
        #resetbutton
        t.mainloop()
    def destroy(self): #terminates the window
        self.stoploop = True
        self.window.destroy()
    def settime(self):
        self.disp=t.Label(self.window,font=('Helvetica', 20 , "bold"),bg = 'gray35', fg = 'yellow')
        self.disp.place(x=130, y=300)

        try:
            #total seconds
            hrs=int(self.hcbox.get())*3600
            mins=int(self.mcbox.get())*60
            secs=int(self.scbox.get())
            self.total=hrs+mins+secs
            #startbutton
            start_button =t.Button(self.window, text='START/RESUME', 
            font=('Helvetica',12), bg="white", fg="black", 
            command=self.start)
            start_button.place(x=300, y=150)
            #pausebutton
            pause_button =t.Button(self.window, text='PAUSE', 
            font=('Helvetica',12), bg="white", fg="black",
            command=self.pause)
            pause_button.place(x=450, y=150)
        except Exception as es:
            messagebox.showerror("Error!", \
            f"Error due to {es}")
    def start(self):
        self.x =threading.Thread(target=self.startx, daemon=True)
        self.x.start()
    def startx(self):
        self.stoploop=False
        while self.total>0:
            minsx, secsx = divmod(self.total, 60)
            hours = 0
            if minsx>60:
                hours, minsx = divmod(mins, 60)
            self.disp.config(text=f"Time Left: {hours:02d}: {minsx:02d}: {secsx:02d}")
            self.disp.update()
            time.sleep(1)#for pausing execution for 1 second
            self.total = self.total-1
            if self.stoploop == True:
                break
    def pause(self):
        self.stoploop= True
        minsx, secsx = divmod(self.total, 60)
        hours = 0
        if minsx > 60:
            hours, minsx = divmod(mins, 60)
        self.disp.config(text=f"Time Left: {hours:02d}: {minsx:02d}: {secsx:02d}")
        self.disp.update()
    def reset(self):
        self.stoploop = True
        self.disp.config(text="Time Left: 00: 00: 00")
        
        
countdowntimer()
