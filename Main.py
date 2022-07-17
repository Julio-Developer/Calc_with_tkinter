# -*- encoding: utf-8 -*-

# Calculator 

# Import librarys
import tkinter as tk
from tkinter import font


# Create class

class Calc: 

    def __init__(self):

        # Creatig windows
        self.window = tk.Tk()
        self.window.title('Calculator')
        self.window.resizable(0,0)

        # Creating camp insert values
        self.screen_number = tk.Entry(self.window, font='arial 20 bold', bg='#01173b', fg='white')
        self.screen_number.pack()
        

        self.frame = tk.Frame(self.window)
        self.frame.pack()

        # Creating grid and buttons
        self.button_1 = tk.Button(self.frame, bg='orange', text='1', bd=0, font='arial 20 bold', fg='white',width=5, height=3, command=None)
        self.button_1.grid(row=0, column=0)

        self.button_2 = tk.Button(self.frame, bg='orange', text=1, bd=0, font='arial 20 bold', fg='white', width=5, height=3, command=None)
        self.button_2.grid(row=0, column=0)

        # Loop of closed window
        self.window.mainloop()


Calc()

