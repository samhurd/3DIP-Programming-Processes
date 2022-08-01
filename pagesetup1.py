import tkinter as tk
from tkinter import ttk



  
class StartPage(tk.Frame):

    
        label = ttk.Label(text ="Startpage")
         

        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        button1 = ttk.Button(text ="Page 1")

        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  

        button2 = ttk.Button(text ="Page 2")

        button2.grid(row = 2, column = 1, padx = 10, pady = 10)




app = StartPage()
app.mainloop()
