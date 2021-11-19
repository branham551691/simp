#   a123_apple_1.py
import turtle as trtl
import random as rand
#-----setup-----
apple_image = "apple.gif"
let_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
ran_range = rand.randrange(len(let_list))
#-----turtle-----
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)
wn.bgpic("background.gif")
# Make the screen aware of the new file
apple = trtl.Turtle()
drawer = trtl.Turtle()

apple_list = []
apple_let = []

for i in range (5):
  apple_list.append(trtl.Turtle())
  apple_let.append(rand.choice(let_list))

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(index):
  apple_list[index].penup()
  apple_list[index].shape(apple_image)
  wn.tracer(False)
  apple_list[index].setx(rand.randint(-150,150))
  apple_list[index].sety(rand.randint(-15,100))
  apple_list[index].sety(apple_list[index].ycor()-25)
  apple_list[index].color("white")
  apple_list[index].write(apple_let[index], align = "center", font=("Arial", 30, "bold")) 
  apple_list[index].sety(apple_list[index].ycor()+25)
  apple_list[index].showturtle()
  wn.tracer(True)
  wn.update()

def drop_apple(index):
  apple_list[index].penup()
  apple_list[index].clear()
  apple_list[index].sety(-150)
  apple_list[index].hideturtle()
#-----function calls-----
def typeA():
  for i in range (5):
   if apple_let[i] == "a":
    drop_apple(i)

def typeB():
  for i in range (5):
   if apple_let[i] == "b":
    drop_apple(i)

def typeC():
  for i in range (5):
   if apple_let[i] == "c":
    drop_apple(i)

def typeD():
  for i in range (5):
   if apple_let[i] == "d":
    drop_apple(i)

def typeE():
  for i in range (5):
   if apple_let[i] == "e":
    drop_apple(i)

def typeF():
  for i in range (5):
   if apple_let[i] == "f":
    drop_apple(i)

def typeG():
  for i in range (5):
   if apple_let[i] == "g":
    drop_apple(i)

def typeH():
  for i in range (5):
   if apple_let[i] == "h":
    drop_apple(i)

for i in range(5):
  draw_apple(i)

wn.onkeypress(typeA, "a")
wn.onkeypress(typeB, "b")
wn.onkeypress(typeC, "c")
wn.onkeypress(typeD, "d")
wn.onkeypress(typeE, "e")
wn.onkeypress(typeF, "f")
wn.onkeypress(typeG, "g")
wn.onkeypress(typeH, "h")
wn.onkeypress(drop_apple, let_list[ran_range])
wn.listen()
wn.mainloop()
