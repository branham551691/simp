#   a123_apple_1.py
import turtle as trtl
import random as rand
import time as time
#-----setup-----
apple_image = "apple.gif"
alp_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
ran_range = rand.randrange(len(alp_list))
#-----turtle-----
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
apple = trtl.Turtle()
drawer = trtl.Turtle()
def t():
  def artist():
    drawer.penup()
    drawer.color("white")
    drawer.write(alp_list[ran_range], font = ("Arial", 74, "bold"))
  artist()
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
  def draw_apple(active_apple):
    active_apple.shape(apple_image)
    apple.penup()
    apple.hideturtle()
    apple.goto(rand.randint(-100,100), rand.randint(-150,150))
    apple.showturtle()
    wn.update()

  def drop_apple():
    apple.penup()
    apple.goto(apple.xcor(),-150)
    drawer.clear()
    drawer.hideturtle()
#-----function calls-----
  draw_apple(apple)
  wn.bgpic("background.gif")
  wn.onkeypress(drop_apple, alp_list[ran_range])
  wn.listen()

for i in range(10):
  time.sleep(2)
  ran_range = rand.randrange(len(alp_list))
  drawer.clear()
  t()
wn.mainloop()
