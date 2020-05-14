from turtle import Turtle
from random import randint

laura = Turtle()
laura.color('red')
laura.shape('turtle')

laura.penup()
laura.goto(-160,100)
laura.pendown()

matt = Turtle()
matt.color('green')
matt.shape('turtle')

matt.penup()
matt.goto(-160,70)
matt.pendown()

mary = Turtle()
mary.color('blue')
mary.shape('turtle')

mary.penup()
mary.goto(-160,40)
mary.pendown()

john = Turtle()
john.color('yellow')
john.shape('turtle')

john.penup()
john.goto(-160,10)
john.pendown()

for movement in range(100):
  laura.forward(randint(1,5))
  matt.forward(randint(1,5))
  mary.forward(randint(1,5))
  john.forward(randint(1,5))
  
  