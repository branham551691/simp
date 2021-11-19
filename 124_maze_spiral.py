#-----pseudocode-----
  #use forward to make walls + pensize to make it thicker
  #use function that increases size of walls (look at previous assignments)
  #use loops to make more walls (while/for)

#-----import turtle-----
import turtle as trtl
maze_painter = trtl.Turtle()
#-----variables-----
path_width = inc #increment
#-----making walls-----
maze_painter.forward(10)
maze_painter.penup()
maze_painter.forward(path_width*2)
maze_painter.pendown()

wn = trtl.Screen()
wn.mainloop()