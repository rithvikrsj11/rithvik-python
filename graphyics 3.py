from turtle import *

# slowest speed
turtle.speed(0)
  
# turtle movement
turtle.forward(150)

bgcolor("black")
speed(0)
hideturtle()
for i in range (120):
 color('red')
 circle(i)
 color ('orange')
 circle(i*0.8)
 right (3)
 forward(3)
done()
