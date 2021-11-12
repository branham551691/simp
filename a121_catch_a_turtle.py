# a121_catch_a_turtle.py
#-----import statements-----
import turtle as t
import random as rand
import leaderboard_ as lb
#-----game configuration----
shape = "circle"
size = "2"
color = "lavender"
font_setup = ("Arial", 20, "normal")
score = 0
#-----background-----
bg_color = "purple"
t.bgcolor(bg_color)
#-----list of colors-----
colors = ["pale green", "sky blue", "pink", "yellow", "beige"]
#-----list of sizes-----
sizes = [1, 1.5, 2, 2.5]
#-----counter-----
counter_interval = 1000
timer_up = False
timer = 5
count = t.Turtle()
count.hideturtle()
count.penup()
count.goto(150,150)
count.pendown()
#-----leaderboard-----
leaderboard_file_name = "leaderboard_file1.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("please enter your name:  ")
#-----manages the leaderboard for top 5 scorers-----
def manage_leaderboard():
  global leader_scores_list
  global leader_names_list
  global score
  global spot
  #-----load all the leaderboard records into the lists-----
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)
  #-----TODO-----
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)
  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)
#-----initialize turtle-----
t.begin_fill()
t.shape(shape)
t.shapesize(rand.choice(sizes))
t.fillcolor(rand.choice(colors))
t.end_fill()
score_writer = t.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(150,100) 
score_writer.pendown()
score_writer.hideturtle()
spot = t.Turtle()
spot.color("purple")
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
def resize():
  sizes = [.5, 1, 1.5, 2]
  spot.shapesize(rand.choice(sizes))
def leave_a_mark():
  spot.fillcolor(rand.choice(colors[1:]))
  spot.stamp()
  spot.fillcolor(colors[0])
def change_position():
    t.penup()
    t.hideturtle()
    new_ypos = rand.randint(-150,150)
    new_xpos = rand.randint(-200,200)
    t.goto(new_xpos,new_ypos)
    t.pendown()
    t.showturtle()
def countdown():
    global timer, timer_up
    count.clear()
    if timer <= 0:
        count.write("time's up!", font = font_setup)
        timer_up = True
        manage_leaderboard()
    else:
        count.write("timer: " + str(timer), font = font_setup)
        timer -= 1
        count.getscreen().ontimer(countdown, counter_interval)
#-----end-----
wn = t.Screen()
t.onclick(spot_clicked)
wn.ontimer(countdown, counter_interval)
wn.mainloop()
