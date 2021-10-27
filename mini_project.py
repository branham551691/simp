import turtle as trtl
mini=trtl.Turtle()

number_of_circles=int(input("how many circles would you like to make?"  ))

def number_of_circles():
  mini.circle(20)
  mini.forward(40)

x=number_of_circles

while(x<=10):
  color_circles=input("enter color"  )
  mini.fillcolor(color_circles)
  mini.begin_fill()
  print (number_of_circles)
  