# group members: Eulina, Harshita, Supriya, Tamara
import turtle as trtl
t = trtl.Turtle()

t.speed(0)

# coordinate plane
t.pensize(4)

t.penup()
t.goto(-200,0)
t.pendown()
t.forward(400)
t.penup()
t.goto(0,200)
t.right(90)
t.pendown()
t.forward(400)

t.pensize(1)

x = -200
for i in range(21):
    t.penup()
    t.goto(x,200)
    t.pendown()
    
    t.forward(400)

    x = x + 20  

t.left(90)
y = -200
for i in range(21):
    t.penup()
    t.goto(-200,y)
    t.pendown()
    
    t.forward(400)

    y = y + 20

# ask user for equation
user_input = input("Write an equation in the format, y=mx+b, where m and b are positive whole integers and x and y are left as x and y: ")

# define variables of equation

m = int(user_input[2])
b = int(user_input[5])
b = b*20

# draw line with equation
t.pensize(5)
t.color("red")

# point 1
x = -200
y = m * x + b

t.penup()
t.goto(x, y)
t.pendown()

# point 2, y-intercept
t.goto(0, b)

# point 3
x = 200
y = m * x + b

t.goto(x, y)

wn = trtl.Screen()
wn.mainloop()