import turtle as t

timmy = t.Turtle()
screen = t.Screen()

def move_forwards():
    timmy.forward(10)

def move_backwards():
    timmy.backward(10)

def clockwise():
    timmy.setheading(timmy.heading()+30)

def counterclockwise():
    timmy.setheading(timmy.heading()-30)



def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()



timmy = t.Turtle()
screen = t.Screen()
screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(clockwise, "a")
screen.onkey(counterclockwise, "d")
screen.onkey(clear, "c")



screen.exitonclick()
