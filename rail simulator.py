import turtle
import time 
import random

screen = turtle.Screen()
screen.setup(1200, 675)
screen.setworldcoordinates(-800, -450, 800, 450)
screen.bgcolor("black")



# TURN THIS ON AND ITS PAIR
# screen.tracer(0)

screen.tracer(0)

# Title Screen

pen_main = turtle.Turtle()
pen_main.speed(0)
pen_main.hideturtle()
pen_main.color("white")
pen_main.pensize(2)
pen_main.penup()
pen_main.goto(0, 400)
pen_main.pendown()
pen_main.write("Rail Emulator", align  = "Center", font = ("Helvetica Neue", 24, "normal"))

# Sunbury Up

pen_main = turtle.Turtle()
pen_main.speed(0)
pen_main.hideturtle()
pen_main.color("white")
pen_main.pensize(2)
pen_main.penup()
pen_main.goto(800, 75)
pen_main.pendown()
pen_main.goto(-450, 75)
pen_main.goto(-800, 425)



# Sunbury Down

pen_main = turtle.Turtle()
pen_main.speed(0)
pen_main.hideturtle()
pen_main.color("white")
pen_main.pensize(2)
pen_main.penup()
pen_main.goto(800, 25)
pen_main.pendown()
pen_main.goto(-450, 25)
pen_main.goto(-800, 375)



# Ballarat Up

pen_main = turtle.Turtle()
pen_main.speed(0)
pen_main.hideturtle()
pen_main.color("white")
pen_main.pensize(2)
pen_main.penup()
pen_main.goto(800, -25)
pen_main.pendown()
pen_main.goto(-800, -25)



# Ballarat Down

pen_main = turtle.Turtle()
pen_main.speed(0)
pen_main.hideturtle()
pen_main.color("white")
pen_main.pensize(2)
pen_main.penup()
pen_main.goto(800, -75)
pen_main.pendown()
pen_main.goto(-800, -75)



# Bendigo Up Crossover

pen_main = turtle.Turtle()
pen_main.speed(0)
pen_main.hideturtle()
pen_main.color("white")
pen_main.pensize(2)
pen_main.penup()
pen_main.goto(-450, -75)
pen_main.pendown()
pen_main.goto(-625, 100)
pen_main.goto(-625, 200)



# Bendigo Down Crossover

pen_main = turtle.Turtle()
pen_main.speed(0)
pen_main.hideturtle()
pen_main.color("white")
pen_main.pensize(2)
pen_main.penup()
pen_main.goto(-450, -25)
pen_main.pendown()
pen_main.goto(-575, 100)
pen_main.goto(-575, 200)



# Jacana Loop Up Broad Gauge

pen_main = turtle.Turtle()
pen_main.speed(0)
pen_main.hideturtle()
pen_main.color("white")
pen_main.pensize(2)
pen_main.penup()
pen_main.goto(-675, 300)
pen_main.pendown()
pen_main.goto(-675, 450)



# Jacana Loop Down Broad Gauge

pen_main = turtle.Turtle()
pen_main.speed(0)
pen_main.hideturtle()
pen_main.color("white")
pen_main.pensize(2)
pen_main.penup()
pen_main.goto(-725, 300)
pen_main.pendown()
pen_main.goto(-725, 450)



# Jacana Loop Standard Gauge Bidirectional

pen_main = turtle.Turtle()
pen_main.speed(0)
pen_main.hideturtle()
pen_main.color("white")
pen_main.pensize(2)
pen_main.penup()
pen_main.goto(-625, 450)
pen_main.pendown()
pen_main.goto(-625, 300)
pen_main.goto(-550, 225)
pen_main.goto(800, 225)



# Ballarate Bidirectional Double Cross Over

pen_main = turtle.Turtle()
pen_main.speed(0)
pen_main.hideturtle()
pen_main.color("white")
pen_main.pensize(2)
pen_main.penup()
pen_main.goto(-150, -25)
pen_main.pendown()
pen_main.goto(-100, -75)
pen_main.penup()
pen_main.goto(-100, -25)
pen_main.pendown()
pen_main.goto(-50, -75)



# Annoying Down Broad Gauge Freight Ballarat to Up Subury Crossover

pen_main = turtle.Turtle()
pen_main.speed(0)
pen_main.hideturtle()
pen_main.color("white")
pen_main.pensize(2)
pen_main.penup()
pen_main.goto(0, -75)
pen_main.pendown()
pen_main.goto(150, 75)



# Annoying Up Broad Gauge Feight Ballarat to Up Sunbury Crossover

pen_main = turtle.Turtle()
pen_main.speed(0)
pen_main.hideturtle()
pen_main.color("white")
pen_main.pensize(2)
pen_main.penup()
pen_main.goto(50, -75)
pen_main.pendown()
pen_main.goto(200, 75)



# Extension of The Annoying Down Broad Gauge Feight Ballarat to Tottenham Yard Crossover

pen_main = turtle.Turtle()
pen_main.speed(0)
pen_main.hideturtle()
pen_main.color("white")
pen_main.pensize(2)
pen_main.penup()
pen_main.goto(200, 25)
pen_main.pendown()
pen_main.goto(300, 125)



# Extension of The Annoying Down Broad Gauge Feight Ballarat to Tottenham Yard Crossover

pen_main = turtle.Turtle()
pen_main.speed(0)
pen_main.hideturtle()
pen_main.color("white")
pen_main.pensize(2)
pen_main.penup()
pen_main.goto(250, 25)
pen_main.pendown()
pen_main.goto(350, 125)

#Turn this off
# pen_main.clear()




#||TRAINS||#



# Sunbury Up Train

pen_Sunbury_Up_Train = turtle.Turtle()
pen_Sunbury_Up_Train.speed(0)
pen_Sunbury_Up_Train.hideturtle()
pen_Sunbury_Up_Train.color("#279FD5")
pen_Sunbury_Up_Train.pensize(4)

def Sunbury_Up_Train():
    pen_Sunbury_Up_Train.penup()
    pen_Sunbury_Up_Train.goto(800, 75)
    pen_Sunbury_Up_Train.pendown()
    pen_Sunbury_Up_Train.goto(-450, 75)
    pen_Sunbury_Up_Train.goto(-800, 425)

    return pen_Sunbury_Up_Train

pen_Sunbury_Up_Train__Useable = Sunbury_Up_Train()
pen_Sunbury_Up_Train__Useable.clear()



# Sunbury Down Train

pen_Sunbury_Down_Train = turtle.Turtle()
pen_Sunbury_Down_Train.speed(0)
pen_Sunbury_Down_Train.hideturtle()
pen_Sunbury_Down_Train.color("#279FD5")
pen_Sunbury_Down_Train.pensize(4)

def Sunbury_Down_Train():
    pen_Sunbury_Down_Train.penup()
    pen_Sunbury_Down_Train.goto(800, 25)
    pen_Sunbury_Down_Train.pendown()
    pen_Sunbury_Down_Train.goto(-450, 25)
    pen_Sunbury_Down_Train.goto(-800, 375)

    return pen_Sunbury_Down_Train

pen_Sunbury_Down_Train__Useable = Sunbury_Down_Train()
pen_Sunbury_Down_Train__Useable.clear()



# Ballarat Up Train

pen_Ballarat_Up_Train = turtle.Turtle()
pen_Ballarat_Up_Train.speed(0)
pen_Ballarat_Up_Train.hideturtle()
pen_Ballarat_Up_Train.color("#8F1A95")
pen_Ballarat_Up_Train.pensize(4)

def Ballarat_Up_Train():
    pen_Ballarat_Up_Train.penup()
    pen_Ballarat_Up_Train.goto(800, -25)
    pen_Ballarat_Up_Train.pendown()
    pen_Ballarat_Up_Train.goto(-800, -25)

    return pen_Ballarat_Up_Train

pen_Ballarat_Up_Train__Useable = Ballarat_Up_Train()
pen_Ballarat_Up_Train__Useable.clear()



# Ballarat Down Train

pen_Ballarat_Down_Train = turtle.Turtle()
pen_Ballarat_Down_Train.speed(0)
pen_Ballarat_Down_Train.hideturtle()
pen_Ballarat_Down_Train.color("#8F1A95")
pen_Ballarat_Down_Train.pensize(4)

def Ballarat_Down_Train():
    pen_Ballarat_Down_Train.penup()
    pen_Ballarat_Down_Train.goto(800, -75)
    pen_Ballarat_Down_Train.pendown()
    pen_Ballarat_Down_Train.goto(-800, -75)

    return pen_Ballarat_Down_Train

pen_Ballarat_Down_Train__Useable = Ballarat_Down_Train()
pen_Ballarat_Down_Train__Useable.clear()



# Bendigo Up Train

pen_Bendigo_Up_Train = turtle.Turtle()
pen_Bendigo_Up_Train.speed(0)
pen_Bendigo_Up_Train.hideturtle()
pen_Bendigo_Up_Train.color("#8F1A95")
pen_Bendigo_Up_Train.pensize(4)

def Bendigo_Up_Train():
    pen_Bendigo_Up_Train.penup()
    pen_Bendigo_Up_Train.goto(800, -25)
    pen_Bendigo_Up_Train.pendown()
    pen_Bendigo_Up_Train.goto(-450, -25)
    pen_Bendigo_Up_Train.goto(-575, 100)
    pen_Bendigo_Up_Train.goto(-575, 200)
    pen_Bendigo_Up_Train.goto(-800, 425)

    return pen_Bendigo_Up_Train

pen_Bendigo_Up_Train__Useable = Bendigo_Up_Train()
pen_Bendigo_Up_Train__Useable.clear()



# Bendigo Down Train

pen_Bendigo_Down_Train = turtle.Turtle()
pen_Bendigo_Down_Train.speed(0)
pen_Bendigo_Down_Train.hideturtle()
pen_Bendigo_Down_Train.color("#8F1A95")
pen_Bendigo_Down_Train.pensize(4)

def Bendigo_Down_Train():
    pen_Bendigo_Down_Train.penup()
    pen_Bendigo_Down_Train.goto(800, -75)
    pen_Bendigo_Down_Train.pendown()
    pen_Bendigo_Down_Train.goto(-450, -75)
    pen_Bendigo_Down_Train.goto(-625, 100)
    pen_Bendigo_Down_Train.goto(-625, 200)
    pen_Bendigo_Down_Train.goto(-800, 375)
    
    return pen_Bendigo_Down_Train

pen_Bendigo_Down_Train__Useable = Bendigo_Down_Train()
pen_Bendigo_Down_Train__Useable.clear()



# Ballarat Up Freight Train

pen_Ballarat_Up_Freight_Train = turtle.Turtle()
pen_Ballarat_Up_Freight_Train.speed(0)
pen_Ballarat_Up_Freight_Train.hideturtle()
pen_Ballarat_Up_Freight_Train.color("#ff9000")
pen_Ballarat_Up_Freight_Train.pensize(4)


def Ballarat_Up_Freight_Train():
    pen_Ballarat_Up_Freight_Train.penup()
    pen_Ballarat_Up_Freight_Train.goto(-800, -25)
    pen_Ballarat_Up_Freight_Train.pendown()
    pen_Ballarat_Up_Freight_Train.goto(50, -25)
    pen_Ballarat_Up_Freight_Train.goto(150, 75 )
    pen_Ballarat_Up_Freight_Train.goto(250, 75 )
    pen_Ballarat_Up_Freight_Train.goto(300, 125)

    return pen_Ballarat_Up_Freight_Train

pen_Ballarat_Up_Freight_Train__Useable = Ballarat_Up_Freight_Train()
pen_Ballarat_Up_Freight_Train__Useable.clear()



# Ballarat Down Freight Train

pen_Ballarat_Down_Freight_Train = turtle.Turtle()
pen_Ballarat_Down_Freight_Train.speed(0)
pen_Ballarat_Down_Freight_Train.hideturtle()
pen_Ballarat_Down_Freight_Train.color("#ff9000")
pen_Ballarat_Down_Freight_Train.pensize(4)

def Ballarat_Down_Freight_Train():
    pen_Ballarat_Down_Freight_Train.penup()
    pen_Ballarat_Down_Freight_Train.goto(-800, -75)
    pen_Ballarat_Down_Freight_Train.pendown()
    pen_Ballarat_Down_Freight_Train.goto(50, -75)
    pen_Ballarat_Down_Freight_Train.goto(150, 25)
    pen_Ballarat_Down_Freight_Train.goto(250, 25)
    pen_Ballarat_Down_Freight_Train.goto(350, 125)

    return pen_Ballarat_Down_Freight_Train

pen_Ballarat_Down_Freight_Train__Useable = Ballarat_Down_Freight_Train()
pen_Ballarat_Down_Freight_Train__Useable.clear()



# Bendigo Up Freight Train

pen_Bendigo_Up_Freight_Train = turtle.Turtle()
pen_Bendigo_Up_Freight_Train.speed(0)
pen_Bendigo_Up_Freight_Train.hideturtle()
pen_Bendigo_Up_Freight_Train.color("#ff9000")
pen_Bendigo_Up_Freight_Train.pensize(4)

def Bendigo_Up_Freight_Train():

    pen_Bendigo_Up_Freight_Train.penup()
    pen_Bendigo_Up_Freight_Train.goto(300, 125)
    pen_Bendigo_Up_Freight_Train.pendown()
    pen_Bendigo_Up_Freight_Train.goto(250, 75)
    pen_Bendigo_Up_Freight_Train.goto(150, 75)
    pen_Bendigo_Up_Freight_Train.goto(50, -25)
    pen_Bendigo_Up_Freight_Train.goto(-450, -25)
    pen_Bendigo_Up_Freight_Train.goto(-575, 100)
    pen_Bendigo_Up_Freight_Train.goto(-575, 200)
    pen_Bendigo_Up_Freight_Train.goto(-800, 425)
    
    return pen_Bendigo_Up_Freight_Train

pen_Bendigo_Up_Freight_Train__Useable = Bendigo_Up_Freight_Train()
pen_Bendigo_Up_Freight_Train__Useable.clear()



# Bendigo Down Freight Train

pen_Bendigo_Down_Freight_Train = turtle.Turtle()
pen_Bendigo_Down_Freight_Train.speed(0)
pen_Bendigo_Down_Freight_Train.hideturtle()
pen_Bendigo_Down_Freight_Train.color("#ff9000")
pen_Bendigo_Down_Freight_Train.pensize(4)

def Bendigo_Down_Freight_Train():
    pen_Bendigo_Down_Freight_Train.penup()
    pen_Bendigo_Down_Freight_Train.goto(350, 125)
    pen_Bendigo_Down_Freight_Train.pendown()
    pen_Bendigo_Down_Freight_Train.goto(250, 25)
    pen_Bendigo_Down_Freight_Train.goto(150, 25)
    pen_Bendigo_Down_Freight_Train.goto(50, -75)
    pen_Bendigo_Down_Freight_Train.goto(-450, -75)
    pen_Bendigo_Down_Freight_Train.goto(-625, 100)
    pen_Bendigo_Down_Freight_Train.goto(-625, 200)
    pen_Bendigo_Down_Freight_Train.goto(-800, 375)

    return pen_Bendigo_Down_Freight_Train

pen_Bendigo_Down_Freight_Train__Useable = Bendigo_Down_Freight_Train()
pen_Bendigo_Down_Freight_Train__Useable.clear()



# Jacana Loop Up Freight Train

pen_Jacana_Loop_Up_Freight_Train = turtle.Turtle()
pen_Jacana_Loop_Up_Freight_Train.speed(0)
pen_Jacana_Loop_Up_Freight_Train.hideturtle()
pen_Jacana_Loop_Up_Freight_Train.color("#ff9000")
pen_Jacana_Loop_Up_Freight_Train.pensize(4)


def Jacana_Loop_Up_Freight_Train():
    pen_Jacana_Loop_Up_Freight_Train.penup()
    pen_Jacana_Loop_Up_Freight_Train.goto(300, 125)
    pen_Jacana_Loop_Up_Freight_Train.pendown()
    pen_Jacana_Loop_Up_Freight_Train.goto(250, 75)
    pen_Jacana_Loop_Up_Freight_Train.goto(150, 75)
    pen_Jacana_Loop_Up_Freight_Train.goto(50, -25)
    pen_Jacana_Loop_Up_Freight_Train.goto(-450, -25)
    pen_Jacana_Loop_Up_Freight_Train.goto(-575, 100)
    pen_Jacana_Loop_Up_Freight_Train.goto(-575, 200)
    pen_Jacana_Loop_Up_Freight_Train.goto(-675, 300)
    pen_Jacana_Loop_Up_Freight_Train.goto(-675, 450)

    return pen_Jacana_Loop_Up_Freight_Train

pen_Jacana_Loop_Up_Freight_Train__Useable = Jacana_Loop_Up_Freight_Train()
pen_Jacana_Loop_Up_Freight_Train__Useable.clear()



# Jacana Loop Down Freight Train

pen_Jacana_Loop_Down_Freight_Train = turtle.Turtle()
pen_Jacana_Loop_Down_Freight_Train.speed(0)
pen_Jacana_Loop_Down_Freight_Train.hideturtle()
pen_Jacana_Loop_Down_Freight_Train.color("#ff9000")
pen_Jacana_Loop_Down_Freight_Train.pensize(4)

def Jacana_Loop_Down_Freight_Train():
    pen_Jacana_Loop_Down_Freight_Train.penup()
    pen_Jacana_Loop_Down_Freight_Train.goto(350, 125)
    pen_Jacana_Loop_Down_Freight_Train.pendown()
    pen_Jacana_Loop_Down_Freight_Train.goto(250, 25)
    pen_Jacana_Loop_Down_Freight_Train.goto(150, 25)
    pen_Jacana_Loop_Down_Freight_Train.goto(50, -75)
    pen_Jacana_Loop_Down_Freight_Train.goto(-450, -75)
    pen_Jacana_Loop_Down_Freight_Train.goto(-625, 100)
    pen_Jacana_Loop_Down_Freight_Train.goto(-625, 200)
    pen_Jacana_Loop_Down_Freight_Train.goto(-725, 300)
    pen_Jacana_Loop_Down_Freight_Train.goto(-725, 450)

    return pen_Jacana_Loop_Down_Freight_Train

pen_Jacana_Loop_Down_Freight_Train__Useable = Jacana_Loop_Down_Freight_Train()
pen_Jacana_Loop_Down_Freight_Train__Useable.clear()



# ||| Defintions



# Definition Of Sunbury Up

pen_Definition_Of_Sunbury_Up = turtle.Turtle()
pen_Definition_Of_Sunbury_Up.speed(0)
pen_Definition_Of_Sunbury_Up.hideturtle()
pen_Definition_Of_Sunbury_Up.color("#279FD5")
pen_Definition_Of_Sunbury_Up.pensize(2)

def Definition_Of_Sunbury_Up():
    pen_Definition_Of_Sunbury_Up.penup()
    pen_Definition_Of_Sunbury_Up.goto(799,395)
    pen_Definition_Of_Sunbury_Up.pendown()
    pen_Definition_Of_Sunbury_Up.write("Sunbury Up", align = "right", font = ("Helvetica Neue", 24, "normal" ))

    return pen_Definition_Of_Sunbury_Up

pen_Definition_Of_Sunbury_Up__Useable = Definition_Of_Sunbury_Up()
pen_Definition_Of_Sunbury_Up__Useable.clear()



# Definition Of Sunbury Down

pen_Definition_Of_Sunbury_Down = turtle.Turtle()
pen_Definition_Of_Sunbury_Down.speed(0)
pen_Definition_Of_Sunbury_Down.hideturtle()
pen_Definition_Of_Sunbury_Down.color("#279FD5")
pen_Definition_Of_Sunbury_Down.pensize(2)

def Definition_Of_Sunbury_Down():
    pen_Definition_Of_Sunbury_Down.penup()
    pen_Definition_Of_Sunbury_Down.goto(799,395)
    pen_Definition_Of_Sunbury_Down.pendown()
    pen_Definition_Of_Sunbury_Down.write("Sunbury Down", align = "right", font = ("Helvetica Neue", 24, "normal" ))

    return pen_Definition_Of_Sunbury_Down

pen_Definition_Of_Sunbury_Down__Useable = Definition_Of_Sunbury_Down()
pen_Definition_Of_Sunbury_Down__Useable.clear()



# Definition Of Ballarat Up

pen_Definition_Of_Ballarat_Up = turtle.Turtle()
pen_Definition_Of_Ballarat_Up.speed(0)
pen_Definition_Of_Ballarat_Up.hideturtle()
pen_Definition_Of_Ballarat_Up.color("#8F1A95")
pen_Definition_Of_Ballarat_Up.pensize(2)

def Definition_Of_Ballarat_Up():
    pen_Definition_Of_Ballarat_Up.penup()
    pen_Definition_Of_Ballarat_Up.goto(799,395)
    pen_Definition_Of_Ballarat_Up.pendown()
    pen_Definition_Of_Ballarat_Up.write("Ballarat Up", align = "right", font = ("Helvetica Neue", 24, "normal" ))

    return pen_Definition_Of_Ballarat_Up

pen_Definition_Of_Ballarat_Up__Useable = Definition_Of_Ballarat_Up()
pen_Definition_Of_Ballarat_Up__Useable.clear()



# Definition Of Ballarat Down

pen_Definition_Of_Ballarat_Down = turtle.Turtle()
pen_Definition_Of_Ballarat_Down.speed(0)
pen_Definition_Of_Ballarat_Down.hideturtle()
pen_Definition_Of_Ballarat_Down.color("#8F1A95")
pen_Definition_Of_Ballarat_Down.pensize(2)

def Definition_Of_Ballarat_Down():
    pen_Definition_Of_Ballarat_Down.penup()
    pen_Definition_Of_Ballarat_Down.goto(799,395)
    pen_Definition_Of_Ballarat_Down.pendown()
    pen_Definition_Of_Ballarat_Down.write("Ballarat Down", align = "right", font = ("Helvetica Neue", 24, "normal" ))

    return pen_Definition_Of_Ballarat_Down

pen_Definition_Of_Ballarat_Down__Useable = Definition_Of_Ballarat_Down()
pen_Definition_Of_Ballarat_Down__Useable.clear()



# Definition Of Bendigo Up

pen_Definition_Of_Bendigo_Up = turtle.Turtle()
pen_Definition_Of_Bendigo_Up.speed(0)
pen_Definition_Of_Bendigo_Up.hideturtle()
pen_Definition_Of_Bendigo_Up.color("#8F1A95")
pen_Definition_Of_Bendigo_Up.pensize(2)

def Definition_Of_Bendigo_Up():
    pen_Definition_Of_Bendigo_Up.penup()
    pen_Definition_Of_Bendigo_Up.goto(799,395)
    pen_Definition_Of_Bendigo_Up.pendown()
    pen_Definition_Of_Bendigo_Up.write("Bendigo Up", align = "right", font = ("Helvetica Neue", 24, "normal" ))

    return pen_Definition_Of_Bendigo_Up

pen_Definition_Of_Bendigo_Up__Useable = Definition_Of_Bendigo_Up()
pen_Definition_Of_Bendigo_Up__Useable.clear()



# Definition Of Bendigo Down

pen_Definition_Of_Bendigo_Down = turtle.Turtle()
pen_Definition_Of_Bendigo_Down.speed(0)
pen_Definition_Of_Bendigo_Down.hideturtle()
pen_Definition_Of_Bendigo_Down.color("#8F1A95")
pen_Definition_Of_Bendigo_Down.pensize(2)

def Definition_Of_Bendigo_Down():
    pen_Definition_Of_Bendigo_Down.penup()
    pen_Definition_Of_Bendigo_Down.goto(799,395)
    pen_Definition_Of_Bendigo_Down.pendown()
    pen_Definition_Of_Bendigo_Down.write("Bendigo Down", align = "right", font = ("Helvetica Neue", 24, "normal" ))

    return pen_Definition_Of_Bendigo_Down

pen_Definition_Of_Bendigo_Down__Useable = Definition_Of_Bendigo_Down()
pen_Definition_Of_Bendigo_Down__Useable.clear()



# Definition Of Ballarat Up Freight

pen_Definition_Of_Ballarat_Up_Freight = turtle.Turtle()
pen_Definition_Of_Ballarat_Up_Freight.speed(0)
pen_Definition_Of_Ballarat_Up_Freight.hideturtle()
pen_Definition_Of_Ballarat_Up_Freight.color("#ff9000")
pen_Definition_Of_Ballarat_Up_Freight.pensize(2)

def Definition_Of_Ballarat_Up_Freight():
    pen_Definition_Of_Ballarat_Up_Freight.penup()
    pen_Definition_Of_Ballarat_Up_Freight.goto(799,395)
    pen_Definition_Of_Ballarat_Up_Freight.pendown()
    pen_Definition_Of_Ballarat_Up_Freight.write("Ballarat Up Freight", align = "right", font = ("Helvetica Neue", 24, "normal" ))

    return pen_Definition_Of_Ballarat_Up_Freight

pen_Definition_Of_Ballarat_Up_Freight__Useable = Definition_Of_Ballarat_Up_Freight()
pen_Definition_Of_Ballarat_Up_Freight__Useable.clear()



# Definition Of Ballarat Down Freight

pen_Definition_Of_Ballarat_Down_Freight = turtle.Turtle()
pen_Definition_Of_Ballarat_Down_Freight.speed(0)
pen_Definition_Of_Ballarat_Down_Freight.hideturtle()
pen_Definition_Of_Ballarat_Down_Freight.color("#ff9000")
pen_Definition_Of_Ballarat_Down_Freight.pensize(2)

def Definition_Of_Ballarat_Down_Freight():
    pen_Definition_Of_Ballarat_Down_Freight.penup()
    pen_Definition_Of_Ballarat_Down_Freight.goto(799,395)
    pen_Definition_Of_Ballarat_Down_Freight.pendown()
    pen_Definition_Of_Ballarat_Down_Freight.write("Ballarat Down Freight", align = "right", font = ("Helvetica Neue", 24, "normal" ))

    return pen_Definition_Of_Ballarat_Down_Freight

pen_Definition_Of_Ballarat_Down_Freight__Useable = Definition_Of_Ballarat_Down_Freight()
pen_Definition_Of_Ballarat_Down_Freight__Useable.clear()









#||Signals||#

#||| Diagonals: 25 by 25 out, then in a 15 : 15 right triangle
#||| Cardinals: 35 out, then in a root(10) : root(10) right traingle



# Signal Red Sunbury Up 11

pen_Signal_Red_11 = turtle.Turtle()
pen_Signal_Red_11.speed(0)
pen_Signal_Red_11.hideturtle()
pen_Signal_Red_11.color("#FF0000")
pen_Signal_Red_11.pensize(2)

def Signal_Red_11_Sunbury_Up():
    pen_Signal_Red_11.penup()
    pen_Signal_Red_11.goto(-750, 375)
    pen_Signal_Red_11.begin_fill()
    pen_Signal_Red_11.pendown()
    pen_Signal_Red_11.goto(-765, 375)
    pen_Signal_Red_11.goto(-750, 390)
    pen_Signal_Red_11.goto(-750, 375)
    pen_Signal_Red_11.end_fill()

    return pen_Signal_Red_11

pen_Signal_Red_11__Useable = Signal_Red_11_Sunbury_Up()
pen_Signal_Red_11__Useable.clear()



# Signal Red 12 Sunbury Down

pen_Signal_Red_12 = turtle.Turtle()
pen_Signal_Red_12.speed(0)
pen_Signal_Red_12.hideturtle()
pen_Signal_Red_12.color("#FF0000")
pen_Signal_Red_12.pensize(2)

def Signal_Red_12_Sunbury_Up():
    pen_Signal_Red_12.penup()
    pen_Signal_Red_12.goto(-185, 75)
    pen_Signal_Red_12.begin_fill()
    pen_Signal_Red_12.pendown()
    pen_Signal_Red_12.goto(-195, 65)
    pen_Signal_Red_12.goto(-195, 85)
    pen_Signal_Red_12.goto(-185, 75)
    pen_Signal_Red_12.end_fill()

    return pen_Signal_Red_12

pen_Signal_Red_12__Useable = Signal_Red_12_Sunbury_Up()
pen_Signal_Red_12__Useable.clear()



# Signal Red 21 Sunbury Down 

pen_Signal_Red_21 = turtle.Turtle()
pen_Signal_Red_21.speed(0)
pen_Signal_Red_21.hideturtle()
pen_Signal_Red_21.color("#FF0000")
pen_Signal_Red_21.pensize(2)

def Signal_Red_21_Sunbury_Down():
    pen_Signal_Red_21.penup()
    pen_Signal_Red_21.goto(335, 25)
    pen_Signal_Red_21.begin_fill()
    pen_Signal_Red_21.pendown()
    pen_Signal_Red_21.goto(345, 15)
    pen_Signal_Red_21.goto(345, 35)
    pen_Signal_Red_21.goto(335, 25)
    pen_Signal_Red_21.end_fill()

    return pen_Signal_Red_21

pen_Signal_Red_21__Useable = Signal_Red_21_Sunbury_Down()
pen_Signal_Red_21__Useable.clear()



# Signal Red 22 Sunbury Up

pen_Signal_Red_22 = turtle.Turtle()
pen_Signal_Red_22.speed(0)
pen_Signal_Red_22.hideturtle()
pen_Signal_Red_22.color("#FF0000")
pen_Signal_Red_22.pensize(2)

def Signal_Red_22_Sunbury_Down():
    pen_Signal_Red_22.penup()
    pen_Signal_Red_22.goto(-415, 25)
    pen_Signal_Red_22.begin_fill()
    pen_Signal_Red_22.pendown()
    pen_Signal_Red_22.goto(-405, 15)
    pen_Signal_Red_22.goto(-405, 35)
    pen_Signal_Red_22.goto(-415, 25)
    pen_Signal_Red_22.end_fill()

    return pen_Signal_Red_22

pen_Signal_Red_22__Useable = Signal_Red_22_Sunbury_Down()
pen_Signal_Red_22__Useable.clear()



# Signal Red 31 Ballarat Up

pen_Signal_Red_31 = turtle.Turtle()
pen_Signal_Red_31.speed(0)
pen_Signal_Red_31.hideturtle()
pen_Signal_Red_31.color("#FF0000")
pen_Signal_Red_31.pensize(2)

def Signal_Red_31_Ballarat_Up():
    pen_Signal_Red_31.penup()
    pen_Signal_Red_31.goto(-535, -25)
    pen_Signal_Red_31.begin_fill()
    pen_Signal_Red_31.pendown()
    pen_Signal_Red_31.goto(-545, -35)
    pen_Signal_Red_31.goto(-545, -15)
    pen_Signal_Red_31.goto(-535, -25)
    pen_Signal_Red_31.end_fill()

    return pen_Signal_Red_31

pen_Signal_Red_31__Useable = Signal_Red_31_Ballarat_Up()
pen_Signal_Red_31__Useable.clear()



# Signal Red 32 Ballarat Bendigo Up

pen_Signal_Red_32 = turtle.Turtle()
pen_Signal_Red_32.speed(0)
pen_Signal_Red_32.hideturtle()
pen_Signal_Red_32.color("#FF0000")
pen_Signal_Red_32.pensize(2)

def Signal_Red_32_Ballarat_Bendigo_Up():
    pen_Signal_Red_32.penup()
    pen_Signal_Red_32.goto(-185, -25)
    pen_Signal_Red_32.begin_fill()
    pen_Signal_Red_32.pendown()
    pen_Signal_Red_32.goto(-195, -35)
    pen_Signal_Red_32.goto(-195, -15)
    pen_Signal_Red_32.goto(-185, -25)
    pen_Signal_Red_32.end_fill()

    return pen_Signal_Red_32

pen_Signal_Red_32__Useable = Signal_Red_32_Ballarat_Bendigo_Up()
pen_Signal_Red_32__Useable.clear()



# Signal Red 41 Ballarat Bendigo Down 

pen_Signal_Red_41 = turtle.Turtle()
pen_Signal_Red_41.speed(0)
pen_Signal_Red_41.hideturtle()
pen_Signal_Red_41.color("#FF0000")
pen_Signal_Red_41.pensize(2)

def Signal_Red_41_Ballarat_Bendigo_Down():
    pen_Signal_Red_41.penup()
    pen_Signal_Red_41.goto(335, -75)
    pen_Signal_Red_41.begin_fill()
    pen_Signal_Red_41.pendown()
    pen_Signal_Red_41.goto(345, -85)
    pen_Signal_Red_41.goto(345, -65)
    pen_Signal_Red_41.goto(335, -75)
    pen_Signal_Red_41.end_fill()

    return pen_Signal_Red_41

pen_Signal_Red_41__Useable = Signal_Red_41_Ballarat_Bendigo_Down()
pen_Signal_Red_41__Useable.clear()



# Signal Red 42 Ballarat Bendigo Down 

pen_Signal_Red_42 = turtle.Turtle()
pen_Signal_Red_42.speed(0)
pen_Signal_Red_42.hideturtle()
pen_Signal_Red_42.color("#FF0000")
pen_Signal_Red_42.pensize(2)

def Signal_Red_42_Ballarat_Bendigo_Down():
    pen_Signal_Red_42.penup()
    pen_Signal_Red_42.goto(-415, -75)
    pen_Signal_Red_42.begin_fill()
    pen_Signal_Red_42.pendown()
    pen_Signal_Red_42.goto(-405, -85)
    pen_Signal_Red_42.goto(-405, -65)
    pen_Signal_Red_42.goto(-415, -75)
    pen_Signal_Red_42.end_fill()

    return pen_Signal_Red_42

pen_Signal_Red_42__Useable = Signal_Red_42_Ballarat_Bendigo_Down()
pen_Signal_Red_42__Useable.clear()



# Signal Red 51 Freight Down

pen_Signal_Red_51 = turtle.Turtle()
pen_Signal_Red_51.speed(0)
pen_Signal_Red_51.hideturtle()
pen_Signal_Red_51.color("#FF0000")
pen_Signal_Red_51.pensize(2)

def Signal_Red_51_Freight_Down():
    pen_Signal_Red_51.penup()
    pen_Signal_Red_51.goto(325, 100)
    pen_Signal_Red_51.begin_fill()
    pen_Signal_Red_51.pendown()
    pen_Signal_Red_51.goto(340, 100)
    pen_Signal_Red_51.goto(325, 115)
    pen_Signal_Red_51.goto(325, 100)
    pen_Signal_Red_51.end_fill()

    return pen_Signal_Red_51

pen_Signal_Red_51__Useable = Signal_Red_51_Freight_Down()
pen_Signal_Red_51__Useable.clear()














# Signal Green Sunbury Up 11

pen_Signal_Green_11 = turtle.Turtle()
pen_Signal_Green_11.speed(0)
pen_Signal_Green_11.hideturtle()
pen_Signal_Green_11.color("#00FF00")
pen_Signal_Green_11.pensize(2)

def Signal_Green_11_Sunbury_Up():
    pen_Signal_Green_11.penup()
    pen_Signal_Green_11.goto(-750, 375)
    pen_Signal_Green_11.begin_fill()
    pen_Signal_Green_11.pendown()
    pen_Signal_Green_11.goto(-765, 375)
    pen_Signal_Green_11.goto(-750, 390)
    pen_Signal_Green_11.goto(-750, 375)
    pen_Signal_Green_11.end_fill()

    return pen_Signal_Green_11

pen_Signal_Green_11__Useable = Signal_Green_11_Sunbury_Up()
pen_Signal_Green_11__Useable.clear()



# Signal Green 12 Sunbury Down

pen_Signal_Green_12 = turtle.Turtle()
pen_Signal_Green_12.speed(0)
pen_Signal_Green_12.hideturtle()
pen_Signal_Green_12.color("#00FF00")
pen_Signal_Green_12.pensize(2)

def Signal_Green_12_Sunbury_Up():
    pen_Signal_Green_12.penup()
    pen_Signal_Green_12.goto(-185, 75)
    pen_Signal_Green_12.begin_fill()
    pen_Signal_Green_12.pendown()
    pen_Signal_Green_12.goto(-195, 65)
    pen_Signal_Green_12.goto(-195, 85)
    pen_Signal_Green_12.goto(-185, 75)
    pen_Signal_Green_12.end_fill()

    return pen_Signal_Green_12

pen_Signal_Green_12__Useable = Signal_Green_12_Sunbury_Up()
pen_Signal_Green_12__Useable.clear()



# Signal Green 21 Sunbury Down

pen_Signal_Green_21 = turtle.Turtle()
pen_Signal_Green_21.speed(0)
pen_Signal_Green_21.hideturtle()
pen_Signal_Green_21.color("#00FF00")
pen_Signal_Green_21.pensize(2)

def Signal_Green_21_Sunbury_Down():
    pen_Signal_Green_21.penup()
    pen_Signal_Green_21.goto(335, 25)
    pen_Signal_Green_21.begin_fill()
    pen_Signal_Green_21.pendown()
    pen_Signal_Green_21.goto(345, 15)
    pen_Signal_Green_21.goto(345, 35)
    pen_Signal_Green_21.goto(335, 25)
    pen_Signal_Green_21.end_fill()

    return pen_Signal_Green_21

pen_Signal_Green_21__Useable = Signal_Green_21_Sunbury_Down()
pen_Signal_Green_21__Useable.clear()



# Signal Green 22 Sunbury Up

pen_Signal_Green_22 = turtle.Turtle()
pen_Signal_Green_22.speed(0)
pen_Signal_Green_22.hideturtle()
pen_Signal_Green_22.color("#00FF00")
pen_Signal_Green_22.pensize(2)

def Signal_Green_22_Sunbury_Down():
    pen_Signal_Green_22.penup()
    pen_Signal_Green_22.goto(-415, 25)
    pen_Signal_Green_22.begin_fill()
    pen_Signal_Green_22.pendown()
    pen_Signal_Green_22.goto(-405, 15)
    pen_Signal_Green_22.goto(-405, 35)
    pen_Signal_Green_22.goto(-415, 25)
    pen_Signal_Green_22.end_fill()

    return pen_Signal_Green_22

pen_Signal_Green_22__Useable = Signal_Green_22_Sunbury_Down()
pen_Signal_Green_22__Useable.clear()



# Signal Green 31 Ballarat Up

pen_Signal_Green_31 = turtle.Turtle()
pen_Signal_Green_31.speed(0)
pen_Signal_Green_31.hideturtle()
pen_Signal_Green_31.color("#00FF00")
pen_Signal_Green_31.pensize(2)

def Signal_Green_31_Ballarat_Up():
    pen_Signal_Green_31.penup()
    pen_Signal_Green_31.goto(-535, -25)
    pen_Signal_Green_31.begin_fill()
    pen_Signal_Green_31.pendown()
    pen_Signal_Green_31.goto(-545, -35)
    pen_Signal_Green_31.goto(-545, -15)
    pen_Signal_Green_31.goto(-535, -25)
    pen_Signal_Green_31.end_fill()

    return pen_Signal_Green_31

pen_Signal_Green_31__Useable = Signal_Green_31_Ballarat_Up()
pen_Signal_Green_31__Useable.clear()



# Signal Green 32 Ballarat Bendigo Up

pen_Signal_Green_32 = turtle.Turtle()
pen_Signal_Green_32.speed(0)
pen_Signal_Green_32.hideturtle()
pen_Signal_Green_32.color("#00FF00")
pen_Signal_Green_32.pensize(2)

def Signal_Green_32_Ballarat_Bendigo_Up():
    pen_Signal_Green_32.penup()
    pen_Signal_Green_32.goto(-185, -25)
    pen_Signal_Green_32.begin_fill()
    pen_Signal_Green_32.pendown()
    pen_Signal_Green_32.goto(-195, -35)
    pen_Signal_Green_32.goto(-195, -15)
    pen_Signal_Green_32.goto(-185, -25)
    pen_Signal_Green_32.end_fill()

    return pen_Signal_Green_32

pen_Signal_Green_32__Useable = Signal_Green_32_Ballarat_Bendigo_Up()
pen_Signal_Green_32__Useable.clear()



# Signal Green 41 Ballarat Bendigo Down

pen_Signal_Green_41 = turtle.Turtle()
pen_Signal_Green_41.speed(0)
pen_Signal_Green_41.hideturtle()
pen_Signal_Green_41.color("#00FF00")
pen_Signal_Green_41.pensize(2)

def Signal_Green_41_Ballarat_Bendigo_Down():
    pen_Signal_Green_41.penup()
    pen_Signal_Green_41.goto(335, -75)
    pen_Signal_Green_41.begin_fill()
    pen_Signal_Green_41.pendown()
    pen_Signal_Green_41.goto(345, -85)
    pen_Signal_Green_41.goto(345, -65)
    pen_Signal_Green_41.goto(335, -75)
    pen_Signal_Green_41.end_fill()

    return pen_Signal_Green_41

pen_Signal_Green_41__Useable = Signal_Green_41_Ballarat_Bendigo_Down()
pen_Signal_Green_41__Useable.clear()



# Signal Green 42 Ballarat Bendigo Down

pen_Signal_Green_42 = turtle.Turtle()
pen_Signal_Green_42.speed(0)
pen_Signal_Green_42.hideturtle()
pen_Signal_Green_42.color("#00FF00")
pen_Signal_Green_42.pensize(2)

def Signal_Green_42_Ballarat_Bendigo_Down():
    pen_Signal_Green_42.penup()
    pen_Signal_Green_42.goto(-415, -75)
    pen_Signal_Green_42.begin_fill()
    pen_Signal_Green_42.pendown()
    pen_Signal_Green_42.goto(-405, -85)
    pen_Signal_Green_42.goto(-405, -65)
    pen_Signal_Green_42.goto(-415, -75)
    pen_Signal_Green_42.end_fill()

    return pen_Signal_Green_42

pen_Signal_Green_42__Useable = Signal_Green_42_Ballarat_Bendigo_Down()
pen_Signal_Green_42__Useable.clear()



# Signal Green 51 Freight Down

pen_Signal_Green_51 = turtle.Turtle()
pen_Signal_Green_51.speed(0)
pen_Signal_Green_51.hideturtle()
pen_Signal_Green_51.color("#00FF00")
pen_Signal_Green_51.pensize(2)

def Signal_Green_51_Freight_Down():
    pen_Signal_Green_51.penup()
    pen_Signal_Green_51.goto(325, 100)
    pen_Signal_Green_51.begin_fill()
    pen_Signal_Green_51.pendown()
    pen_Signal_Green_51.goto(340, 100)
    pen_Signal_Green_51.goto(325, 115)
    pen_Signal_Green_51.goto(325, 100)
    pen_Signal_Green_51.end_fill()

    return pen_Signal_Green_51

pen_Signal_Green_51__Useable = Signal_Green_51_Freight_Down()
pen_Signal_Green_51__Useable.clear()







# Track Confirmations [[Green]]





# Sunbury Up Confirmation

pen_Sunbury_Up_Confirmation = turtle.Turtle()
pen_Sunbury_Up_Confirmation.speed(0)
pen_Sunbury_Up_Confirmation.hideturtle()
pen_Sunbury_Up_Confirmation.color("#00FF00")
pen_Sunbury_Up_Confirmation.pensize(4)

def Sunbury_Up_Confirmation():
    pen_Sunbury_Up_Confirmation.penup()
    pen_Sunbury_Up_Confirmation.goto(800, 75)
    pen_Sunbury_Up_Confirmation.pendown()
    pen_Sunbury_Up_Confirmation.goto(-450, 75)
    pen_Sunbury_Up_Confirmation.goto(-800, 425)

    return pen_Sunbury_Up_Confirmation

pen_Sunbury_Up_Confirmation__Useable = Sunbury_Up_Confirmation()
pen_Sunbury_Up_Confirmation__Useable.clear()



# Sunbury Down Confirmation

pen_Sunbury_Down_Confirmation = turtle.Turtle()
pen_Sunbury_Down_Confirmation.speed(0)
pen_Sunbury_Down_Confirmation.hideturtle()
pen_Sunbury_Down_Confirmation.color("#00FF00")
pen_Sunbury_Down_Confirmation.pensize(4)

def Sunbury_Down_Confirmation():
    pen_Sunbury_Down_Confirmation.penup()
    pen_Sunbury_Down_Confirmation.goto(800, 25)
    pen_Sunbury_Down_Confirmation.pendown()
    pen_Sunbury_Down_Confirmation.goto(-450, 25)
    pen_Sunbury_Down_Confirmation.goto(-800, 375)

    return pen_Sunbury_Down_Confirmation

pen_Sunbury_Down_Confirmation__Useable = Sunbury_Down_Confirmation()
pen_Sunbury_Down_Confirmation__Useable.clear()



# Ballarat Up Confirmation

pen_Ballarat_Up_Confirmation = turtle.Turtle()
pen_Ballarat_Up_Confirmation.speed(0)
pen_Ballarat_Up_Confirmation.hideturtle()
pen_Ballarat_Up_Confirmation.color("#00FF00")
pen_Ballarat_Up_Confirmation.pensize(4)

def Ballarat_Up_Confirmation():
    pen_Ballarat_Up_Confirmation.penup()
    pen_Ballarat_Up_Confirmation.goto(800, -25)
    pen_Ballarat_Up_Confirmation.pendown()
    pen_Ballarat_Up_Confirmation.goto(-800, -25)

    return pen_Ballarat_Up_Confirmation

pen_Ballarat_Up_Confirmation__Useable = Ballarat_Up_Confirmation()
pen_Ballarat_Up_Confirmation__Useable.clear()



# Ballarat Down Confirmation

pen_Ballarat_Down_Confirmation = turtle.Turtle()
pen_Ballarat_Down_Confirmation.speed(0)
pen_Ballarat_Down_Confirmation.hideturtle()
pen_Ballarat_Down_Confirmation.color("#00FF00")
pen_Ballarat_Down_Confirmation.pensize(4)

def Ballarat_Down_Confirmation():
    pen_Ballarat_Down_Confirmation.penup()
    pen_Ballarat_Down_Confirmation.goto(800, -75)
    pen_Ballarat_Down_Confirmation.pendown()
    pen_Ballarat_Down_Confirmation.goto(-800, -75)

    return pen_Ballarat_Down_Confirmation

pen_Ballarat_Down_Confirmation__Useable = Ballarat_Down_Confirmation()
pen_Ballarat_Down_Confirmation__Useable.clear()



# Bendigo Up Confirmation

pen_Bendigo_Up_Confirmation = turtle.Turtle()
pen_Bendigo_Up_Confirmation.speed(0)
pen_Bendigo_Up_Confirmation.hideturtle()
pen_Bendigo_Up_Confirmation.color("#00FF00")
pen_Bendigo_Up_Confirmation.pensize(4)

def Bendigo_Up_Confirmation():
    pen_Bendigo_Up_Confirmation.penup()
    pen_Bendigo_Up_Confirmation.goto(800, -25)
    pen_Bendigo_Up_Confirmation.pendown()
    pen_Bendigo_Up_Confirmation.goto(-450, -25)
    pen_Bendigo_Up_Confirmation.goto(-575, 100)
    pen_Bendigo_Up_Confirmation.goto(-575, 200)
    pen_Bendigo_Up_Confirmation.goto(-800, 425)

    return pen_Bendigo_Up_Confirmation

pen_Bendigo_Up_Confirmation__Useable = Bendigo_Up_Confirmation()
pen_Bendigo_Up_Confirmation__Useable.clear()



# Bendigo Down Confirmation

pen_Bendigo_Down_Confirmation = turtle.Turtle()
pen_Bendigo_Down_Confirmation.speed(0)
pen_Bendigo_Down_Confirmation.hideturtle()
pen_Bendigo_Down_Confirmation.color("#00FF00")
pen_Bendigo_Down_Confirmation.pensize(4)

def Bendigo_Down_Confirmation():
    pen_Bendigo_Down_Confirmation.penup()
    pen_Bendigo_Down_Confirmation.goto(800, -75)
    pen_Bendigo_Down_Confirmation.pendown()
    pen_Bendigo_Down_Confirmation.goto(-450, -75)
    pen_Bendigo_Down_Confirmation.goto(-625, 100)
    pen_Bendigo_Down_Confirmation.goto(-625, 200)
    pen_Bendigo_Down_Confirmation.goto(-800, 375)
    
    return pen_Bendigo_Down_Confirmation

pen_Bendigo_Down_Confirmation__Useable = Bendigo_Down_Confirmation()
pen_Bendigo_Down_Confirmation__Useable.clear()



# Ballarat Up Freight Confirmation

pen_Ballarat_Up_Freight_Confirmation = turtle.Turtle()
pen_Ballarat_Up_Freight_Confirmation.speed(0)
pen_Ballarat_Up_Freight_Confirmation.hideturtle()
pen_Ballarat_Up_Freight_Confirmation.color("#00FF00")
pen_Ballarat_Up_Freight_Confirmation.pensize(4)

def Ballarat_Up_Freight_Confirmation():
    pen_Ballarat_Up_Freight_Confirmation.penup()
    pen_Ballarat_Up_Freight_Confirmation.goto(-800, -25)
    pen_Ballarat_Up_Freight_Confirmation.pendown()
    pen_Ballarat_Up_Freight_Confirmation.goto(50, -25)
    pen_Ballarat_Up_Freight_Confirmation.goto(150, 75 )
    pen_Ballarat_Up_Freight_Confirmation.goto(250, 75 )
    pen_Ballarat_Up_Freight_Confirmation.goto(300, 125)

    return pen_Ballarat_Up_Freight_Confirmation

pen_Ballarat_Up_Freight_Confirmation__Useable = Ballarat_Up_Freight_Confirmation()
pen_Ballarat_Up_Freight_Confirmation__Useable.clear()



# Ballarat Down Freight Confirmation

pen_Ballarat_Down_Freight_Confirmation = turtle.Turtle()
pen_Ballarat_Down_Freight_Confirmation.speed(0)
pen_Ballarat_Down_Freight_Confirmation.hideturtle()
pen_Ballarat_Down_Freight_Confirmation.color("#00FF00")
pen_Ballarat_Down_Freight_Confirmation.pensize(4)

def Ballarat_Down_Freight_Confirmation():
    pen_Ballarat_Down_Freight_Confirmation.penup()
    pen_Ballarat_Down_Freight_Confirmation.goto(-800, -75)
    pen_Ballarat_Down_Freight_Confirmation.pendown()
    pen_Ballarat_Down_Freight_Confirmation.goto(50, -75)
    pen_Ballarat_Down_Freight_Confirmation.goto(150, 25)
    pen_Ballarat_Down_Freight_Confirmation.goto(250, 25)
    pen_Ballarat_Down_Freight_Confirmation.goto(350, 125)

    return pen_Ballarat_Down_Freight_Confirmation

pen_Ballarat_Down_Freight_Confirmation__Useable = Ballarat_Down_Freight_Confirmation()
pen_Ballarat_Down_Freight_Confirmation__Useable.clear()



# Ballarat Down Freight Confirmation Part 1

pen_Ballarat_Down_Freight_Confirmation_Part_1 = turtle.Turtle()
pen_Ballarat_Down_Freight_Confirmation_Part_1.speed(0)
pen_Ballarat_Down_Freight_Confirmation_Part_1.hideturtle()
pen_Ballarat_Down_Freight_Confirmation_Part_1.color("#00FF00")
pen_Ballarat_Down_Freight_Confirmation_Part_1.pensize(4)

def Ballarat_Down_Freight_Confirmation_Part_1():
    pen_Ballarat_Down_Freight_Confirmation_Part_1.penup()
    pen_Ballarat_Down_Freight_Confirmation_Part_1.goto(-450, -75)
    pen_Ballarat_Down_Freight_Confirmation_Part_1.pendown()
    pen_Ballarat_Down_Freight_Confirmation_Part_1.goto(50, -75)
    pen_Ballarat_Down_Freight_Confirmation_Part_1.goto(150, 25)
    pen_Ballarat_Down_Freight_Confirmation_Part_1.goto(250, 25)
    pen_Ballarat_Down_Freight_Confirmation_Part_1.goto(350, 125)

    return pen_Ballarat_Down_Freight_Confirmation_Part_1

pen_Ballarat_Down_Freight_Confirmation_Part_1__Useable = Ballarat_Down_Freight_Confirmation_Part_1()
pen_Ballarat_Down_Freight_Confirmation_Part_1__Useable.clear()



# Ballarat Down Freight Confirmation Part 2

pen_Ballarat_Down_Freight_Confirmation_Part_2 = turtle.Turtle()
pen_Ballarat_Down_Freight_Confirmation_Part_2.speed(0)
pen_Ballarat_Down_Freight_Confirmation_Part_2.hideturtle()
pen_Ballarat_Down_Freight_Confirmation_Part_2.color("#00FF00")
pen_Ballarat_Down_Freight_Confirmation_Part_2.pensize(4)

def Ballarat_Down_Freight_Confirmation_Part_2():
    pen_Ballarat_Down_Freight_Confirmation_Part_2.penup()
    pen_Ballarat_Down_Freight_Confirmation_Part_2.goto(-800, -75)
    pen_Ballarat_Down_Freight_Confirmation_Part_2.pendown()
    pen_Ballarat_Down_Freight_Confirmation_Part_2.goto(-450, -75)

    return pen_Ballarat_Down_Freight_Confirmation_Part_2

pen_Ballarat_Down_Freight_Confirmation_Part_2__Useable = Ballarat_Down_Freight_Confirmation_Part_2()
pen_Ballarat_Down_Freight_Confirmation_Part_2__Useable.clear()




# Track Refutation [[Red]]










# Sunbury Up Refutation

pen_Sunbury_Up_Refutation = turtle.Turtle()
pen_Sunbury_Up_Refutation.speed(0)
pen_Sunbury_Up_Refutation.hideturtle()
pen_Sunbury_Up_Refutation.color("#FF0000")
pen_Sunbury_Up_Refutation.pensize(4)

def Sunbury_Up_Refutation():
    pen_Sunbury_Up_Refutation.penup()
    pen_Sunbury_Up_Refutation.goto(800, 75)
    pen_Sunbury_Up_Refutation.pendown()
    pen_Sunbury_Up_Refutation.goto(-450, 75)
    pen_Sunbury_Up_Refutation.goto(-800, 425)

    return pen_Sunbury_Up_Refutation

pen_Sunbury_Up_Refutation__Useable = Sunbury_Up_Refutation()
pen_Sunbury_Up_Refutation__Useable.clear()



# Sunbury Down Refutation

pen_Sunbury_Down_Refutation = turtle.Turtle()
pen_Sunbury_Down_Refutation.speed(0)
pen_Sunbury_Down_Refutation.hideturtle()
pen_Sunbury_Down_Refutation.color("#FF0000")
pen_Sunbury_Down_Refutation.pensize(4)

def Sunbury_Down_Refutation():
    pen_Sunbury_Down_Refutation.penup()
    pen_Sunbury_Down_Refutation.goto(800, 25)
    pen_Sunbury_Down_Refutation.pendown()
    pen_Sunbury_Down_Refutation.goto(-450, 25)
    pen_Sunbury_Down_Refutation.goto(-800, 375)

    return pen_Sunbury_Down_Refutation

pen_Sunbury_Down_Refutation__Useable = Sunbury_Down_Refutation()
pen_Sunbury_Down_Refutation__Useable.clear()



# Ballarat Up Refutation

pen_Ballarat_Up_Refutation = turtle.Turtle()
pen_Ballarat_Up_Refutation.speed(0)
pen_Ballarat_Up_Refutation.hideturtle()
pen_Ballarat_Up_Refutation.color("#FF0000")
pen_Ballarat_Up_Refutation.pensize(4)

def Ballarat_Up_Refutation():
    pen_Ballarat_Up_Refutation.penup()
    pen_Ballarat_Up_Refutation.goto(800, -25)
    pen_Ballarat_Up_Refutation.pendown()
    pen_Ballarat_Up_Refutation.goto(-800, -25)

    return pen_Ballarat_Up_Refutation

pen_Ballarat_Up_Refutation__Useable = Ballarat_Up_Refutation()
pen_Ballarat_Up_Refutation__Useable.clear()



# Ballarat Down Refutation

pen_Ballarat_Down_Refutation = turtle.Turtle()
pen_Ballarat_Down_Refutation.speed(0)
pen_Ballarat_Down_Refutation.hideturtle()
pen_Ballarat_Down_Refutation.color("#FF0000")
pen_Ballarat_Down_Refutation.pensize(4)

def Ballarat_Down_Refutation():
    pen_Ballarat_Down_Refutation.penup()
    pen_Ballarat_Down_Refutation.goto(800, -75)
    pen_Ballarat_Down_Refutation.pendown()
    pen_Ballarat_Down_Refutation.goto(-800, -75)

    return pen_Ballarat_Down_Refutation

pen_Ballarat_Down_Refutation__Useable = Ballarat_Down_Refutation()
pen_Ballarat_Down_Refutation__Useable.clear()



# Bendigo Up Refutation

pen_Bendigo_Up_Refutation = turtle.Turtle()
pen_Bendigo_Up_Refutation.speed(0)
pen_Bendigo_Up_Refutation.hideturtle()
pen_Bendigo_Up_Refutation.color("#FF0000")
pen_Bendigo_Up_Refutation.pensize(4)

def Bendigo_Up_Refutation():
    pen_Bendigo_Up_Refutation.penup()
    pen_Bendigo_Up_Refutation.goto(800, -25)
    pen_Bendigo_Up_Refutation.pendown()
    pen_Bendigo_Up_Refutation.goto(-450, -25)
    pen_Bendigo_Up_Refutation.goto(-575, 100)
    pen_Bendigo_Up_Refutation.goto(-575, 200)
    pen_Bendigo_Up_Refutation.goto(-800, 425)

    return pen_Bendigo_Up_Refutation

pen_Bendigo_Up_Refutation__Useable = Bendigo_Up_Refutation()
pen_Bendigo_Up_Refutation__Useable.clear()



# Bendigo Down Refutation

pen_Bendigo_Down_Refutation = turtle.Turtle()
pen_Bendigo_Down_Refutation.speed(0)
pen_Bendigo_Down_Refutation.hideturtle()
pen_Bendigo_Down_Refutation.color("#FF0000")
pen_Bendigo_Down_Refutation.pensize(4)

def Bendigo_Down_Refutation():
    pen_Bendigo_Down_Refutation.penup()
    pen_Bendigo_Down_Refutation.goto(800, -75)
    pen_Bendigo_Down_Refutation.pendown()
    pen_Bendigo_Down_Refutation.goto(-450, -75)
    pen_Bendigo_Down_Refutation.goto(-625, 100)
    pen_Bendigo_Down_Refutation.goto(-625, 200)
    pen_Bendigo_Down_Refutation.goto(-800, 375)
    
    return pen_Bendigo_Down_Refutation

pen_Bendigo_Down_Refutation__Useable = Bendigo_Down_Refutation()
pen_Bendigo_Down_Refutation__Useable.clear()



# Ballarat Up Freight Refutation

pen_Ballarat_Up_Freight_Refutation = turtle.Turtle()
pen_Ballarat_Up_Freight_Refutation.speed(0)
pen_Ballarat_Up_Freight_Refutation.hideturtle()
pen_Ballarat_Up_Freight_Refutation.color("#FF0000")
pen_Ballarat_Up_Freight_Refutation.pensize(4)

def Ballarat_Up_Freight_Refutation():
    pen_Ballarat_Up_Freight_Refutation.penup()
    pen_Ballarat_Up_Freight_Refutation.goto(-800, -25)
    pen_Ballarat_Up_Freight_Refutation.pendown()
    pen_Ballarat_Up_Freight_Refutation.goto(50, -25)
    pen_Ballarat_Up_Freight_Refutation.goto(150, 75 )
    pen_Ballarat_Up_Freight_Refutation.goto(250, 75 )
    pen_Ballarat_Up_Freight_Refutation.goto(300, 125)

    return pen_Ballarat_Up_Freight_Refutation

pen_Ballarat_Up_Freight_Refutation__Useable = Ballarat_Up_Freight_Refutation()
pen_Ballarat_Up_Freight_Refutation__Useable.clear()



# Ballarat Down Freight Refutation Part 1

pen_Ballarat_Down_Freight_Refutation_Part_1 = turtle.Turtle()
pen_Ballarat_Down_Freight_Refutation_Part_1.speed(0)
pen_Ballarat_Down_Freight_Refutation_Part_1.hideturtle()
pen_Ballarat_Down_Freight_Refutation_Part_1.color("#FF0000")
pen_Ballarat_Down_Freight_Refutation_Part_1.pensize(4)

def Ballarat_Down_Freight_Refutation_Part_1():
    pen_Ballarat_Down_Freight_Refutation_Part_1.penup()
    pen_Ballarat_Down_Freight_Refutation_Part_1.goto(-450, -75)
    pen_Ballarat_Down_Freight_Refutation_Part_1.pendown()
    pen_Ballarat_Down_Freight_Refutation_Part_1.goto(50, -75)
    pen_Ballarat_Down_Freight_Refutation_Part_1.goto(150, 25)
    pen_Ballarat_Down_Freight_Refutation_Part_1.goto(250, 25)
    pen_Ballarat_Down_Freight_Refutation_Part_1.goto(350, 125)

    return pen_Ballarat_Down_Freight_Refutation_Part_1

pen_Ballarat_Down_Freight_Refutation_Part_1__Useable = Ballarat_Down_Freight_Refutation_Part_1()
pen_Ballarat_Down_Freight_Refutation_Part_1__Useable.clear()



# Ballarat Down Freight Refutation Part 2

pen_Ballarat_Down_Freight_Refutation_Part_2 = turtle.Turtle()
pen_Ballarat_Down_Freight_Refutation_Part_2.speed(0)
pen_Ballarat_Down_Freight_Refutation_Part_2.hideturtle()
pen_Ballarat_Down_Freight_Refutation_Part_2.color("#FF0000")
pen_Ballarat_Down_Freight_Refutation_Part_2.pensize(4)

def Ballarat_Down_Freight_Refutation_Part_2():
    pen_Ballarat_Down_Freight_Refutation_Part_2.penup()
    pen_Ballarat_Down_Freight_Refutation_Part_2.goto(-800, -75)
    pen_Ballarat_Down_Freight_Refutation_Part_2.pendown()
    pen_Ballarat_Down_Freight_Refutation_Part_2.goto(-450, -75)

    return pen_Ballarat_Down_Freight_Refutation_Part_2

pen_Ballarat_Down_Freight_Refutation_Part_2__Useable = Ballarat_Down_Freight_Refutation_Part_2()
pen_Ballarat_Down_Freight_Refutation_Part_2__Useable.clear()



S11R = 0
S12R = 0
S21R = 0
S22R = 0
S31R = 0
S32R = 0
S41R = 0
S42R = 0
S51R = 0

# S1_Counter

S1_Counter = 0

def Increase_S1_Counter():
    global S1_Counter
    S1_Counter = (S1_Counter + 1) % 3
    if S1_Counter == 0:
        pen_Signal_Green_11__Useable.clear()
        pen_Signal_Green_12__Useable.clear()
        pen_Signal_Red_11__Useable.clear()
        pen_Signal_Red_12__Useable.clear()
        Bendigo_Up_Refutation()
        Sunbury_Up_Confirmation()
        Signal_Green_11_Sunbury_Up()
        Signal_Green_12_Sunbury_Up()
        screen.update()
        time.sleep(1)
        pen_Bendigo_Up_Refutation__Useable.clear()
        pen_Sunbury_Up_Confirmation__Useable.clear()

    if S1_Counter == 1:
        pen_Signal_Green_11__Useable.clear()
        pen_Signal_Green_12__Useable.clear()
        pen_Signal_Red_32__Useable.clear()
        Sunbury_Up_Refutation()
        Bendigo_Up_Confirmation()
        Signal_Green_11_Sunbury_Up()
        Signal_Red_12_Sunbury_Up()
        Signal_Green_32_Ballarat_Bendigo_Up()
        screen.update()
        time.sleep(1)
        pen_Sunbury_Up_Refutation__Useable.clear()
        pen_Bendigo_Up_Confirmation.clear()

    if S1_Counter == 2:
        pen_Signal_Green_11__Useable.clear()
        pen_Signal_Red_12__Useable.clear()
        Sunbury_Up_Refutation()
        Bendigo_Up_Refutation()
        Signal_Red_11_Sunbury_Up()
        Signal_Red_12_Sunbury_Up()
        screen.update()
        time.sleep(1)
        pen_Sunbury_Up_Refutation__Useable.clear()
        pen_Bendigo_Up_Refutation__Useable.clear()

screen.listen()
screen.onkey(Increase_S1_Counter, "a")



# S2_Counter

S2_Counter = 0

def Increase_S2_Counter():
    global S2_Counter
    S2_Counter = (S2_Counter + 1) % 3
    if S2_Counter == 0:
        pen_Signal_Red_51__Useable.clear()
        pen_Signal_Green_21__Useable.clear()
        pen_Signal_Green_22__Useable.clear()
        pen_Signal_Red_21__Useable.clear()
        pen_Signal_Red_22__Useable.clear()
        Ballarat_Down_Freight_Refutation_Part_1()
        Ballarat_Down_Freight_Refutation_Part_2()
        Sunbury_Down_Confirmation()
        Signal_Green_21_Sunbury_Down()
        Signal_Green_22_Sunbury_Down()
        Signal_Red_51_Freight_Down()
        screen.update()
        time.sleep(1)
        pen_Ballarat_Down_Freight_Refutation_Part_1__Useable.clear()
        pen_Ballarat_Down_Freight_Refutation_Part_2__Useable.clear()
        pen_Sunbury_Down_Confirmation__Useable.clear()
    
    if S2_Counter == 1:
        pen_Signal_Green_51__Useable.clear()
        pen_Signal_Green_21__Useable.clear()
        pen_Signal_Green_42__Useable.clear()
        pen_Signal_Red_51__Useable.clear()
        pen_Signal_Red_21__Useable.clear()
        pen_Signal_Red_42__Useable.clear()
        Sunbury_Down_Refutation()
        Ballarat_Down_Freight_Confirmation_Part_1()
        Ballarat_Down_Freight_Confirmation_Part_2()
        Signal_Green_51_Freight_Down()
        Signal_Red_21_Sunbury_Down()
        Signal_Green_42_Ballarat_Bendigo_Down()
        Signal_Red_22_Sunbury_Down()
        screen.update()
        time.sleep(1)
        pen_Sunbury_Down_Refutation__Useable.clear()
        pen_Ballarat_Down_Freight_Confirmation_Part_1__Useable.clear()
        pen_Ballarat_Down_Freight_Confirmation_Part_2__Useable.clear()

    if S2_Counter == 2:
        pen_Signal_Red_42__Useable.clear()
        pen_Signal_Green_51__Useable.clear()
        pen_Signal_Green_21__Useable.clear()
        pen_Signal_Green_22__Useable.clear()
        pen_Signal_Red_51__Useable.clear()
        pen_Signal_Red_21__Useable.clear()
        pen_Signal_Red_22__Useable.clear()
        Sunbury_Down_Refutation()
        Ballarat_Down_Freight_Refutation_Part_1()
        Ballarat_Down_Freight_Refutation_Part_2()
        Signal_Red_51_Freight_Down()
        Signal_Red_21_Sunbury_Down()
        Signal_Red_22_Sunbury_Down()
        screen.update()
        time.sleep(1)
        pen_Sunbury_Down_Refutation__Useable.clear()
        pen_Ballarat_Down_Freight_Refutation_Part_1__Useable.clear()
        pen_Ballarat_Down_Freight_Refutation_Part_2__Useable.clear()

screen.listen()
screen.onkey(Increase_S2_Counter, "s")



# S3_Counter

S3_Counter = 0

def Increase_S3_Counter():
    global S3_Counter
    S3_Counter = (S3_Counter + 1) % 3
    if S3_Counter == 0:
        pen_Signal_Green_31__Useable.clear()
        pen_Signal_Green_32__Useable.clear()
        pen_Signal_Red_31__Useable.clear()
        pen_Signal_Red_32__Useable.clear()
        Ballarat_Up_Freight_Refutation()
        Ballarat_Up_Confirmation()
        Signal_Green_31_Ballarat_Up()
        Signal_Green_32_Ballarat_Bendigo_Up()
        screen.update()
        time.sleep(1)
        pen_Ballarat_Up_Freight_Refutation__Useable.clear()
        pen_Ballarat_Up_Confirmation__Useable.clear()

    if S3_Counter == 1:
        pen_Signal_Green_31__Useable.clear()
        pen_Signal_Green_32__Useable.clear()
        pen_Signal_Red_31__Useable.clear()
        pen_Signal_Red_32__Useable.clear()
        Ballarat_Up_Refutation()
        Ballarat_Up_Freight_Confirmation()
        Signal_Green_31_Ballarat_Up()
        Signal_Green_32_Ballarat_Bendigo_Up()
        screen.update()
        time.sleep(1)
        pen_Ballarat_Up_Refutation__Useable.clear()
        pen_Ballarat_Up_Freight_Confirmation__Useable.clear()

    if S3_Counter == 2:
        pen_Signal_Green_31__Useable.clear()
        pen_Signal_Green_32__Useable.clear()
        pen_Signal_Red_31__Useable.clear()
        pen_Signal_Red_32__Useable.clear()
        Ballarat_Up_Refutation()
        Ballarat_Up_Freight_Refutation()
        Signal_Red_31_Ballarat_Up()
        Signal_Red_32_Ballarat_Bendigo_Up()
        screen.update()
        time.sleep(1)
        pen_Ballarat_Up_Refutation__Useable.clear()
        pen_Ballarat_Up_Freight_Refutation__Useable.clear()

screen.listen()
screen.onkey(Increase_S3_Counter, "d")



# S4_Counter

S4_Counter = 0

def Increase_S4_Counter():
    global S4_Counter
    S4_Counter = (S4_Counter + 1) % 3
    if S4_Counter == 0:
        pen_Signal_Green_41__Useable.clear()
        pen_Signal_Green_42__Useable.clear()
        pen_Signal_Red_41__Useable.clear()
        pen_Signal_Red_42__Useable.clear()
        Bendigo_Down_Refutation()
        Ballarat_Down_Confirmation()
        Signal_Green_41_Ballarat_Bendigo_Down()
        Signal_Green_42_Ballarat_Bendigo_Down()
        screen.update()
        time.sleep(1)
        pen_Bendigo_Down_Refutation__Useable.clear()
        pen_Ballarat_Down_Confirmation__Useable.clear()

    if S4_Counter == 1:
        pen_Signal_Green_41__Useable.clear()
        pen_Signal_Green_42__Useable.clear()
        pen_Signal_Red_41__Useable.clear()
        pen_Signal_Red_42__Useable.clear()
        Ballarat_Down_Refutation()
        Bendigo_Down_Confirmation()
        Signal_Green_41_Ballarat_Bendigo_Down()
        Signal_Green_42_Ballarat_Bendigo_Down()
        screen.update()
        time.sleep(1)
        pen_Ballarat_Down_Refutation__Useable.clear()
        pen_Bendigo_Down_Confirmation__Useable.clear()

    if S4_Counter == 2:
        pen_Signal_Green_41__Useable.clear()
        pen_Signal_Green_42__Useable.clear()
        pen_Signal_Red_41__Useable.clear()
        pen_Signal_Red_42__Useable.clear()
        Ballarat_Down_Refutation()
        Bendigo_Down_Refutation()
        Signal_Red_41_Ballarat_Bendigo_Down()
        Signal_Red_42_Ballarat_Bendigo_Down()
        screen.update()
        time.sleep(1)
        pen_Ballarat_Down_Refutation__Useable.clear()
        pen_Bendigo_Down_Refutation__Useable.clear()


screen.listen()
screen.onkey(Increase_S4_Counter, "f")






# Difficulty Counter
l = 1
def Increase_Difficulty_Counter():
    global l
    if l < 20:
        l = l + 1
    else:
        l = l + 0
    print(l)

def Decrease_Difficulty_Counter():
    global l
    if l > 1:
        l = l - 1
    else:
        l = l + 0
    print(l)

screen.listen()
screen.onkey(Increase_Difficulty_Counter, "g")
screen.onkey(Decrease_Difficulty_Counter, "h")



# Progression = False

# Latch = 0

# def Space_Bar_Action():
#     global Progression, Latch
#     if Latch == 0:
#         Progression = True
#         Latch = Latch + 1
#     else:
#         Progression = True
#         Latch = Latch + 1

# screen.listen()
# screen.onkey(Space_Bar_Action, "space")




pen_Instructions = turtle.Turtle()
pen_Instructions.speed(0)
pen_Instructions.hideturtle()
pen_Instructions.pensize(2)
pen_Instructions.color("white")

def Instructions():

    pen_Instructions.penup()
    pen_Instructions.goto(0, 25)
    pen_Instructions.pendown()
    pen_Instructions.write("Action Keys Are A S D F", align = "Center", font = ("Helvetica Neue", 24, "normal"))
    pen_Instructions.penup()
    pen_Instructions.goto(0, -25)
    pen_Instructions.pendown()
    pen_Instructions.write("Press SPACE To Start", align  = "Center", font = ("Helvetica Neue", 24, "normal"))

    return pen_Instructions

pen_Instructions__Useable = Instructions()
pen_Instructions__Useable.clear()







def Fail_State_Screen():

    # 
    
    pen_Sunbury_Up_Train__Useable.clear()
    pen_Sunbury_Down_Train__Useable.clear()
    pen_Ballarat_Up_Train__Useable.clear()
    pen_Ballarat_Down_Train__Useable.clear()
    pen_Bendigo_Up_Train__Useable.clear()
    pen_Bendigo_Down_Train__Useable.clear()
    pen_Ballarat_Up_Freight_Train__Useable.clear()
    pen_Ballarat_Up_Freight_Train__Useable.clear()

    pen_Definition_Of_Sunbury_Up__Useable.clear()
    pen_Definition_Of_Sunbury_Down__Useable.clear()
    pen_Definition_Of_Ballarat_Up__Useable.clear()
    pen_Definition_Of_Ballarat_Down__Useable.clear()
    pen_Definition_Of_Bendigo_Up__Useable.clear()
    pen_Definition_Of_Bendigo_Down__Useable.clear()
    pen_Definition_Of_Ballarat_Up_Freight__Useable.clear()
    pen_Definition_Of_Ballarat_Down_Freight__Useable.clear()

    pen_Sunbury_Up_Refutation__Useable.clear()
    pen_Sunbury_Down_Refutation__Useable.clear()
    pen_Ballarat_Up_Refutation__Useable.clear()
    pen_Ballarat_Down_Refutation__Useable.clear()
    pen_Bendigo_Up_Refutation__Useable.clear()
    pen_Bendigo_Down_Refutation__Useable.clear()
    pen_Ballarat_Up_Freight_Refutation__Useable.clear()
    pen_Ballarat_Down_Freight_Refutation_Part_1__Useable.clear()
    pen_Ballarat_Down_Freight_Refutation_Part_2__Useable.clear()

    pen_Sunbury_Up_Confirmation__Useable.clear()
    pen_Sunbury_Down_Confirmation__Useable.clear()
    pen_Ballarat_Up_Confirmation__Useable.clear()
    pen_Ballarat_Down_Confirmation__Useable.clear()
    pen_Bendigo_Up_Confirmation__Useable.clear()
    pen_Bendigo_Down_Confirmation__Useable.clear()
    pen_Ballarat_Up_Freight_Confirmation__Useable.clear()
    pen_Ballarat_Down_Freight_Confirmation_Part_1__Useable.clear()
    pen_Ballarat_Down_Freight_Confirmation_Part_2__Useable.clear()

    pen_Signal_Red_11__Useable.clear()
    pen_Signal_Red_12__Useable.clear()
    pen_Signal_Red_21__Useable.clear()
    pen_Signal_Red_22__Useable.clear()
    pen_Signal_Red_31__Useable.clear()
    pen_Signal_Red_32__Useable.clear()
    pen_Signal_Red_41__Useable.clear()
    pen_Signal_Red_42__Useable.clear()
    pen_Signal_Red_51__Useable.clear()

    pen_Signal_Green_11__Useable.clear()
    pen_Signal_Green_12__Useable.clear()
    pen_Signal_Green_21__Useable.clear()
    pen_Signal_Green_22__Useable.clear()
    pen_Signal_Green_31__Useable.clear()
    pen_Signal_Green_32__Useable.clear()
    pen_Signal_Green_41__Useable.clear()
    pen_Signal_Green_42__Useable.clear()
    pen_Signal_Green_51__Useable.clear()

    pen_main.penup()
    pen_main.goto(0, 25)
    pen_main.pendown()
    pen_main.write("Game Over", align = "Center", font = ("Helvetica Neue", 24, "normal"))
    pen_main.penup()
    pen_main.goto(0, -25)
    pen_main.pendown()
    pen_main.write("Press ENTER To Quit", align  = "Center", font = ("Helvetica Neue", 24, "normal"))















# Success Conditions [Tainted Success(Not Protected)]

# 0 = Forward  1 = Diversion  2 = No Go [[3 = Forward but No Go, only for S4]]

# Sunbury_Up_Train:

# S1 Counter == 0
# S2 Counter == 1'
# S3 Counter == 1'
# S4 Counter == Anything


# Sunbury_Down_Train:

# S1 Counter == 1'
# S2 Counter == 0
# S3 Counter == 1'
# S4 Counter == 1'


# Ballarat_Up_Train:

# S1 Counter == 1'
# S2 Counter == 1'
# S3 Counter == 0
# S4 Counter == 1'


# Ballarat_Down_Train

# S1 Counter == Anything
# S2 Counter == 1'
# S3 Counter == Anything
# S4 Counter == 0


# Bendigo_Up_Train

# S1 Counter == 1
# S2 Counter == 1'
# S3 Counter == 0
# S4 Counter == Anything


# Bendigo_Down_Train

# S1 Counter == Anything
# S2 Counter == 2
# S3 Counter == 2
# S4 Counter == 1


# Ballarat_Up_Freight_Train

# S1 Counter = 2
# S2 Counter = 0'
# S3 Counter = 1
# S4 Counter = 1'


# Ballarat_Down_Freight_Train

# S1 Counter = 0'
# S2 Counter = 1
# S3 Counter = 0'
# S4 Counter = 2
# Always check if it is 2, for the Ballarat train it doesnt matter, but we say it 


# The Score
Score = 0

pen_Score = turtle.Turtle()
pen_Score.hideturtle()
pen_Score.color("white")
pen_Score.pensize(1)
pen_Score.speed(0)

def Score_Number():
    pen_Score.penup()
    pen_Score.goto(700, -300)
    pen_Score.pendown()
    pen_Score.write(f"Score: {Score}", align = "right", font = ("Helvetica Neue", "10", "normal"))

    return pen_Score
pen_Score__Useable =  Score_Number()
pen_Score__Useable.clear()





# |||| The actual game Generator




# Limit
i = 0 

# Hyperbolic Decreasing Time Unit
j = 0

# Scaling Factor of J in for the i axis
k = 10

# Switch [Turn this on for certain things like delays]
l = 1

def Generator_Main():    
    global i, j, Score, l
    j = 0.3 + ((5.7 * k) / (i + k))
    i = i + 1
    Score = Score + 1

    global Generator_Outcome
    Generator_Outcome = random.randint(0, 7)



#   Sunbury Up Generation

    if Generator_Outcome == 0:

        Definition_Of_Sunbury_Up()
        screen.update()
        time.sleep((j/6)*l)
        pen_Definition_Of_Sunbury_Up__Useable.clear()
        screen.update()
        time.sleep((j/6)*l)

        Definition_Of_Sunbury_Up()
        screen.update()
        time.sleep((j/6)*l)
        pen_Definition_Of_Sunbury_Up__Useable.clear()
        screen.update()
        time.sleep((j/6)*l)

        Definition_Of_Sunbury_Up()
        screen.update()
        time.sleep((j/6)*l)
        pen_Definition_Of_Sunbury_Up__Useable.clear()
        screen.update()
        time.sleep((j/6)*l)
        screen.update()
        screen.listen()
        time.sleep((j/6)*(l-1))
        screen.update()
        screen.listen()

        if S1_Counter == 0 and S2_Counter != 1 and S3_Counter != 1:
            Sunbury_Up_Train()
            Score_Number()
            screen.update()
            if j >= (1*l):
                time.sleep((j*l) / 2)
            else:
                time.sleep(1*l)
            pen_Sunbury_Up_Train__Useable.clear()
            pen_Score__Useable.clear()
            
            Generator_Main()

        else:
            Fail_State_Screen()
            Score_Number()



#   Sunbury_Down_Generation

    if Generator_Outcome == 1:
            
        Definition_Of_Sunbury_Down()
        screen.update()
        time.sleep((j/6)*l)
        pen_Definition_Of_Sunbury_Down__Useable.clear()
        screen.update()
        time.sleep((j/6)*l)
    
        Definition_Of_Sunbury_Down()
        screen.update()
        time.sleep((j/6)*l)
        pen_Definition_Of_Sunbury_Down__Useable.clear()
        screen.update()
        time.sleep((j/6)*l)
        
        Definition_Of_Sunbury_Down()
        screen.update()
        time.sleep((j/6)*l)
        pen_Definition_Of_Sunbury_Down__Useable.clear()
        screen.update()
        time.sleep((j/6)*l)
        screen.update()
        screen.listen()
        time.sleep((j/6)*(l-1))
        screen.update()
        screen.listen()
        
        if S2_Counter == 0 and S3_Counter != 1:
            Sunbury_Down_Train()
            Score_Number()
            screen.update()
            if j >= (1*l):
                time.sleep((j*l) / 2)
            else:
                time.sleep(1*l)
            pen_Sunbury_Down_Train__Useable.clear()
            pen_Score__Useable.clear()
            
            Generator_Main()
    
        else:
            Fail_State_Screen()
            Score_Number()



#   Ballarat Up Generation

    if Generator_Outcome == 2:
            
        Definition_Of_Ballarat_Up()
        screen.update()
        time.sleep((j/6)*l)
        pen_Definition_Of_Ballarat_Up__Useable.clear()
        screen.update()
        time.sleep((j/6)*l)
    
        Definition_Of_Ballarat_Up()
        screen.update()
        time.sleep((j/6)*l)
        pen_Definition_Of_Ballarat_Up__Useable.clear()
        screen.update()
        time.sleep((j/6)*l)

        Definition_Of_Ballarat_Up()
        screen.update()
        time.sleep((j/6)*l)
        pen_Definition_Of_Ballarat_Up__Useable.clear()
        screen.update()
        time.sleep((j/6)*l)
        screen.update()
        screen.listen()
        time.sleep((j/6)*(l-1))
        screen.update()
        screen.listen()

        if S2_Counter != 1 and S3_Counter == 0:
            Ballarat_Up_Train()
            Score_Number()
            screen.update()
            if j >= (1*l):
                time.sleep((j*l) / 2)
            else:
                time.sleep(1*l)
            pen_Ballarat_Up_Train__Useable.clear()
            pen_Score__Useable.clear()
            
            Generator_Main()
    
        else:
            Fail_State_Screen()
            Score_Number()



#   Ballarat Down Generation

    if Generator_Outcome == 3:
            
        Definition_Of_Ballarat_Down()
        screen.update()
        time.sleep((j/6)*l)
        pen_Definition_Of_Ballarat_Down__Useable.clear()
        screen.update()
        time.sleep((j/6)*l)
    
        Definition_Of_Ballarat_Down()
        screen.update()
        time.sleep((j/6)*l)
        pen_Definition_Of_Ballarat_Down__Useable.clear()
        screen.update()
        time.sleep((j/6)*l)

        Definition_Of_Ballarat_Down()
        screen.update()
        time.sleep((j/6)*l)
        pen_Definition_Of_Ballarat_Down__Useable.clear()
        screen.update()
        time.sleep((j/6)*l)
        screen.update()
        screen.listen()
        time.sleep((j/6)*(l-1))
        screen.update()
        screen.listen()

        if S4_Counter == 0:
            Ballarat_Down_Train()
            Score_Number()
            screen.update()
            if j >= (1*l):
                time.sleep((j*l) / 2)
            else:
                time.sleep(1*l)
            pen_Ballarat_Down_Train__Useable.clear()
            pen_Score__Useable.clear()
            
            Generator_Main()
    
        else:
            Fail_State_Screen()
            Score_Number()



#   Bendigo Up Generation

    if Generator_Outcome == 4:
            
        Definition_Of_Bendigo_Up()
        screen.update()
        time.sleep((j/6)*l)
        pen_Definition_Of_Bendigo_Up__Useable.clear()
        screen.update()
        time.sleep((j/6)*l)
    
        Definition_Of_Bendigo_Up()
        screen.update()
        time.sleep((j/6)*l)
        pen_Definition_Of_Bendigo_Up__Useable.clear()
        screen.update()
        time.sleep((j/6)*l)

        Definition_Of_Bendigo_Up()
        screen.update()
        time.sleep((j/6)*l)
        pen_Definition_Of_Bendigo_Up__Useable.clear()
        screen.update()
        time.sleep((j/6)*l)
        screen.update()
        screen.listen()
        time.sleep((j/6)*(l-1))
        screen.update()
        screen.listen()

        if S1_Counter == 1 and S2_Counter != 1 and S3_Counter == 0:
            Bendigo_Up_Train()
            Score_Number()
            screen.update()
            if j >= (1*l):
                time.sleep((j*l) / 2)
            else:
                time.sleep(1*l)
            pen_Bendigo_Up_Train__Useable.clear()
            pen_Score__Useable.clear()
            
            Generator_Main()
    
        else:
            Fail_State_Screen()
            Score_Number()



#   Bendigo Down Generation

    if Generator_Outcome == 5:
            
        Definition_Of_Bendigo_Down()
        screen.update()
        time.sleep((j/6)*l)
        pen_Definition_Of_Bendigo_Down__Useable.clear()
        screen.update()
        time.sleep((j/6)*l)
    
        Definition_Of_Bendigo_Down()
        screen.update()
        time.sleep((j/6)*l)
        pen_Definition_Of_Bendigo_Down__Useable.clear()
        screen.update()
        time.sleep((j/6)*l)

        Definition_Of_Bendigo_Down()
        screen.update()
        time.sleep((j/6)*l)
        pen_Definition_Of_Bendigo_Down__Useable.clear()
        screen.update()
        time.sleep((j/6)*l)
        screen.update()
        screen.listen()
        time.sleep((j/6)*(l-1))
        screen.update()
        screen.listen()

        if S4_Counter == 1:
            Bendigo_Down_Train()
            Score_Number()
            screen.update()
            if j >= (1*l):
                time.sleep((j*l) / 2)
            else:
                time.sleep(1*l)
            pen_Bendigo_Down_Train__Useable.clear()
            pen_Score__Useable.clear()
            
            Generator_Main()
    
        else:
            Fail_State_Screen()
            Score_Number()



#   Ballarat Up Freight Generation

    if Generator_Outcome == 6:
            
        Definition_Of_Ballarat_Up_Freight()
        screen.update()
        time.sleep((j/6)*l)
        pen_Definition_Of_Ballarat_Up_Freight__Useable.clear()
        screen.update()
        time.sleep((j/6)*l)
    
        Definition_Of_Ballarat_Up_Freight()
        screen.update()
        time.sleep((j/6)*l)
        pen_Definition_Of_Ballarat_Up_Freight__Useable.clear()
        screen.update()
        time.sleep((j/6)*l)

        Definition_Of_Ballarat_Up_Freight()
        screen.update()
        time.sleep((j/6)*l)
        pen_Definition_Of_Ballarat_Up_Freight__Useable.clear()
        screen.update()
        time.sleep((j/6)*l)
        screen.update()
        screen.listen()
        time.sleep((j/6)*(l-1))
        screen.update()
        screen.listen()

        if S1_Counter != 2 and S3_Counter == 1:
            Ballarat_Up_Freight_Train()
            Score_Number()
            screen.update()
            if j >= (1*l):
                time.sleep((j*l) / 2)
            else:
                time.sleep(1*l)
            pen_Ballarat_Up_Freight_Train__Useable.clear()
            pen_Score__Useable.clear()
            
            Generator_Main()
    
        else:
            Fail_State_Screen()
            Score_Number()



#   Ballarat Down Freight Generation

    if Generator_Outcome == 7:
            
        Definition_Of_Ballarat_Down_Freight()
        screen.update()
        time.sleep((j/6)*l)
        pen_Definition_Of_Ballarat_Down_Freight__Useable.clear()
        screen.update()
        time.sleep((j/6)*l)
    
        Definition_Of_Ballarat_Down_Freight()
        screen.update()
        time.sleep((j/6)*l)
        pen_Definition_Of_Ballarat_Down_Freight__Useable.clear()
        screen.update()
        time.sleep((j/6)*l)

        Definition_Of_Ballarat_Down_Freight()
        screen.update()
        time.sleep((j/6)*l)
        pen_Definition_Of_Ballarat_Down_Freight__Useable.clear()
        screen.update()
        time.sleep((j/6)*l)
        screen.update()
        screen.listen()
        time.sleep((j/6)*(l-1))
        screen.update()
        screen.listen()

        if S2_Counter == 1 and S4_Counter == 0:
            Ballarat_Down_Freight_Train()
            Score_Number()
            screen.update()
            if j >= (1*l):
                time.sleep((j*l) / 2)
            else:
                time.sleep(1*l)
            pen_Ballarat_Down_Freight_Train__Useable.clear()
            pen_Score__Useable.clear()
            
            Generator_Main()
    
        else:
            Fail_State_Screen()
            Score_Number()




def Check_Game_State():
    global Progression
    if Progression == True:
        pen_Instructions__Useable.clear()
        Generator_Main()
    else:
        screen.ontimer(Check_Game_State, 50)




Progression = False
Latch = 0

def Space_Bar_Action():
    global Progression, Latch
    
    
    if Latch == 0:
        Progression = True
        Latch = Latch + 1
        
        
        pen_Instructions__Useable.clear()

        Signal_Red_11_Sunbury_Up()
        Signal_Red_12_Sunbury_Up()
        Signal_Red_21_Sunbury_Down()
        Signal_Red_22_Sunbury_Down()
        Signal_Red_31_Ballarat_Up()
        Signal_Red_32_Ballarat_Bendigo_Up()
        Signal_Red_41_Ballarat_Bendigo_Down()
        Signal_Red_42_Ballarat_Bendigo_Down()
        Signal_Red_51_Freight_Down()
        
        
        Generator_Main()

screen.listen()
screen.onkey(Space_Bar_Action, "space")




# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------




# The Actual Code That Fires:









#||Game [Test & Start Up Screen]||#

screen.update()
time.sleep(2)

Sunbury_Up_Train()
screen.update()
time.sleep(0.15)
Sunbury_Down_Train()
screen.update()
time.sleep(0.15)
Ballarat_Up_Train()
screen.update()
time.sleep(0.15)
Ballarat_Down_Train()
screen.update()
time.sleep(0.15)
Bendigo_Up_Train()
screen.update()
time.sleep(0.15)
Bendigo_Down_Train()
screen.update()
time.sleep(0.15)
Ballarat_Up_Freight_Train()
screen.update()
time.sleep(0.15)
Ballarat_Down_Freight_Train()
screen.update()
time.sleep(0.15)
# Bendigo_Up_Freight_Train()
# Bendigo_Down_Freight_Train()
# Jacana_Loop_Up_Freight_Train()
# Jacana_Loop_Down_Freight_Train()

Signal_Red_11_Sunbury_Up()
screen.update()
time.sleep(0.05)
Signal_Red_12_Sunbury_Up()
screen.update()
time.sleep(0.05)
Signal_Red_21_Sunbury_Down()
screen.update()
time.sleep(0.05)
Signal_Red_22_Sunbury_Down()
screen.update()
time.sleep(0.05)
Signal_Red_31_Ballarat_Up()
screen.update()
time.sleep(0.05)
Signal_Red_32_Ballarat_Bendigo_Up()
screen.update()
time.sleep(0.05)
Signal_Red_41_Ballarat_Bendigo_Down()
screen.update()
time.sleep(0.05)
Signal_Red_42_Ballarat_Bendigo_Down()
screen.update()
time.sleep(0.05)
Signal_Red_51_Freight_Down()

screen.update()
time.sleep(1)

pen_Signal_Red_11__Useable.clear()
pen_Signal_Red_12__Useable.clear()
pen_Signal_Red_21__Useable.clear()
pen_Signal_Red_22__Useable.clear()
pen_Signal_Red_31__Useable.clear()
pen_Signal_Red_32__Useable.clear()
pen_Signal_Red_41__Useable.clear()
pen_Signal_Red_42__Useable.clear()
pen_Signal_Red_51__Useable.clear()

screen.update()
time.sleep(1)

Signal_Green_11_Sunbury_Up()
screen.update()
time.sleep(0.05)
Signal_Green_12_Sunbury_Up()
screen.update()
time.sleep(0.05)
Signal_Green_21_Sunbury_Down()
screen.update()
time.sleep(0.05)
Signal_Green_22_Sunbury_Down()
screen.update()
time.sleep(0.05)
Signal_Green_31_Ballarat_Up()
screen.update()
time.sleep(0.05)
Signal_Green_32_Ballarat_Bendigo_Up()
screen.update()
time.sleep(0.05)
Signal_Green_41_Ballarat_Bendigo_Down()
screen.update()
time.sleep(0.05)
Signal_Green_42_Ballarat_Bendigo_Down()
screen.update()
time.sleep(0.05)
Signal_Green_51_Freight_Down()

screen.update()
time.sleep(2)

pen_Signal_Green_11__Useable.clear()
pen_Signal_Green_12__Useable.clear()
pen_Signal_Green_21__Useable.clear()
pen_Signal_Green_22__Useable.clear()
pen_Signal_Green_31__Useable.clear()
pen_Signal_Green_32__Useable.clear()
pen_Signal_Green_41__Useable.clear()
pen_Signal_Green_42__Useable.clear()
pen_Signal_Green_51__Useable.clear()

pen_Sunbury_Up_Train__Useable.clear()
pen_Sunbury_Down_Train__Useable.clear()
pen_Ballarat_Up_Train__Useable.clear()
pen_Ballarat_Down_Train__Useable.clear()
pen_Bendigo_Up_Train__Useable.clear()
pen_Bendigo_Down_Train__Useable.clear()
pen_Ballarat_Up_Freight_Train__Useable.clear()
pen_Ballarat_Down_Freight_Train__Useable.clear()

screen.update()
time.sleep(2)

Definition_Of_Sunbury_Up()
Sunbury_Up_Train()
Signal_Red_11_Sunbury_Up()
Signal_Red_12_Sunbury_Up()

screen.update()
time.sleep(1)

pen_Signal_Red_11__Useable.clear()
pen_Signal_Red_12__Useable.clear()
Signal_Green_11_Sunbury_Up()
Signal_Green_12_Sunbury_Up()

screen.update()
time.sleep(2)

pen_Definition_Of_Sunbury_Up__Useable.clear()
pen_Sunbury_Up_Train__Useable.clear()
pen_Signal_Green_11__Useable.clear()
pen_Signal_Green_12__Useable.clear()
Definition_Of_Sunbury_Down()
Sunbury_Down_Train()
Signal_Red_21_Sunbury_Down()
Signal_Red_22_Sunbury_Down()

screen.update()
time.sleep(1)

pen_Signal_Red_21__Useable.clear()
pen_Signal_Red_22__Useable.clear()
Signal_Green_21_Sunbury_Down()
Signal_Green_22_Sunbury_Down()

screen.update()
time.sleep(2)

pen_Definition_Of_Sunbury_Down__Useable.clear()
pen_Sunbury_Down_Train__Useable.clear()
pen_Signal_Green_21__Useable.clear()
pen_Signal_Green_22__Useable.clear()
Definition_Of_Ballarat_Up()
Ballarat_Up_Train()
Signal_Red_31_Ballarat_Up()
Signal_Red_32_Ballarat_Bendigo_Up()

screen.update()
time.sleep(1)

pen_Signal_Red_31__Useable.clear()
pen_Signal_Red_32__Useable.clear()
Signal_Green_31_Ballarat_Up()
Signal_Green_32_Ballarat_Bendigo_Up()

screen.update()
time.sleep(2)

pen_Definition_Of_Ballarat_Up__Useable.clear()
pen_Ballarat_Up_Train__Useable.clear()
pen_Signal_Green_31__Useable.clear()
pen_Signal_Green_32__Useable.clear()
Definition_Of_Ballarat_Down()
Ballarat_Down_Train()
Signal_Red_41_Ballarat_Bendigo_Down()
Signal_Red_42_Ballarat_Bendigo_Down()

screen.update()
time.sleep(1)

pen_Signal_Red_41__Useable.clear()
pen_Signal_Red_42__Useable.clear()
Signal_Green_41_Ballarat_Bendigo_Down()
Signal_Green_42_Ballarat_Bendigo_Down()

screen.update()
time.sleep(2)

pen_Definition_Of_Ballarat_Down__Useable.clear()
pen_Ballarat_Down_Train__Useable.clear()
pen_Signal_Green_41__Useable.clear()
pen_Signal_Green_42__Useable.clear()
Definition_Of_Bendigo_Up()
Bendigo_Up_Train()
Signal_Red_11_Sunbury_Up()
Signal_Red_32_Ballarat_Bendigo_Up()

screen.update()
time.sleep(1)

pen_Signal_Red_11__Useable.clear()
pen_Signal_Red_32__Useable.clear()
Signal_Green_11_Sunbury_Up()
Signal_Green_32_Ballarat_Bendigo_Up()

screen.update()
time.sleep(2)

pen_Definition_Of_Bendigo_Up__Useable.clear()
pen_Bendigo_Up_Train__Useable.clear()
pen_Signal_Green_11__Useable.clear()
pen_Signal_Green_32__Useable.clear()
Definition_Of_Bendigo_Down()
Bendigo_Down_Train()
Signal_Red_41_Ballarat_Bendigo_Down()
Signal_Red_42_Ballarat_Bendigo_Down()

screen.update()
time.sleep(1)

pen_Signal_Red_41__Useable.clear()
pen_Signal_Red_42__Useable.clear()
Signal_Green_41_Ballarat_Bendigo_Down()
Signal_Green_42_Ballarat_Bendigo_Down()

screen.update()
time.sleep(2)

pen_Definition_Of_Bendigo_Down__Useable.clear()
pen_Bendigo_Down_Train__Useable.clear()
pen_Signal_Green_41__Useable.clear()
pen_Signal_Green_42__Useable.clear()
Definition_Of_Ballarat_Up_Freight()
Ballarat_Up_Freight_Train()
Signal_Red_31_Ballarat_Up()
Signal_Red_32_Ballarat_Bendigo_Up()

screen.update()
time.sleep(1)

pen_Signal_Red_31__Useable.clear()
pen_Signal_Red_32__Useable.clear()
Signal_Green_31_Ballarat_Up()
Signal_Green_32_Ballarat_Bendigo_Up()

screen.update()
time.sleep(2)

pen_Definition_Of_Ballarat_Up_Freight__Useable.clear()
pen_Ballarat_Up_Freight_Train__Useable.clear()
pen_Signal_Green_31__Useable.clear()
pen_Signal_Green_32__Useable.clear()
Definition_Of_Ballarat_Down_Freight()
Ballarat_Down_Freight_Train()
Signal_Red_51_Freight_Down()
Signal_Red_42_Ballarat_Bendigo_Down()

screen.update()
time.sleep(1)

pen_Signal_Red_51__Useable.clear()
pen_Signal_Red_42__Useable.clear()
Signal_Green_51_Freight_Down()
Signal_Green_42_Ballarat_Bendigo_Down()

screen.update()
time.sleep(2)

pen_Definition_Of_Ballarat_Down_Freight__Useable.clear()
pen_Ballarat_Down_Freight_Train__Useable.clear()
pen_Signal_Green_51__Useable.clear()
pen_Signal_Green_42__Useable.clear()

screen.update()
time.sleep(2)

Signal_Red_11_Sunbury_Up()
Signal_Red_12_Sunbury_Up()
Signal_Red_21_Sunbury_Down()
Signal_Red_22_Sunbury_Down()
Signal_Red_31_Ballarat_Up()
Signal_Red_32_Ballarat_Bendigo_Up()
Signal_Red_41_Ballarat_Bendigo_Down()
Signal_Red_42_Ballarat_Bendigo_Down()
Signal_Red_51_Freight_Down()

Sunbury_Up_Refutation()
Sunbury_Down_Refutation()
Ballarat_Up_Refutation()
Ballarat_Down_Refutation()
Bendigo_Up_Refutation()
Bendigo_Down_Refutation()
Ballarat_Up_Freight_Refutation()
Ballarat_Down_Freight_Refutation_Part_1()
Ballarat_Down_Freight_Refutation_Part_2()

screen.update()
time.sleep(2)

pen_Sunbury_Up_Refutation__Useable.clear()
pen_Sunbury_Down_Refutation__Useable.clear()
pen_Ballarat_Up_Refutation__Useable.clear()
pen_Ballarat_Down_Refutation__Useable.clear()
pen_Bendigo_Up_Refutation__Useable.clear()
pen_Bendigo_Down_Refutation__Useable.clear()
pen_Ballarat_Up_Freight_Refutation__Useable.clear()
pen_Ballarat_Down_Freight_Refutation_Part_1__Useable.clear()
pen_Ballarat_Down_Freight_Refutation_Part_2__Useable.clear()

screen.update()
time.sleep(2)


pen_Signal_Red_11__Useable.clear()
pen_Signal_Red_12__Useable.clear()
pen_Signal_Red_21__Useable.clear()
pen_Signal_Red_22__Useable.clear()
pen_Signal_Red_31__Useable.clear()
pen_Signal_Red_32__Useable.clear()
pen_Signal_Red_41__Useable.clear()
pen_Signal_Red_42__Useable.clear()
pen_Signal_Red_51__Useable.clear()



Instructions()





Score_Number()

screen.update()
time.sleep(1)

pen_Score__Useable.clear()


# S1 Counter == 1'
# S2 Counter == 0
# S3 Counter == 1'
# S4 Counter == 1'










# screen.update()
# time.sleep(2)



# pen_Sunbury_Up_Train__Useable.clear()
# pen_Sunbury_Down_Train__Useable.clear()
# pen_Ballarat_Up_Train__Useable.clear()
# pen_Ballarat_Down_Train__Useable.clear()
# pen_Bendigo_Up_Train__Useable.clear()
# pen_Bendigo_Down_Train__Useable.clear()
# pen_Ballarat_Up_Freight_Train__Useable.clear()
# pen_Ballarat_Down_Freight_Train__Useable.clear()
# pen_Bendigo_Up_Freight_Train__Useable.clear()
# pen_Bendigo_Down_Freight_Train__Useable.clear()
# pen_Jacana_Loop_Up_Freight_Train__Useable.clear()
# pen_Jacana_Loop_Down_Freight_Train__Useable.clear()

# screen.update()
# time.sleep(2)



# screen.update()

# TURN THIS ON AND ITS PAIR
screen.update()

screen.listen()
screen.onkey(screen.bye, "Return")
screen.mainloop()











# This was the biggest waste of time I have ever done.
# Digitech was the most excruciating class I ever had.
# Over 80% of code hand made without copying other people's code.
# I stayed up till 12AM multiple times for this.