import pygame 
from tkinter import *
import random
import time
import sys, time
import os

def sprint(str):
    for c in str + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3. / 90)

#user input name
      
P1 = input("player name: ") 
print() 
sprint("Your mission is to defend the base. Move the arrow keys to move the paddle")
print() 

class Ball:

    def __init__(self, canvas, color, size, paddle):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, size, size, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.xspeed = random.randrange(-3, 3)
        self.yspeed = -1
        self.hit_bottom = False
        self.score = 0

    def draw(self):
        self.canvas.move(self.id, self.xspeed, self.yspeed)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.yspeed = 3
        if pos[3] >= 400:
            self.hit_bottom = True
        if pos[0] <= 0:
            self.xspeed = 3
        if pos[2] >= 500:
            self.xspeed = -3
        if self.hit_paddle(pos) == True:
            self.yspeed = -3
            self.xspeed = random.randrange(-3, 3)
            self.score += 10
     
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False


# Define paddle properties and functions


class Paddle:

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 150, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.xspeed = 0
        self.canvas.bind_all('<KeyPress-Left>', self.move_left)
        self.canvas.bind_all('<KeyPress-Right>', self.move_right)

    def draw(self):
        self.canvas.move(self.id, self.xspeed, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.xspeed = 0
        if pos[2] >= 500:
            self.xspeed = 0
#######################

    def move_left(self, evt):
        self.xspeed = -6

    def move_right(self, evt):
        self.xspeed = 5


# Create window and canvas to draw on
tk = Tk()
tk.title("Ball Game")
canvas = Canvas(tk, width=500, height=400, bd=0, bg='aquamarine')
canvas.pack()
label = canvas.create_text(5, 5, anchor=NW, text="Score: 0")
tk.update()
#######################
paddle = Paddle(canvas, 'black')
ball = Ball(canvas, 'black', 25, paddle)

# Animation loop
while ball.hit_bottom == False:
    ball.draw()
    paddle.draw()
    canvas.itemconfig(label,
                      fill='black',
                      text="Score: " + str(ball.score))  
#code prints a statement and breaks the loop
    while ball.hit_bottom == True:
     sprint("Pathetic, not even close, because of your failure our base had been raided") 
     break
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01) 
#code prints a statement and breaks the loop 
    if ball.score == 100: 
      sprint("Thank you " + P1 + ". You have succesfully defended the base")  
      break




      








































