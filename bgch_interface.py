import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.proxy import Proxy, ProxyType
from datetime import datetime, timedelta
from threading import Thread
import easygui

class Application(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(height=500, width=450)
        self.master = master
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        #image
        width, height = 250, 250
        img = Image.open("BGCH_Emblem.png")
        img = img.resize((width, height), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(img)
        img = Label(image=render)
        img.image = render
        img.place(x=100, y=0)
        #inputs
        self.box_relief = "solid"
        self.num_players = StringVar()
        self.which_course = StringVar()
        self.email, self.password = StringVar(), StringVar()
        num_players_label = Label(self, text="Enter Number of Players:")
        num_players_label.place(x=120, y=260)
        one_player = Radiobutton(self, text="1", variable=self.num_players, value=1)
        one_player.place(x=120, y=280)
        two_player = Radiobutton(self, text="2", variable=self.num_players, value=2)
        two_player.place(x=160, y=280)
        three_player = Radiobutton(self, text="3", variable=self.num_players, value=3)
        three_player.place(x=200, y=280)
        four_player = Radiobutton(self, text="4", variable=self.num_players, value=4)
        four_player.place(x=240, y=280)
        which_course_label = Label(self, text="Select Course:")
        which_course_label.place(x=120, y=310)
        black = Radiobutton(self, text="Black", variable=self.which_course, value="Bethpage Black Course")
        black.place(x=120, y=330)
        blue = Radiobutton(self, text="Blue", variable=self.which_course, value="Bethpage Blue Course")
        blue.place(x=180, y=330)
        green = Radiobutton(self, text="Green", variable=self.which_course, value="Bethpage Green Course")
        green.place(x=240, y=330)
        red = Radiobutton(self, text="Red", variable=self.which_course, value="Bethpage Red Course")
        red.place(x=300, y=330)
        preferred_times_label = Label(self, text="Select Preferred Tee Time Window:")
        preferred_times_label.place(x=120, y=360)
        start_label = Label(self, text="Start:")
        start_label.place(x=120, y=380)
        self.start_time = StringVar()
        #don't know which times will be posted ahead of time.
        start_times = tk.OptionMenu(self, self.start_time, "8:30am", "8:31am", "8:32am", "8:33am", "8:34am", "8:35am", "8:36am", "8:37am", "8:38am", "8:39am", "8:40am", "8:41am", "8:42am", "8:43am", 
                           "8:44am", "8:45am", "8:46am", "8:47am", "8:48am", "8:49am", "8:50am", "8:51am", "8:52am", "8:53am", "8:54am", "8:55am", "8:56am", "8:57am", "8:58am", "8:59am", "9:00am", 
                           "9:01am", "9:02am", "9:03am", "9:04am", "9:05am", "9:06am", "9:07am", "9:08am", "9:09am", "9:10am", "9:11am", "9:12am", "9:13am", "9:14am", "9:15am", "9:16am", "9:17am", "9:18am", 
                           "9:19am", "9:20am", "9:21am", "9:22am", "9:23am", "9:24am", "9:25am", "9:26am", "9:27am", "9:28am", "9:29am", "9:30am", "9:31am", "9:32am", "9:33am", "9:34am", "9:35am", "9:36am", "9:37am", "9:38am", "9:39am", "9:40am", "9:41am", "9:42am", "9:43am", "9:44am", 
                           "9:45am", "9:46am", "9:47am", "9:48am", "9:49am", "9:50am", "9:51am", "9:52am", "9:53am", "9:54am", "9:55am", "9:56am", "9:57am", "9:58am", "9:59am", "10:00am", "10:01am", "10:02am",
                           "10:03am", "10:04am", "10:05am", "10:06am", "10:07am", "10:08am", "10:09am", "10:10am", "10:11am", "10:12am", "10:13am", "10:14am", "10:15am", "10:16am", "10:17am", "10:18am", 
                           "10:19am", "10:20am", "10:21am", "10:22am", "10:23am", "10:24am", "10:25am", "10:26am", "10:27am", "10:28am", "10:29am", "10:30am", "10:31am", "10:32am", "10:33am", "10:34am", 
                           "10:35am", "10:36am", "10:37am", "10:38am", "10:39am", "10:40am", "10:41am", "10:42am", "10:43am", "10:44am", "10:45am", "10:46am", "10:47am", "10:48am", "10:49am", "10:50am", 
                           "10:51am", "10:52am", "10:53am", "10:54am", "10:55am", "10:56am", "10:57am", "10:58am", "10:59am", "11:00am", "11:01am", "11:02am", "11:03am", "11:04am", "11:05am", "11:06am", 
                           "11:07am", "11:08am", "11:09am", "11:10am", "11:11am", "11:12am", "11:13am", "11:14am", "11:15am", "11:16am", "11:17am", "11:18am", "11:19am", "11:20am", "11:21am", "11:22am", 
                           "11:23am", "11:24am", "11:25am", "11:26am", "11:27am", "11:28am", "11:29am", "11:30am", "11:31am", "11:32am", "11:33am", "11:34am", "11:35am", "11:36am", "11:37am", "11:38am", 
                           "11:39am", "11:40am", "11:41am", "11:42am", "11:43am", "11:44am", "11:45am", "11:46am", "11:47am", "11:48am", "11:49am", "11:50am", "11:51am", "11:52am", "11:53am", "11:54am", 
                           "11:57am", "11:58am", "11:59am", "12:00pm", "12:01pm", "12:02pm", "12:03pm", "12:04pm", "12:05pm", "12:06pm", "12:07pm", "12:08pm", "12:09pm", "12:10pm", "12:11pm", "12:12pm", 
                           "12:13pm", "12:14pm", "12:15pm", "12:16pm", "12:17pm", "12:18pm", "12:19pm", "12:20pm", "12:21pm", "12:22pm", "12:23pm", "12:24pm", "12:25pm", "12:26pm", "12:27pm", "12:28pm", 
                           "12:29pm", "12:30pm")
        start_times.config(width=8)
        start_times.place(x=160, y=380)
        end_label = Label(self, text="End:")
        end_label.place(x=255, y=380)
        self.end_time = StringVar()
        end_times = tk.OptionMenu(self, self.end_time, "12:31pm", "12:32pm", "12:33pm", "12:34pm", "12:35pm", "12:36pm", "12:37pm", "12:38pm", "12:39pm" , "12:40pm", "12:41pm", "12:42pm", "12:43pm", "12:44pm", 
                           "12:45pm", "12:46pm", "12:47pm", "12:48pm", "12:49pm", "12:50pm", "12:51pm", "12:52pm", "12:53pm", "12:54pm", "12:55pm", "12:56pm", "12:57pm", "12:58pm", "12:59pm", "1:00pm", 
                           "1:01pm", "1:02pm", "1:03pm", "1:04pm", "1:05pm", "1:06pm", "1:07pm", "1:08pm", "1:09pm", "1:10pm", "1:11pm", "1:12pm", "1:13pm", "1:14pm", "1:15pm", "1:16pm", "1:17pm", "1:18pm", 
                           "1:19pm", "1:20pm", "1:21pm", "1:22pm", "1:23pm", "1:24pm", "1:25pm", "1:26pm", "1:27pm", "1:28pm", "1:29pm", "1:30pm", "1:31pm", "1:32pm", "1:33pm", "1:34pm", "1:35pm", "1:36pm", 
                           "1:37pm", "1:38pm", "1:39pm", "1:40pm", "1:41pm", "1:42pm", "1:43pm", "1:44pm", "1:45pm", "1:46pm", "1:47pm", "1:48pm", "1:49pm", "1:50pm", "1:51pm", "1:52pm", "1:53pm", "1:54pm", 
                           "1:55pm", "1:56pm", "1:57pm", "1:58pm", "1:59pm", "2:00pm", "2:01pm", "2:02pm", "2:03pm", "2:04pm", "2:05pm", "2:06pm", "2:07pm", "2:08pm", "2:09pm", "2:10pm", "2:11pm", "2:12pm", "2:13pm", 
                           "2:14pm", "2:15pm", "2:16pm", "2:17pm", "2:18pm", "2:19pm", "2:20pm", "2:21pm", "2:22pm", "2:23pm", "2:24pm", "2:25pm", "2:26pm", "2:27pm", "2:28pm", "2:29pm", "2:30pm", "2:31pm", 
                           "2:32pm", "2:33pm", "2:34pm", "2:35pm", "2:36pm", "2:37pm", "2:38pm", "2:39pm", "2:40pm", "2:41pm", "2:42pm", "2:43pm", "2:44pm", "2:45pm", "2:46pm", "2:47pm", "2:48pm", "2:49pm", 
                           "2:50pm", "2:51pm", "2:52pm", "2:53pm", "2:54pm", "2:55pm", "2:56pm", "2:57pm", "2:58pm", "2:59pm", "3:00pm", "3:01pm", "3:02pm", "3:03pm", "3:04pm", "3:05pm", "3:06pm", "3:07pm", 
                           "3:08pm", "3:09pm", "3:10pm", "3:11pm", "3:12pm", "3:13pm", "3:14pm", "3:15pm", "3:16pm", "3:17pm", "3:18pm", "3:19pm", "3:20pm", "3:21pm", "3:22pm", "3:23pm", "3:24pm", "3:25pm", 
                           "3:26pm", "3:27pm", "3:28pm", "3:29pm", "3:30pm", "3:31pm", "3:32pm", "3:33pm", "3:34pm", "3:35pm", "3:36pm", "3:37pm", "3:38pm", "3:39pm", "3:40pm", "3:41pm", "3:42pm", "3:43pm", 
                           "3:44pm", "3:45pm", "3:46pm", "3:47pm", "3:48pm", "3:49pm", "3:50pm", "3:51pm", "3:52pm", "3:53pm", "3:54pm", "3:55pm", "3:56pm", "3:57pm", "3:58pm", "3:59pm", "4:00pm", "4:01pm", 
                           "4:02pm", "4:03pm", "4:04pm", "4:05pm", "4:06pm", "4:07pm", "4:08pm", "4:09pm", "4:10pm", "4:11pm", "4:12pm", "4:13pm", "4:14pm", "4:15pm", "4:16pm", "4:17pm", "4:18pm", "4:19pm", 
                           "4:20pm", "4:21pm", "4:22pm", "4:23pm", "4:24pm", "4:25pm", "4:26pm", "4:27pm", "4:28pm", "4:29pm", "4:30pm")
        end_times.config(width=8)
        end_times.place(x=290, y=380)
        email_label = Label(self, text="Email: ")
        email_label.place(x=80, y=410)
        email_entry = Entry(self, textvariable=self.email, width=25, borderwidth=2)
        email_entry.place(x=125, y=410)
        password_label = Label(self, text="Password: ")
        password_label.place(x=80, y=440)
        password_entry = Entry(self, textvariable=self.password, width=25, borderwidth=2)
        password_entry.place(x=150, y=440)
        entry = tk.Button(self, text="Get Tee Time", command=self.enterCallback, relief=self.box_relief)
        entry.place(x=295, y=290)

    def enterCallback(self):
        global dataframe
        num_players = self.num_players.get()
        print("num players: {}".format(num_players))
        course_select = self.which_course.get()
        print("course selected: {}".format(course_select))
        start_time = self.start_time.get()
        print("start: {}".format(start_time))
        end_time = self.end_time.get()
        print("end: {}".format(end_time))
        email = self.email.get()
        print("email: {}".format(email))
        password = self.password.get()
        print("password: {}".format(password))
        sys.argv = ['beau_golf_crawler_hack.py', num_players, course_select, start_time, end_time, email, password]
        exec(open('beau_golf_crawler_hack.py').read())

def main():
    root = tk.Tk()
    app = Application(master=root)
    root.geometry("460x490")
    root.title("BGCH")
    app.mainloop()    
        
main()