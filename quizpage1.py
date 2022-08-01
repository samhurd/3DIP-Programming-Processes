import tkinter as tk

from tkinter import font as tkfont


mathquestions = {
        'questions' : ["Question 1", "Question 2", "Question 3", "Question 4" ],
        'answers' : [2, 4, 1, 3],
        'q1options' : ["option1 \n option2 \n option3 \n option4",],
        'q2options' : ["option1 \n option2 \n option3 \n option4",],
        'q3options' : ["option1 \n option2 \n option3 \n option4",],
        'q4options' : ["option1 \n option2 \n option3 \n option4",]

}
class MainFrame(tk.Tk):


    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.titlefont = tkfont.Font(family = "Verdana", size = 12, weight = "bold", slant = "roman")

        container = tk.Frame()
        container.grid(row=0, column=0, sticky='nsew')




        self.listing = {}

        for p in (MainMenu, MathQuiz, EngQuiz, PhyQuiz, SosQuiz, WelcomeScreen):
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

    def quiz():
        global subject
        subject = ("placeholder")
        label = tk.Label(text = "Welcome to the {} quiz".format(subject), font = MainFrame.titlefont)
        label.pack()

class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text = "Welcome to the quiz \n", font = controller.titlefont)
        label.pack()

        label = tk.Label(self, text = "Select a quiz below to start: \n", font = controller.titlefont)
        label.pack()
        
        mathbtn = tk.Button(self, text = "Maths", command= lambda: controller.up_frame("MathQuiz"))
        mathbtn.pack()

        engbtn = tk.Button(self, text = "English", command= lambda: controller.up_frame("EngQuiz"))
        engbtn.pack()

        phybtn = tk.Button(self, text = "Physics", command= lambda: controller.up_frame("PhyQuiz"))
        phybtn.pack()

        sosbtn = tk.Button(self, text = "Social Studies", command= lambda: controller.up_frame("SosQuiz"))
        sosbtn.pack()        

class MathQuiz(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text = "Maths Quiz \n", font = controller.titlefont)
        label.pack()

        bou = tk.Button(self, text = "To Main Menu", command= lambda: controller.up_frame("MainMenu"))
        bou.pack()

class EngQuiz(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        subject = ("English")

        label = tk.Label(self, text = "English Quiz \n", font = controller.titlefont)
        label.pack()

        bou = tk.Button(self, text = "To Main Menu", command= lambda: controller.up_frame("MainMenu"))
        bou.pack()

class PhyQuiz(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text = "Physics Quiz \n", font = controller.titlefont)
        label.pack()

        bou = tk.Button(self, text = "To Main Menu", command= lambda: controller.up_frame("MainMenu"))
        bou.pack()

class SosQuiz(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text = "Social studies test \n", font = controller.titlefont)
        label.pack()

        bou = tk.Button(self, text = "To Main Menu", command= lambda: controller.up_frame("MainMenu"))
        bou.pack()

class WelcomeScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text = "Press button to enter quiz \n", font = controller.titlefont)
        label.pack()

        bou = tk.Button(self, text = "Enter quiz", command= lambda: controller.up_frame("MainMenu"))
        bou.pack()


if __name__ == '__main__':
    app = MainFrame()
    app.mainloop()

