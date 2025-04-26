#Imports
import os
import random
import turtle

#Basic define
turtle.fd(0)#required in MacOS
turtle.bgcolor("black")
turtle.speed(0)
turtle.hideturtle()#Hides the turtle
turtle.tracer(1)#Speeds up the drawing
turtle.setundobuffer(1)#Save the memory

#Classes
class Sprite(turtle.Turtle):
    def __init__(self, color, SpriteShape, x, y):
        turtle.Turtle.__init__(self, shape = SpriteShape)
        self.color(color)
        self.shape(SpriteShape)
        self.penup()
        self.goto(x, y)
        turtle.speed(0)
        turtle.fd(0)
        
        self.speed = 1
        
    def move(self):
        self.forward(self.speed)
        
class Player(Sprite):
    def __init__(self, color, SpriteShape, x, y):
        Sprite.__init__(self, color, SpriteShape, x, y)
        self.speed = 4
        self.lives = 3
        
        
        

#Sprites
player = Player("white", "triangle", 0, 0)

#Main loop
while True:
    player.move()


delay = input("Press enter to finish.")