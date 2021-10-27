# a113_tower.py
# modify this code in VS Code to alternate colors
import turtle as trtl

painter=trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location
x=-150
y=-150

# height of tower and a counter of floors
num_floors=21
floor=0

# iterate
while floor<num_floors:
  painter.penup()
  painter.goto(x,y)
  painter.color("gray")
  y=y+5
  rem=floor%3
  if (rem==0):
    painter.color("pink")
  rem=floor%2
  if (rem==0):
    painter.color("yellow")
  painter.stamp()
  floor=floor+1

  painter.pendown()
  painter.forward(50)
  
# starting location
x=-75
y=-150

# height of tower and a counter of floors
num_floors=21
floor=0

# iterate
while floor<num_floors:
  painter.penup()
  painter.goto(x,y)
  painter.color("gray")
  y=y+5
  rem=floor%3
  if (rem==0):
    painter.color("pink")
  rem=floor%2
  if (rem==0):
    painter.color("orange")
  painter.stamp()
  floor=floor+1

  painter.pendown()
  painter.forward(50)
   # starting location
x=0
y=-150

# height of tower and a counter of floors
num_floors=21
floor=0

# iterate
while floor<num_floors:
  painter.penup()
  painter.goto(x,y)
  painter.color("gray")
  y=y+5
  rem=floor%3
  if (rem==0):
    painter.color("pink")
  rem=floor%2
  if (rem==0):
    painter.color("red")
  painter.stamp()
  floor=floor+1

  painter.pendown()
  painter.forward(50)

wn=trtl.Screen()
wn.mainloop()
