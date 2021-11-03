# a121_catch_a_turtle.py
#-----import statements-----
import turtle as t
import random as rand
#-----game configuration----
shape = "circle"
size = "2"
color = "lavender"
font_setup = ("Arial", 20, "normal")
score = 0

#-----counter-----
counter_interval = 1000
timer_up = False
timer = 30
count = t.Turtle()
count.hideturtle()
count.penup()
count.goto(150,200)
count.pendown()


#-----initialize turtle-----
t.begin_fill()
t.shape(shape)
t.shapesize(int(size))
t.fillcolor(color)
t.end_fill()
score_writer = t.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(150,150) 
score_writer.pendown()
score_writer.hideturtle()

#-----game functions--------
def update_score():
    global score 
    score += 1
    score_writer.clear()
    score_writer.write(score, font = font_setup)
def spot_clicked(x,y):
    global timer_up
    if (not timer_up):
        update_score()
        change_position()
    else:
        t.hideturtle()
        update_score()
def change_position():
    t.penup()
    t.hideturtle()
    new_ypos = rand.randint(-250,250)
    new_xpos = rand.randint(-250,250)
    t.goto(new_xpos,new_ypos)
    t.pendown()
    t.showturtle()
def countdown():
    global timer, timer_up
    count.clear()
    if timer <= 0:
        count.write("time's up!", font = font_setup)
        timer_up = True
    else:
        count.write("timer: " + str(timer), font = font_setup)
        timer -= 1
        count.getscreen().ontimer(countdown, counter_interval)
 
#-----end-----
wn = t.Screen()
t.onclick(spot_clicked)
wn.ontimer(countdown, counter_interval)
wn.mainloop()
