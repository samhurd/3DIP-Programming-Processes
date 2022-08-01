import os
import sys
import json
import tkinter as tk
from tkinter import *
from tkinter import font as tkfont

class MainFrame(tk.Tk):


    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.titlefont = tkfont.Font(family = "Verdana", size = 12, weight = "bold", slant = "roman")

        container = tk.Frame()
        container.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)




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
        self.q_no=0
        
        self.display_title()
        spacer = tk.Label(self, text="", width = 50)
        spacer.pack()
        self.display_question()
        self.data_size=len(question)
        self.opt_selected=tk.IntVar() 
        self.opts=self.option_buttons()
        self.set_options()
        self.buttons()
        self.complete = tk.Label(self, text="Quiz Complete!")
        self.correct_msg = tk.Label(self, text="", font=("ariel",16,"bold"))
        self.correct_msg.pack()

    def check_ans(self, q_no):

        #checks if the user selected option is equal to the correct answer in the json file
        if self.opt_selected.get() == answer[q_no]:
            
            return True   


    def next_btn(self):
         

        if self.check_ans(self.q_no):
             print("That was the correct answer!")


        else:
            print("That was incorrect")

        self.q_no += 1
         
        if self.q_no==self.data_size:
            self.next_button["state"] = DISABLED
            self.complete.pack()
            
        else:
            
            self.display_question()
            self.set_options()
 

    def buttons(self):
        self.next_button = tk.Button(self, text="Next",command=self.next_btn,
        width=10,bg="blue",fg="black",font=("ariel",16,"bold"))
         
        
        self.next_button.pack()

    def set_options(self):
        val=0
         


        self.opt_selected.set(0)
        
        
        for option in options[self.q_no]:
            self.opts[val]['text']=option
            val+=1

    def display_question(self):


        q_no = tk.Label(self, text=question[self.q_no], width=60,
        font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
         
        
        q_no.place(x=5, y=30)

    def display_title(self):
         
        
        title = tk.Label(self, text="Revision Quiz",
        width=74, bg="white",fg="black", font=("ariel", 20, "bold"))
         
        
        title.pack()

    def option_buttons(self):
         
        #creating an empty list. This list tracks how many option buttons have been created
        q_list = []
         
        #setting the y position of the first option
        y_pos = 150
         
        
        while len(q_list) < 4:
             
            #setting the properties of each radio button
            radio_btn = tk.Radiobutton(self,text=" ",variable=self.opt_selected,
            value = len(q_list)+1,font = ("ariel",14), pady=10, padx=10)
             
            
            q_list.append(radio_btn)
             
            #packing the button
            radio_btn.pack(anchor=W)
             
            #incrementing the y position so that the options are spaced out and not on top of each other
            y_pos += 40

         
        
        return q_list



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




with open (os.path.join(sys.path[0], 'questionsbackup.json'), "r") as f:
    data = json.load(f)

question = (data['question'])
options = (data['options'])
answer = (data['answer'])


gui = MainFrame()
gui.mainloop()
