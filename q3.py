import turtle
from turtle import * 

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





        
                
        




