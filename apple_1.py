#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()
drawer = trtl.Turtle()
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
def drop_apple(active_apple):
  drawer.color("blue")
  drawer.write("A", font=("Arial", 74, "bold"))
  apple.penup()
  apple.goto(apple.xcor(),-150)
#-----function calls-----
draw_apple(apple)
wn.onkeypress(drop_apple, "a")
wn.listen()
wn.bgpic("background.gif")
wn.mainloop()