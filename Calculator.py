from tkinter import *
import math

#initiate expression
expression = "" 
  
#basic press method
def press(num): 
    global expression 
    expression = expression + str(num) 
    equation.set(expression) 
  
  
#equal - base of all other advaced method
def equalpress(): 
    try: 
        global expression 
        total = str(eval(expression)) 
        equation.set(total) 
        expression = "" 
    except: 
        equation.set(" error ") 
        expression = "" 
   

def pi():
    try: 
        global expression 
        total = eval(expression)
        result = str(total*3.1415926)
        equation.set(result) 
        expression = ""  
    except: 
        equation.set(" error ") 
        expression = ""


def e():
    try: 
        global expression 
        total = eval(expression)
        result = str(total*2.718281828)
        equation.set(result) 
        expression = ""  
    except: 
        equation.set(" error ") 
        expression = ""


def square():
    try: 
        global expression 

        total = eval(expression)
        result = str(total*total)
        equation.set(result) 
        expression = ""  
    except: 
        equation.set(" error ") 
        expression = "" 


def multi_inverse():
    try: 
        global expression 
        total = eval(expression)
        result = str(1/total)
        equation.set(result) 
        expression = ""  
    except: 
        equation.set(" error ") 
        expression = ""


def absolute():
    try: 
        global expression 
        total = eval(expression)
        if total >= 0:
            result = str(total)
        else:
            result = str(0-total)
        equation.set(result) 
        expression = ""  
    except: 
        equation.set(" error ") 
        expression = ""


def square_root():
    try: 
        global expression 
        total = eval(expression)
        result = str(math.sqrt(total))
        equation.set(result) 
        expression = ""  
    except: 
        equation.set(" error ") 
        expression = ""


def factorial():
    try: 
        global expression 
        total = eval(expression)
        result = str(math.factorial(total))
        equation.set(result) 
        expression = ""  
    except: 
        equation.set(" error ") 
        expression = ""


def tenpower():
    try: 
        global expression 
        total = eval(expression)
        result = str(10**total)
        equation.set(result) 
        expression = ""  
    except: 
        equation.set(" error ") 
        expression = ""


def log():
    try: 
        global expression 
        total = eval(expression)
        result = str(math.log(10,total))
        equation.set(result) 
        expression = ""  
    except: 
        equation.set(" error ") 
        expression = ""


def ln():
    try: 
        global expression 
        total = eval(expression)
        result = str(math.log(2.718281828,total))
        equation.set(result) 
        expression = ""  
    except: 
        equation.set(" error ") 
        expression = ""


def plus_minus():
    try: 
        global expression 
        total = eval(expression)
        result = str(0-total)
        equation.set(result) 
        expression = ""  
    except: 
        equation.set(" error ") 
        expression = ""


def clear(): 
    global expression 
    expression = "" 
    equation.set("0") 
  

def idk():
    global expression
    expression = ""
    equation.set("I'm bad at math, don't know what it does =-=")


if __name__ == "__main__": 

    gui = Tk() 
    gui.configure(background="white") 
    gui.title("Scientific Calculator") 
  
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
    #Row 5:
    second = Button(gui, text='2nd', fg='black', bg='#F4F4F4', 
                  command=idk, height=3, width=10) 
    second.grid(row=5, column=0)

    pi = Button(gui, text='π', fg='black', bg='#F4F4F4', 
                  command=pi, height=3, width=10) 
    pi.grid(row=5, column=1)

    e = Button(gui, text='e', fg='black', bg='#F4F4F4', 
                  command=e, height=3, width=10) 
    e.grid(row=5, column=2)

    ce = Button(gui, text='CE', fg='black', bg='#F4F4F4', 
                  command=clear, height=3, width=10) 
    ce.grid(row=5, column=3)
  
    clear = Button(gui, text='Clear', fg='black', bg='#F40D0D', 
                   command=clear, height=3, width=10) 
    clear.grid(row=5, column=4) 
    
    #Row 6:
    square = Button(gui, text='^2', fg='black', bg='#F4F4F4', 
                  command=square, height=3, width=10) 
    square.grid(row=6, column=0)

    multi_inverse = Button(gui, text='1/x', fg='black', bg='#F4F4F4', 
                  command=multi_inverse, height=3, width=10) 
    multi_inverse.grid(row=6, column=1)

    absolute = Button(gui, text='|x|', fg='black', bg='#F4F4F4', 
                  command=absolute, height=3, width=10) 
    absolute.grid(row=6, column=2)

    exp = Button(gui, text='exp', fg='black', bg='#F4F4F4', 
                  command=idk, height=3, width=10) 
    exp.grid(row=6, column=3)

    mod = Button(gui, text='mod', fg='black', bg='#F4F4F4', 
                  command=lambda: press("%"), height=3, width=10) 
    mod.grid(row=6, column=4)

    #row 7
    square_root = Button(gui, text='√', fg='black', bg='#F4F4F4', 
                  command=square_root, height=3, width=10) 
    square_root.grid(row=7, column=0)

    open_bracket = Button(gui, text='(', fg='black', bg='#F4F4F4', 
                  command=lambda: press("("), height=3, width=10) 
    open_bracket.grid(row=7, column=1)

    close_bracket = Button(gui, text=')', fg='black', bg='#F4F4F4', 
                  command=lambda: press(")"), height=3, width=10) 
    close_bracket.grid(row=7, column=2)

    factorial = Button(gui, text='n!', fg='black', bg='#F4F4F4', 
                  command=factorial, height=3, width=10) 
    factorial.grid(row=7, column=3)

    divide = Button(gui, text=' / ', fg='black', bg='#F4F4F4', 
                    command=lambda: press("/"), height=3, width=10) 
    divide.grid(row=7, column=4) 

    #row 8
    power = Button(gui, text='x^y', fg='black', bg='#F4F4F4', 
                     command=lambda: press('**'), height=3, width=10) 
    power.grid(row=8, column=0)

    button7 = Button(gui, text=' 7 ', fg='black', bg='#F4F4F4', 
                     command=lambda: press(7), height=3, width=10) 
    button7.grid(row=8, column=1) 
  
    button8 = Button(gui, text=' 8 ', fg='black', bg='#F4F4F4', 
                     command=lambda: press(8), height=3, width=10) 
    button8.grid(row=8, column=2) 
  
    button9 = Button(gui, text=' 9 ', fg='black', bg='#F4F4F4', 
                     command=lambda: press(9), height=3, width=10) 
    button9.grid(row=8, column=3) 

    multiply = Button(gui, text=' * ', fg='black', bg='#F4F4F4', 
                      command=lambda: press("*"), height=3, width=10) 
    multiply.grid(row=8, column=4) 

    #row 9
    tenpower = Button(gui, text='10^x', fg='black', bg='#F4F4F4', 
                      command=tenpower, height=3, width=10) 
    tenpower.grid(row=9, column=0)

    button4 = Button(gui, text=' 4 ', fg='black', bg='#F4F4F4', 
                     command=lambda: press(4), height=3, width=10) 
    button4.grid(row=9, column=1) 
  
    button5 = Button(gui, text=' 5 ', fg='black', bg='#F4F4F4', 
                     command=lambda: press(5), height=3, width=10) 
    button5.grid(row=9, column=2) 
  
    button6 = Button(gui, text=' 6 ', fg='black', bg='#F4F4F4', 
                     command=lambda: press(6), height=3, width=10) 
    button6.grid(row=9, column=3) 
  
    minus = Button(gui, text=' - ', fg='black', bg='#F4F4F4', 
                   command=lambda: press("-"), height=3, width=10) 
    minus.grid(row=9, column=4) 

    #row 10
    log = Button(gui, text='log', fg='black', bg='#F4F4F4', 
                   command=log, height=3, width=10) 
    log.grid(row=10, column=0) 
    
    button1 = Button(gui, text=' 1 ', fg='black', bg='#F4F4F4', 
                     command=lambda: press(1), height=3, width=10) 
    button1.grid(row=10, column=1) 
  
    button2 = Button(gui, text=' 2 ', fg='black', bg='#F4F4F4', 
                     command=lambda: press(2), height=3, width=10) 
    button2.grid(row=10, column=2) 
  
    button3 = Button(gui, text=' 3 ', fg='black', bg='#F4F4F4', 
                     command=lambda: press(3), height=3, width=10) 
    button3.grid(row=10, column=3) 
    
    plus = Button(gui, text=' + ', fg='black', bg='#F4F4F4', 
                  command=lambda: press("+"), height=3, width=10) 
    plus.grid(row=10, column=4) 

    #row 11
    ln = Button(gui, text='ln', fg='black', bg='#F4F4F4', 
                  command=ln, height=3, width=10) 
    ln.grid(row=11, column=0) 

    plus_minus = Button(gui, text=' +/- ', fg='black', bg='#F4F4F4', 
                   command=plus_minus, height=3, width=10) 
    plus_minus.grid(row=11, column=1)

    button0 = Button(gui, text=' 0 ', fg='black', bg='#F4F4F4', 
                     command=lambda: press(0), height=3, width=10) 
    button0.grid(row=11, column=2) 

    Decimal= Button(gui, text='.', fg='black', bg='#F4F4F4', 
                    command=lambda: press('.'), height=3, width=10) 
    Decimal.grid(row=11, column=3) 

    equal = Button(gui, text=' = ', fg='black', bg='#5ADCF9', 
                   command=equalpress, height=3, width=10) 
    equal.grid(row=11, column=4) 

    #flexible buttons gap
    gui.grid_columnconfigure(0, weight = 1)
    gui.grid_columnconfigure(1, weight = 1)
    gui.grid_columnconfigure(2, weight = 1)
    gui.grid_columnconfigure(3, weight = 1)
    gui.grid_rowconfigure(0, weight = 1)
    gui.grid_rowconfigure(1, weight = 1)
    gui.grid_rowconfigure(2, weight = 1)
    gui.grid_rowconfigure(3, weight = 1)
    gui.grid_rowconfigure(4, weight = 1)
    gui.grid_rowconfigure(5, weight = 1)
    gui.grid_rowconfigure(6, weight = 1)

    # start the GUI 
    gui.mainloop() 