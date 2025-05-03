#Imports
import os
import random
import turtle

#Basic define
turtle.fd(0)#required in MacOS
turtle.bgcolor("black")
turtle.speed(0)
turtle.ht()#Hides the turtle
turtle.tracer(1)#Speeds up the drawing
turtle.setundobuffer(1)#Save the memory

#Set the screen size
turtle.setup(650, 650)

#Classes
class Sprite(turtle.Turtle):
    def __init__(self, color, SpriteShape, x, y):
        #Initialize the sprite with the given color and shape
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
        
        #Boundary detection
        if self.xcor() > 290:
            self.rt(60)
            self.setx(290)
        
        if self.xcor() < -290:
            self.rt(60)
            self.setx(-290)
        
        if self.ycor() > 290:
            self.rt(60)
            self.sety(290)
        
        if self.ycor() < -290:
            self.rt(60)
            self.sety(-290)
        
class Player(Sprite):
    def __init__(self, color, SpriteShape, x, y):
        Sprite.__init__(self, color, SpriteShape, x, y)
        self.speed = 4
        self.lives = 3
        self.shapesize(0.8, 1.5, outline=None)
        
    def left(self):
        self.lt(45)

    def right(self):
        self.rt(45)
        
    def accelerate(self):
        self.speed += 1
        
    def decelerate(self):
        self.speed -= 1
        
    def is_collision(self, other):
        if (self.xcor() > other.xcor() - 20) and (self.xcor() < other.xcor() + 20):
            if (self.ycor() > other.ycor() - 20) and (self.ycor() < other.ycor() + 20):
                return True
        else:
            return False
        
class Enemy(Sprite):
    def __init__(self, color, SpriteShape, startx, starty):
        Sprite.__init__(self, color, SpriteShape, startx, starty)
        self.speed = 6
        self.setheading(random.randint(0, 360))
        
class Missile(Sprite):
    def __init__(self, color, SpriteShape, startx, starty):
        Sprite.__init__(self, color, SpriteShape, startx, starty)
        self.shapesize(0.3, 0.6, outline=None)
        self.speed = 20
        self.status = "ready"
        self.goto(-1000, 1000) # Hide the missile off screen
        
    def fire(self):
        if self.status == "ready":
            self.setheading(player.heading())
            self.goto(player.xcor(), player.ycor())
            self.status = "fire"
            # self.forward(10)
        
    def move(self):
        if self.status == "fire":
            self.fd(self.speed)
        
        #border detection
        if self.xcor() > 290 or self.xcor() < -290 or self.ycor() > 290 or self.ycor() < -290:
            self.goto(-1000, 1000)
            self.status = "ready"
        
class Game():
    #Game class to manage the border, game state and score.
    def __init__(self):
      self.score = 0
      self.level = 1
      self.state = "playing"
      self.pen = turtle.Turtle()
      self.lives = 3
      
    def draw_border(self):
        self.pen.speed(0)
        self.pen.pensize(3)
        self.pen.color("white")
        self.pen.penup()
        self.pen.goto(-300, -300)
        self.pen.pendown()
        for side in range(4):
            self.pen.forward(600)
            self.pen.lt(90)
        self.pen.penup()
        
        self.pen.ht()
        
#Creating game object
game = Game()

#Creating the border
game.draw_border()

#Sprites
player = Player("white", "triangle", 0, 0)
enemy = Enemy("red", "circle", random.randint(-290, 290), random.randint(-290, 290))
missile = Missile("yellow", "triangle", 0, 0)

#keys binding
turtle.onkey(player.left, "a")
turtle.onkey(player.right, "d")
turtle.onkey(player.accelerate, "w")
turtle.onkey(player.decelerate, "s")
turtle.onkey(missile.fire, "space")
turtle.listen()

#Main loop
while True:
    player.move()
    enemy.move()
    # missile.move()
    
    turtle.update()
    
    #Check for collision
    if player.is_collision(enemy):
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        enemy.goto(x, y)
    