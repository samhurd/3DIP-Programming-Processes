import os
import sys
import json
import tkinter as tk
from tkinter import DISABLED, font as tkfont

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
        self.q_no = 0
        self.data_size=len(question)
        self.display_question()
        self.buttons()


        self.complete = tk.Label(self, text="Quiz Complete!")

    def display_question(self):

        spacer = tk.Label(self, text="", width = 50)

        spacer.pack()
        q_no = tk.Label(self, text=question[self.q_no], width=30,
        font=( 'verdana' ,18, 'bold' ))
         
        q_no.place(x=5, y=30)

    def next_btn(self):
        #increments the question number variable, to move on to the next question
        self.q_no += 1
         

        if self.q_no==self.data_size:
            self.next_button["state"] = DISABLED
            self.complete.pack()
             
            
        #otherwise it will continue
        else:
            
            self.display_question()
    
    def buttons(self):
        self.next_button = tk.Button(self, text="Next",command=self.next_btn,
        width=10,fg="black",font=("ariel",16,"bold"))
         
        
        self.next_button.place(x=5, y=140)

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




with open (os.path.join(sys.path[0], 'quizquestions.json'), "r") as f:
    data = json.load(f)

question = (data['mathsquestions'])
options = (data['mathsoptions'])
answer = (data['mathsanswers'])

print(question)


gui = MainFrame()
gui.mainloop()
