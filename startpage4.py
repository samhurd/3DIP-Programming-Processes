import os
import sys
import json
import tkinter as tk
from tkinter import *
from tkinter import font as tkfont
from tkinter import messagebox


class MainFrame(tk.Tk):

#the frame object holding all the pages
#controller of all the pages, setting up main functions, styles etc..

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #creating 'styles' that can be used later to apply to widgets, thus preventing unnecessary code
        self.headingfont = tkfont.Font(family = "Verdana", size = 12, weight = "bold", slant = "roman")
        self.titlefont = tkfont.Font(family = "Verdana", size = 20, weight = "bold", slant = "roman")

        #a container Frame that holds all the pages 
        container = tk.Frame()
        container.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)

        #empty dictionary that is given the name of the page, so the program knows which page to switch to
        self.listing = {}

        #takes the name of each Class as a string, then creates a frame for each Class/page which has a parent of container
        #also makes MainFrame the controller, so any functions in MainFrame can be called later outside of MainFrame
        for p in (MainMenu, QuizPage, StartPage, SplashScreen):
            page_name = p.__name__
            frame = p(parent = container, controller = self)
            frame.grid(row=0, column=0, sticky='nsew')
            self.listing[page_name] = frame
        


    #raises the selected page to the top level so it can be seen 
    #this is how the program switches between pages
    def show_frame(self, page_name):
        page = self.listing[page_name]
        page.tkraise()
        # for testing
        if page_name != "MainMenu":
            print("Raised {} page".format(page_name))

        elif page_name == "MainMenu":
            print("Returned to {}".format(page_name))

    #to quit the whole program when needed
    def exit(self):
        gui = MainFrame
        gui.quit(self) 
    

    


    


    

#MainMenu page, with buttons to select which subject the user wants to do a quiz on
class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text = "Welcome to the quiz \n", font = controller.headingfont)
        label.pack()

        label = tk.Label(self, text = "Select a quiz below to start: \n", font = controller.headingfont)
        label.pack()

        #when pressed, these buttons set the variable (subject) to a value, which decides which quiz the user will do. 
        #then the quiz is reset so it starts from the beginning with the desired subject.

        #after all that is done, the button will call the show_frame function from the controller (MainFrame) and pass it the string name of the page we want to switch to

        mathbtn = tk.Button(self, text = "Maths", command= lambda *args: [subject_select(1), print(subject), QuizPage.reset_quiz(), controller.show_frame("QuizPage")])
        mathbtn.pack()

        phybtn = tk.Button(self, text = "Physics", command= lambda *args: [subject_select(2), print(subject), controller.show_frame("QuizPage")])
        phybtn.pack()

        engbtn = tk.Button(self, text = "English", command= lambda *args: [controller.show_frame("QuizPage"), subject_select(3), print(subject)])
        engbtn.pack()

        sosbtn = tk.Button(self, text = "Social Studies", command= lambda *args: [controller.show_frame("QuizPage"), subject_select(4), print(subject)])
        sosbtn.pack()

        # quitbtn = tk.Button(self, text = "Quit", command= gui.quit)
        # quitbtn.pack()   


class QuizPage(tk.Frame):

    #initialises all the functions of the quiz
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.q_no=0
        self.correct=0
        self.quiz_title()
        self.return_button = tk.Button(self, text="Return to main menu", 
            command=lambda *args: [controller.show_frame("MainMenu")], 
            fg="black",font=("ariel",16," bold"))
        self.return_button.pack()
        reset_button = tk.Button(self, text="Reset quiz", 
            command=self.reset_quiz, 
            fg="black",font=("ariel",16," bold"))        
        reset_button.pack(anchor=NE)
        self.display_question()
        self.opt_selected=tk.IntVar()
        self.opts=self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size=len(question)



    #resets the quiz to its initial state
    @classmethod
    def reset_quiz(self):

        #destroys all widgets in the QuizPage frame, clearing it so the widgets can be initialised again
        for widgets in QuizPage.winfo_children(self):
            widgets.pack_forget()
            print("widget destroyed")


        self.q_no=0
        self.correct=0
        self.quiz_title()
        
        self.return_button.pack(anchor=NE)

        self.display_question()
        self.opt_selected=tk.IntVar()
        
        self.opts=self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size=len(question)
        print("quiz successfully reset")
        print(subject)



    def check_ans(self, q_no):
        #sets which subject the quiz will check answers for
        if subject == 1:
            answer = mathanswer

        elif subject == 2:
            answer = phyanswer
        

        #checks if the user selected option is equal to the correct answer in the json file
        if self.opt_selected.get() == answer[q_no]:
            
            return True   


    def next_btn(self):
         
        #if the user answers correctly, adds one to the correct count
        if self.check_ans(self.q_no):
             
            
            self.correct += 1
         
        #increments the question number variable, to move on to the next question
        self.q_no += 1
         
        # if all questions have been answered, the program will display the user's results for the recent quiz
        if self.q_no==self.data_size:
             
            
            self.display_result()
            self.next_button["state"] = DISABLED
             
            
        #otherwise it will continue
        else:
            
            self.display_question()
            self.display_options()
 
    #displays the users result for that quiz as a pop-up messagebox
    def display_result(self):
         
        #calculates the users score
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
         
        
        scorepercentage = int(self.correct / self.data_size * 100)
        result = f"Score: {scorepercentage}%"
         
        
        messagebox.showinfo("Result", f"{result}\n{correct}\n{wrong}")

    def buttons(self):

        self.next_button = tk.Button(self, text="Next",command=self.next_btn,
        width=10,fg="black",font=("ariel",16,"bold"))
         
        
        self.next_button.pack()
         



    def display_options(self):
        val=0
        #sets which subject the quiz will give options for
        if subject == 1:
            options = mathoptions

        elif subject == 2:
            options = phyoptions

        self.opt_selected.set(0)
         
        
        
        for option in options[self.q_no]:
            self.opts[val]['text']=option
            val+=1

    def display_question(self):
        #sets which subject the quiz will give questions for
        if subject == 1:
            question = mathquestion

        elif subject == 2:
            question = phyquestion

        q_no = tk.Label(self, text=question[self.q_no], width=30,
        font=( 'verdana' ,18, 'bold' ))
         
        #the questions are placed on top of each other so they appear in the same place
        q_no.place(x=5, y=30)


    def quiz_title(self):
        if subject == 1:
            title_text = "Maths Quiz"

        elif subject == 2:
            title_text = "Physics Quiz"
         
        
        title = tk.Label(self, text=title_text,
        width=50, font=("verdana", 20, "bold"), fg='blue')
         
        
        title.pack()

    def radio_buttons(self):
         
        
        q_list = []
         
        
        y_pos = 150
         
        
        while len(q_list) < 4:
             
            
            radio_btn = tk.Radiobutton(self,text=" ",variable=self.opt_selected,
            value = len(q_list)+1,font = ("ariel",14), pady=10, padx=10)
             
            
            q_list.append(radio_btn)
             
            
            radio_btn.pack(anchor=W)
             
            
            y_pos += 40
         
        
        return q_list




class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
    
        label = tk.Label(self, text = "Please enter your name and Year Level to continue to the quiz \n", font = controller.headingfont)
        label.pack()

        self.nameLabel = tk.Label(self, text="Enter your name:")
        self.nameLabel.pack()

        self.nameEntry = tk.Entry(self)
        self.nameEntry.pack()

        yr_lvl_Label = tk.Label(self, text="Enter your year level:")
        yr_lvl_Label.pack()

        self.yr_lvlEntry = tk.Entry(self)
        self.yr_lvlEntry.pack()

        self.quiz_button = tk.Button(self, text = "Submit", command=self.check_name)
        self.quiz_button.pack()

        self.welcome = tk.Button(self, text="Success!", font = controller.headingfont)
        self.enter_button = tk.Button(self, text = "Enter quiz", command=lambda: controller.show_frame("MainMenu"))
        
        self.msg = tk.Label(self, text="")



    #checks that the user has entered something in the name field
    def check_name(self):
        self.msg.pack()
        if len(self.nameEntry.get()) >= 1:
            self.check_num()

        elif len(self.nameEntry.get()) == 0:
            self.msg.pack()
            self.msg.config(text="Please enter a name", fg="red")



    #checks that the value entered for year level is a number
    def check_num(self):
        try:
            int(self.yr_lvlEntry.get())
            self.check_age()

        except ValueError:
            self.msg.config(text="Please enter a numerical value for Year Level ", fg="red")



    #checks that the user is between year 11 and 13
    def check_age(self):

        if 11 <= int(self.yr_lvlEntry.get()) <= 13:
            self.msg.pack_forget()
            self.quiz_button.pack_forget()
            self.enter_button.pack()
            self.msg.pack()
            self.msg.config(text="Success! You may now enter the quiz.", fg="green")

        elif int(self.yr_lvlEntry.get()) == 1261:
            self.msg.pack()
            self.msg.config(text="Dont you mean 1216?", fg="blue")


        else:
            self.msg.config(text="You are not the intended Year level for this quiz", fg="red")


#try to use trace and enable button when both fields are filled


class SplashScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text = "\n Welcome to the \n BDSC General Revision Quiz! \n", font = controller.titlefont)
        label.pack()

        self.after(500, lambda: controller.show_frame("StartPage"))  










def subject_select(value):
    global subject
    subject = value




with open (os.path.join(sys.path[0], 'quizquestions.json'), "r") as f:
    data = json.load(f)






subject = 1


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



username = StringVar
yearlevel = StringVar


#start the application
gui = MainFrame()
gui.title("Revision Quiz")
gui.mainloop()



