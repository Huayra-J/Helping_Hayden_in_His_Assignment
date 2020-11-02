from tkinter import *
import random
import string

expression = "" 

def int_rand():
    global expression
    expression = ""
    equation.set(random.randint(1,1000000))


def float_rand():
    global expression
    expression = ""
    equation.set(random.uniform(1,1000000))


def low_rand():
    global expression
    expression = ""
    letter=random.choice(string.ascii_letters)
    equation.set(letter.lower())


def cap_rand():
    global expression
    expression = ""
    letter=random.choice(string.ascii_letters)
    equation.set(letter.upper())

if __name__ == "__main__": 

    gui = Tk() 
    gui.configure(background="white") 
    gui.title("Question 5") 
  
    #define GUi size
    gui.geometry("400x480") 
    gui.minsize(400,480)

    equation = StringVar() 
  
    #expressionfield
    expression_field = Entry(gui, textvariable=equation) 
    expression_field.config(font=("Calibri",40))
    expression_field.grid(rowspan=4,columnspan=5, ipadx=80, ipady=40) 
    equation.set('0') 
    
    #buttons
    second = Button(gui, text='int', fg='black', bg='#F4F4F4', 
                  command=int_rand, height=3, width=20) 
    second.grid(row=5, column=0)

    pi = Button(gui, text='float', fg='black', bg='#F4F4F4', 
                  command=float_rand, height=3, width=20) 
    pi.grid(row=5, column=1)
    
    #Row 6:
    square = Button(gui, text='lower case letters', fg='black', bg='#F4F4F4', 
                  command=low_rand, height=3, width=20) 
    square.grid(row=6, column=0)

    multi_inverse = Button(gui, text='upper case letters', fg='black', bg='#F4F4F4', 
                  command=cap_rand, height=3, width=20) 
    multi_inverse.grid(row=6, column=1)

    #flexible buttons gap
    gui.grid_columnconfigure(0, weight = 1)
    gui.grid_columnconfigure(1, weight = 1)
    gui.grid_rowconfigure(0, weight = 1)
    gui.grid_rowconfigure(1, weight = 1)
    gui.grid_rowconfigure(2, weight = 1)
    gui.grid_rowconfigure(3, weight = 1)
    gui.grid_rowconfigure(4, weight = 1)
    gui.grid_rowconfigure(5, weight = 1)
    gui.grid_rowconfigure(6, weight = 1)

    # start the GUI 
    gui.mainloop() 