# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
t=trtl
#-----game configuration----
shape = "circle"
size = "2"
color = "blue"

#-----initialize turtle-----
t.begin_fill()
t.shape(shape)
t.shapesize(int(size))
t.fillcolor(color)
t.end_fill()

#-----game functions--------
def spot_clicked (x, y):
  change_position(x, y)
t.onclick(spot_clicked)

def change_position(x, y):
  t.penup()
  new_xpos = rand.randint(-150, 150)
  new_ypos = rand.randint(-150, 150)
  rand.randint(-200, 200)
  t.goto(new_xpos, new_ypos)


#-----events----------------
wn = t.Screen()
wn.mainloop()