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

        mathbtn = tk.Button(self, text = "Maths", command= lambda *args : [subject_select(1), controller.up_frame("QuizPage")])
        mathbtn.pack()

        phybtn = tk.Button(self, text = "Physics", command= lambda: [subject_select(2), controller.up_frame("QuizPage")])
        phybtn.pack()

        engbtn = tk.Button(self, text = "English", command= lambda: controller.up_frame("QuizPage"))
        engbtn.pack()

        sosbtn = tk.Button(self, text = "Social Studies", command= lambda: controller.up_frame("QuizPage"))
        sosbtn.pack()        





class QuizPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.return_button = tk.Button(self, text="Return to main menu", 
            command=lambda: [controller.up_frame("MainMenu"), self.reset_quiz()], 
            fg="black",font=("ariel",16," bold"))
        self.answer_msg = tk.Label(self, text="", font=("ariel",16,"bold"))
        self.reset_quiz()


    def reset_quiz(self):
        #resets the answer message label
        self.answer_msg.config(text="")
        #destroys all widgets in the QuizPage frame, clearing it so the widgets can be initialised again
        for widgets in QuizPage.winfo_children(self):
            widgets.pack_forget()
            print("{} destroyed".format(widgets))
        
        self.startLabel = tk.Label(self, text="Subject chosen \n press the button to start your quiz:\n", font=("ariel",16,"bold"))
        self.startLabel.pack()

        self.startButton = tk.Button(self, text="Enter quiz", command=self.start_quiz)
        self.startButton.pack()

    def start_quiz(self):

        self.startLabel.pack_forget()
        self.startButton.pack_forget()

        self.q_no=0
        self.correct=0
        self.quiz_title()

        self.return_button.pack(anchor=E)
        self.display_question()
        self.data_size=len(question)
        self.opt_selected=tk.IntVar() 
        self.opts=self.option_buttons()
        self.set_options()
        self.buttons()
        self.complete = tk.Label(self, text="Quiz Complete!")

        self.answer_msg.pack()
        self.display_result()



    def display_result(self):
         
        #calculates the users score
        wrong_count = self.data_size - self.correct
        correct = f"{self.correct}"
        wrong = f"{wrong_count}"
         
        
        score = int(self.correct / self.data_size * 100)
        result = f"{score}%"
         
        
        self.correctLabel = tk.Label(self, text="You got {} questions correct".format(correct))

        self.wrongLabel = tk.Label(self, text="You got {} questions wrong".format(wrong))

        self.scoreLabel = tk.Label(self, text="Your score was {}".format(result))

    def check_ans(self, q_no):

        if subject == 1:
            answer = mathanswer

        elif subject == 2:
            answer = phyanswer
        
        #checks if the user selected option is equal to the correct answer in the json file
        if self.opt_selected.get() == answer[q_no]:
            
            return True   


    def next_btn(self):
         

        if self.check_ans(self.q_no):

            self.correct += 1
            self.answer_msg.config(text="Correct!", fg="green")
            print("User has answered correctly {} times".format(self.correct))



        else:
            self.answer_msg.config(text="Incorrect", fg="red")
         

        self.q_no += 1
         

        if self.q_no==self.data_size:
             
            self.display_result()
            #and then displaying them to the user
            self.correctLabel.pack()
            self.wrongLabel.pack()
            self.scoreLabel.pack()

            #destroying the next label and answer message
            self.next_button.pack_forget()
            self.answer_msg.pack_forget()
             
            
            
        #otherwise it will continue
        else:
            
            self.display_question()
            self.set_options()

    def buttons(self):
        self.next_button = tk.Button(self, text="Next",command=self.next_btn,
        width=10,bg="blue",fg="black",font=("ariel",16,"bold"))
         
        
        self.next_button.pack()

    def set_options(self):
        val=0
        if subject == 1:
            options = mathoptions

        elif subject == 2:
            options = phyoptions
         


        self.opt_selected.set(0)
        
        
        for option in options[self.q_no]:
            self.opts[val]['text']=option
            val+=1

    def display_question(self):
        if subject == 1:
            question = mathquestion

        elif subject == 2:
            question = phyquestion

        q_no = tk.Label(self, text=question[self.q_no], width=60,
        font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
         
        
        q_no.place(x=5, y=30)

    def quiz_title(self):

        if subject == 1:
            title_text = "Maths Quiz"

        elif subject == 2:
            title_text = "Physics Quiz"
         
        
        title = tk.Label(self, text=title_text,
        width=74, bg="white",fg="blue",  font=("ariel", 20, "bold"))
         
        
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


def subject_select(value):
    global subject
    subject = value
    print(subject)


with open (os.path.join(sys.path[0], 'quizquestions.json'), "r") as f:
    data = json.load(f)


mathquestion = (data['mathsquestions'])
mathoptions = (data['mathsoptions'])
mathanswer = (data['mathsanswers'])


phyquestion = (data['phyquestions'])
phyoptions = (data['phyoptions'])
phyanswer = (data['phyanswers'])


#initialise quiz variables
question = (data['mathsquestions'])
options = (data['mathsoptions'])
answer = (data['mathsanswers'])




gui = MainFrame()
gui.mainloop()
