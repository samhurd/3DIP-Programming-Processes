import tkinter as tk
from tkinter import ttk


LARGETEXT = ("Verdana", 35)
BODYTEXT = ("Verdana", 20)
SMALLTEXT = ("Verdana", 15)

class app(tk.Tk):
     

    def __init__(self, *args, **kwargs):
         
        tk.Tk.__init__(self, *args, **kwargs)
         
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  

        self.frames = {} 
  
        for F in (StartPage, Login, Page2):
  
            frame = F(container, self)

            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0)
  
        self.show_frame(StartPage)
  


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
         

        label = ttk.Label(self, text ="Startpage", font = LARGETEXT)
        
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

  
        button1 = ttk.Button(self, text ="Login Page",
        command = lambda : controller.show_frame(Login))
     

        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  

        button2 = ttk.Button(self, text ="Page 2",
        command = lambda : controller.show_frame(Page2))

        button2.grid(row = 2, column = 1, padx = 10, pady = 10)


class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
         

        label = ttk.Label(self, text ="Login", font = LARGETEXT)

        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        button1 = ttk.Button(self, text ="Start Page",
        command = lambda : controller.show_frame(StartPage))

        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
     
        button2 = ttk.Button(self, text ="Page 2",
        command = lambda : controller.show_frame(Page2))

        button2.grid(row = 2, column = 1, padx = 10, pady = 10)

class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
         

        label = ttk.Label(self, text ="2nd Page", font = LARGETEXT)
         

        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        button1 = ttk.Button(self, text ="Login Page",
        command = lambda : controller.show_frame(Login))

        button1.grid(row = 1, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Page 2",
        command = lambda : controller.show_frame(Page2))
     

        button2.grid(row = 2, column = 1, padx = 10, pady = 10)


app = app()
app.title('General Revision Quiz')
app.geometry("960x720")

app.mainloop()

