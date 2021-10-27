#   116_version1.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name spider is used
spider = trtl.Turtle()
#size of the spider and its features
spider.pensize(40)
spider.circle(20)
legs = 8
length = 70
angle = 200 / legs
spider.pensize(5)
n = 0
#draws the legs using a while loop
while (n < legs):
  spider.goto(0,20)
  spider.setheading(angle*n)
  spider.forward(length)
  n = n + 1
spider.hideturtle()
legsn = trtl.Screen()
legsn.mainloop()