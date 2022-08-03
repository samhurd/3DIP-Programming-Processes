import os
import sys
import json
import tkinter as tk
from tkinter import *
from tkinter import font as tkfont


class MainFrame(tk.Tk):

# the frame object holding all the pages
# controller of all the pages, setting up main functions, styles etc..

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # creating 'styles' that can be used later to apply to widgets, thus preventing unnecessary code
        self.headingfont = tkfont.Font(family = "Verdana", size = 12, weight = "bold", slant = "roman")
        self.titlefont = tkfont.Font(family = "Verdana", size = 20, weight = "bold", slant = "roman")

        # container Frame that holds all the pages 
        container = tk.Frame()
        container.grid(row=0, column=0, sticky='nsew', padx=30, pady=30)

        # empty dictionary that is given the name of the page, so the program knows which page to switch to
        self.listing = {}

        # takes the name of each Class as a string, then creates a frame for each Class/page which has a parent of container
        # also makes MainFrame the controller, so any functions in MainFrame can be called later outside of MainFrame
        for p in (MainMenu, QuizPage, StartPage, SplashScreen):
            page_name = p.__name__
            frame = p(parent = container, controller = self)
            frame.grid(row=0, column=0, sticky='nsew')
            self.listing[page_name] = frame
        


    # raises the selected page to the top level so it can be seen 
    # this is how the program switches between pages
    def show_frame(self, page_name):
        page = self.listing[page_name]
        page.tkraise()

    # to quit the whole program when needed
    def exit(self):
        gui = MainFrame
        gui.quit(self) 
    

    


    


    

# MainMenu page, with buttons to select which subject the user wants to do a quiz on
class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text = "Welcome to the quiz \n", font = controller.headingfont)
        label.pack()

        label = tk.Label(self, text = "Select a quiz below to start: \n", font = controller.headingfont)
        label.pack()

        # when pressed, these buttons set the variable (subject) to a value, which decides which quiz the user will do. 
        # then the quiz is reset so it starts from the beginning with the desired subject.

        # after all that is done, the button will call the show_frame function from the controller (MainFrame) and pass it the string name of the page we want to switch to

        mathbtn = tk.Button(self, text = "Maths", command= lambda *args: [subject_select(1), controller.show_frame("QuizPage")])
        mathbtn.pack()

        phybtn = tk.Button(self, text = "Physics", command= lambda *args: [subject_select(2), controller.show_frame("QuizPage")])
        phybtn.pack()

        engbtn = tk.Button(self, text = "English", command= lambda *args: [subject_select(3), controller.show_frame("QuizPage")])
        engbtn.pack()

        sosbtn = tk.Button(self, text = "Social Studies", command= lambda *args: [subject_select(4), controller.show_frame("QuizPage")])
        sosbtn.pack()

        quitbtn = tk.Button(self, text = "Quit", command= lambda: [controller.exit()], fg="red")
        quitbtn.pack()   


class QuizPage(tk.Frame):

    # initialises all the functions of the quiz
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.q_no = 0
        self.return_button = tk.Button(self, text="Return to main menu", 
            command=lambda: [controller.show_frame("MainMenu"), self.reset_quiz()], 
            fg="black",font=("ariel",16," bold"))
        self.answer_msg = tk.Label(self, text="", font=("ariel",16,"bold"))

        self.questionLabel = tk.Label(self, text=question[self.q_no], width=65, height=3,
        font=( 'verdana' ,16, 'bold' ))
        self.reset_quiz()




    # resets the quiz 
    def reset_quiz(self):
        destroy_count = 0
        # resets the answer message label
        self.answer_msg.config(text="")
        # destroys all widgets in the QuizPage frame, clearing it so the widgets can be initialised again
        for widgets in QuizPage.winfo_children(self):
            widgets.pack_forget()
            print("{} destroyed".format(widgets))
            destroy_count+=1
        self.questionLabel.config(text="")


        print(destroy_count)
        self.startLabel = tk.Label(self, text="Subject chosen \n press the button to start your quiz:\n", font=("ariel",16,"bold"))
        self.startLabel.pack()

        self.startButton = tk.Button(self, text="Enter quiz", command=self.start_quiz)
        self.startButton.pack()





    def start_quiz(self):
        self.startLabel.pack_forget()
        self.startButton.pack_forget()
        self.q_no=0
        self.correct=0
        self.return_button.pack(anchor=E)
        self.quiz_title()
        self.questionLabel.pack(anchor=CENTER)
        self.display_question()
        self.opt_selected=tk.IntVar()
        self.opts=self.option_buttons()
        self.set_options()
        self.button()
        self.data_size=len(question)
        self.answer_msg.pack()
        self.display_result()
        print("quiz successfully started")
        print(subject)

    def check_ans(self, q_no):
        # sets which subject the quiz will check answers for
        if subject == 1:
            answer = mathanswer

        elif subject == 2:
            answer = phyanswer

        elif subject == 3:
            answer = enganswer

        elif subject == 4:
            answer = sosanswer

        # checks if the user selected option is equal to the correct answer in the json file
        if self.opt_selected.get() == answer[q_no]:
            return True   


    def next(self):
         
        # runs the check_ans function and if it returns True, the answer is correct
        if self.check_ans(self.q_no):
             
            # if the user answers correctly, adds one to the correct count, and shows the "Correct! message"
            self.correct += 1
            self.answer_msg.config(text="Correct!", fg="green")

        # if the check_ans function did not return True, meaning the user did not select the correct answer, it shows an "Incorrect" message
        else:
            self.answer_msg.config(text="Incorrect", fg="red")
         
        # increments the question number variable, to move on to the next question
        self.q_no += 1
        
        if self.q_no + 1 == self.data_size:
            self.next_button.config(text="Finish Quiz")
        #  if all questions have been answered, the program will display the user's results for the recent quiz
        if self.q_no==self.data_size:
            
            # running the function to calculate results
            self.display_result()
            # and then displaying them to the user
            self.correctLabel.pack()
            self.wrongLabel.pack()
            self.scoreLabel.pack()

            # destroying the next label and answer message
            self.next_button.pack_forget()
            self.answer_msg.pack_forget()
             
            
        # otherwise it will continue
        else:
            
            self.display_question()
            self.set_options()
 
    # displays the users result for that quiz 
    def display_result(self):
         
        # calculates the users score
        wrong_count = self.data_size - self.correct
        correct = f"{self.correct}"
        wrong = f"{wrong_count}"
         
        
        scorepercentage = int(self.correct / self.data_size * 100)
        result = f"{scorepercentage}%"
         
        
        self.correctLabel = tk.Label(self, text="You got {} questions correct".format(correct))

        self.wrongLabel = tk.Label(self, text="You got {} questions wrong".format(wrong))

        self.scoreLabel = tk.Label(self, text="Your score was {}".format(result))


    def button(self):

        self.next_button = tk.Button(self, text="Next",command=self.next,
        width=10,fg="black",font=("ariel",16,"bold"))
         
        
        self.next_button.pack()
         



    def set_options(self):
        val=0
        # sets which subject the quiz will give options for
        if subject == 1:
            options = mathoptions

        elif subject == 2:
            options = phyoptions

        elif subject == 3:
            options = engoptions

        elif subject == 4:
            options = sosoptions
        self.opt_selected.set(0)
         
        
        # goes through every option in the JSON file and creates a variables for each one.
        for option in options[self.q_no]:
            self.opts[val]['text']=option
            # val here is used to differentiate the options and number them uniquely, so the application knows which order to load them.
            val+=1

    def display_question(self):
        # sets which subject the quiz will give questions for
        if subject == 1:
            question = mathquestion

        elif subject == 2:
            question = phyquestion

        elif subject == 3:
            question = engquestion

        elif subject == 4:
            question = sosquestion

        self.questionLabel.config(text=question[self.q_no])



    def quiz_title(self):
        if subject == 1:
            title_text = "Maths Quiz"

        elif subject == 2:
            title_text = "Physics Quiz"
         
        elif subject == 3:
            title_text = "English Quiz"

        elif subject == 4:
            title_text = "Social Studies Quiz"
         
        title = tk.Label(self, text=title_text,
        width=50, font=("verdana", 20, "bold"), fg='blue', pady=10)
         
        
        title.pack()

    def option_buttons(self):

         
        # creating an empty list. This list tracks how many option buttons have been created
        q_list = []
         
        # setting the y position of the first option
        y_pos = 150
         
        
        while len(q_list) < 4:
             
            # setting the properties of each radio button
            self.radio_btn = tk.Radiobutton(self,text=" ",variable=self.opt_selected,
            value = len(q_list)+1,font = ("ariel",14), pady=10, padx=10)
             
            
            q_list.append(self.radio_btn)
             
            # packing the button
            self.radio_btn.pack(anchor=W)
             
            # incrementing the y position so that the options are spaced out and not on top of each other
            y_pos += 40

         
        
        return q_list



#the Start Page
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

        self.yr_lvlLabel = tk.Label(self, text="Enter your year level:")
        self.yr_lvlLabel.pack()

        self.yr_lvlEntry = tk.Entry(self)
        self.yr_lvlEntry.pack()

        self.submit_button = tk.Button(self, text = "Submit", command=self.check_name)
        self.submit_button.pack()

        self.welcome = tk.Button(self, text="Success!", font = controller.headingfont)
        self.enter_button = tk.Button(self, text = "Enter quiz", command=lambda: controller.show_frame("MainMenu"))
        
        self.msg = tk.Label(self, text="")
        self.msg.pack()



    # checks that the user has entered something in the name field
    def check_name(self):
        self.msg.pack()
        if (self.nameEntry.get().isalpha()):
            if len(self.nameEntry.get()) >= 1:
                self.check_num()

            elif len(self.nameEntry.get()) == 0:
                self.msg.pack()
                self.msg.config(text="Please enter a name", fg="red")

        else:
            self.msg.config(text="Please only enter letters for your name", fg="red")            




    # checks that the value entered for year level is a number
    def check_num(self):
        try:
            int(self.yr_lvlEntry.get())
            self.check_age()

        except ValueError:
            self.msg.config(text="Please enter a numerical value for Year Level ", fg="red")



    # checks that the user is between year 11 and 13
    def check_age(self):

        if 11 <= int(self.yr_lvlEntry.get()) <= 13:
            self.msg.pack_forget()
            self.submit_button.pack_forget()
            self.enter_button.pack()
            self.msg.pack()
            self.msg.config(text="Success! You may now enter the quiz.", fg="green")


        else:
            self.msg.config(text="You are not the intended Year level for this quiz", fg="red")





class SplashScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text = "\n Welcome to the \n BDSC General Revision Quiz! \n", font = controller.titlefont)
        label.pack()

        small_label = tk.Label(self, text = "\n Quiz starting...", font = ('verdana', 12))
        small_label.pack()

        self.after(1000, lambda: controller.show_frame("StartPage"))  










def subject_select(value):
    global subject
    subject = value




with open (os.path.join(sys.path[0], 'quizquestions.json'), "r") as f:
    data = json.load(f)






subject = 1

#initialising all subject variables
mathquestion = (data['mathsquestions'])
mathoptions = (data['mathsoptions'])
mathanswer = (data['mathsanswers'])

phyquestion = (data['phyquestions'])
phyoptions = (data['phyoptions'])
phyanswer = (data['phyanswers'])

engquestion = (data['engquestions'])
engoptions = (data['engoptions'])
enganswer = (data['enganswers'])

sosquestion = (data['sosquestions'])
sosoptions = (data['sosoptions'])
sosanswer = (data['sosanswers'])

# initialise the variables used in the quiz 
question = (data['mathsquestions'])
options = (data['mathsoptions'])
answer = (data['mathsanswers'])





# start the application
gui = MainFrame()
gui.title("Revision Quiz")
gui.mainloop()



