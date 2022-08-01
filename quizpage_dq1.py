import os
import sys
import json
import tkinter as tk
from tkinter import font as tkfont

class MainFrame(tk.Tk):


    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.titlefont = tkfont.Font(family = "Verdana", size = 12, weight = "bold", slant = "roman")

        container = tk.Frame()
        container.grid(row=0, column=0, sticky='nsew')




        self.listing = {}

        for p in (MainMenu, QuizPage, LoginPage, WelcomeScreen):
            page_name = p.__name__
            frame = p(parent = container, controller = self)
            frame.grid(row=0, column=0, sticky='nsew')
            self.listing[page_name] = frame

    def up_frame(self, page_name):
        page = self.listing[page_name]
        page.tkraise()
        # for testing
        if page_name != "MainMenu":
            print("Raised {} page".format(page_name))

        elif page_name == "MainMenu":
            print("Returned to {}".format(page_name))
    



class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        label = tk.Label(self, text = "Welcome to the quiz \n", font = controller.titlefont)
        label.pack()

        label = tk.Label(self, text = "Select a quiz below to start: \n", font = controller.titlefont)
        label.pack()

        mathbtn = tk.Button(self, text = "Maths", command= lambda *args : controller.up_frame("QuizPage"))
        mathbtn.pack()

        engbtn = tk.Button(self, text = "English", command= lambda: controller.up_frame("QuizPage"))
        engbtn.pack()

        phybtn = tk.Button(self, text = "Physics", command= lambda: controller.up_frame("QuizPage"))
        phybtn.pack()

        sosbtn = tk.Button(self, text = "Social Studies", command= lambda: controller.up_frame("QuizPage"))
        sosbtn.pack()        





class QuizPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="The Quiz Page")
        label.pack()


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text = "This is the login page \n", font = controller.titlefont)
        label.pack()

        bou = tk.Button(self, text = "Enter quiz", command= lambda: controller.up_frame("MainMenu"))
        bou.pack()



class WelcomeScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text = "Press button to enter quiz \n", font = controller.titlefont)
        label.pack()

        bou = tk.Button(self, text = "Enter quiz", command= lambda: controller.up_frame("LoginPage"))
        bou.pack()




with open ('quizquestions.json'), "r" as f:
    data = json.load(f)

question = (data['question'])
options = (data['options'])
answer = (data['answer'])


gui = MainFrame()
gui.mainloop()
