# import section
# Collections required for sorting dictonary.
import collections #for q2
#q3 import
import turtle
from turtle import *

#q5 
from tkinter import *
import random
import string

userchoice=1
while userchoice!=0:
    userchoice = input("Press 1 or 2 or 3 or 4 or 5 to run solution for 1 or 2 or 3 or 4 or 5 or press 0 to exit: ")
    if int(userchoice)==1:
        #get file object reference to the file
        file = open("HIT137cdu.txt","r")
        #read content of file to string
        data = file.read()
        #get number of occurrences of the substring in the string
        count = data.count("You Make CDU")
        count2 = data.count("Great. You Make CDU")
        print('Number of You make CDU are:', count)
        print('Number of Great. You make CDU are:', count2)
    elif int(userchoice)==2:
        print("Question 2: Solution.....")
        def findwords():
            # Open File to read
            f = open("HIT137cdu.txt","r")
            wordlist = {}
            # For each line in file
            for line in f:
                # For each word in file
                for word in line.split():
                    word = word.lower()
                    # For each letter in word
                    for letter in word:
                        # If letter is not alphabet letter, remove it. For example '!' and '.'.
                        if ord(letter) < 97 or ord(letter) > 122:
                            word = word.replace(letter,'')
                    # If letter not in dictionary, add it, else increase it's count
                    if word not in wordlist:
                        wordlist[word]=1
                    else:
                        wordlist[word]+=1
            # Sort the dict by alphabet
            sortedlist = collections.OrderedDict(sorted(wordlist.items()))
            # Print sorted list
            for k, v in sortedlist.items(): print(k, v)
            f.close()

        # Call function
        findwords()

        # Prevent app from closing.
        print("")
        exit = input("Press enter to close ")

    elif int(userchoice)==3:
        print("Question 3: Solution.....")
        t = Turtle()
        t.shape("turtle")
        t.pensize(5)
        t.speed(2)  
        t.color("#FF4343") 
        wn=turtle.Screen()
        wn.bgcolor("#9BFDFF") 

        #40 pixels as a 'unit'
        #Tan Le - TL
        # - -    |
        #  |     |_

        def draw_T(): 
            t.forward(40) 
            t.right(180) 
            t.forward(20) 
            t.left(90) 
            t.forward(80) 


        def draw_L():
            t.forward(80) 
            t.left(90) 
            t.forward(40) 
        
        t.up()
        t.goto(0, 0)
        t.down()      
        draw_T() 

        t.up()
        t.goto(60, 0)
        t.down()
        draw_L() 

        t.hideturtle() #Turtle hidden after completion

        delay = input("Press enter to quit running")
    elif int(userchoice)==4:
        print("Question 4: Solution.....")
        class CDU:
            'Common base class for CDU colleges'
            StudentCount = 0
            def __init__(self):
                print("CDU class initiated")
        
            def displayStudentCount(self):
                print(f"\n Total students are: {CDU.StudentCount} \n")
        
        class CollegeOfIT(CDU):
            Building_address = "Purple 12, CDU Casuarina Campus"
        
            def __init__(self, name, course):
                print("College of IT class initiated \n")
                self.name = name
                self.course = course
                CDU.StudentCount += 1
        
        class CollegeOfEng(CDU):
            Building_address ="Blue 9(may be), CDU Casuarina Campus"
        
            def __init__(self, name, course):
                print("College of Engineering class initiated \n")
                self.name = name
                self.course = course
                CDU.StudentCount += 1
        
        class CollegeOfEnv(CDU):
            Building_address = "ABC 123, CDU Casuarina Campus \n"
        
            def __init__(self, name, course):
                print("College of Environment class initiated \n")
                self.name = name
                self.course = course
                CDU.StudentCount += 1
        
        student1 = CollegeOfIT("tony ","Bachelor of IT")
        student2 = CollegeOfIT("raj ", "Master of IT")
        
        print(f"Building address for {student1.name} is : {student1.Building_address}")
        print(f"Building address for {student2.name} is : {student2.Building_address}")
        
        student3 = CollegeOfEng("1st student of Eng","Bachelor Engineering")
        student4 = CollegeOfEng("2nd student of Eng", "Master of Engineering")
        
        print( f"Building address for {student3.name} is : {student3.Building_address}")
        print(f"Building address for {student4.name} is : {student4.Building_address}")
        
        student5 = CollegeOfEnv("1st student of Env","Bachelor of Environmental science")
        student6 = CollegeOfEnv("2nd student of Env", "Master of Disaster management")
        
        print(f"Building address for {student5.name} is : {student5.Building_address}")
        print(f"Building address for {student6.name} is : {student6.Building_address}")
        
        parentObject = CDU()
        parentObject.displayStudentCount() 
    elif int(userchoice)==5:
        print("Question 5: Solution.....")
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
    elif int(userchoice)==0:
        print("Thanks!")
        break
    else:
        print("Wrong Choice, Please try 1,2,3,4,5 or press 0 to exit!")