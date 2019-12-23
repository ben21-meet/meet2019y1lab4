from turtle import Turtle
import random
import turtle

class Ball(Turtle):
	def __init__(self,r,color,dx,dy,):
		self.r = r
		self.color = color 
		self.penup()
		self = (r,dx,dy)
		Turtle.shape("Circle")
		self = r/10
	def move(screen_width,screen_height):
		self.dx = current_x
		current_x = new_x
		self.dy = current_y
		current_y = new_y
		right_side_ball = (new_x + r)
		left_side_ball = (new_y + r)
		print("Ball is moving..")
	screen_width = turtle.getcanvas().winfo_width()/2
	screen_height = turtle.getcanvas().winfo_height()/2

ben23 = Ball(100,"Yellow",100,100)
i = 989
while i < 1000:
	ben23.move()
	i += 1

turtle.mainloop()