
"""
    meteo.py
    assignment: lab 4
    language: python3
    author: YOUR NAME GOES HERE

"""

import turtle as t

def background():
    """
    load the background for the meteo weather map and
    set up the turtle window size and position in the screen's upper left.
    """
    screen = t.Screen()
    screen.bgpic("simland.png")
    t.setup(1100, 650, 0, 0)
    

def draw_rectangle(length, width):
    """
    draws a rectangle with the given length and width
    :param length:
    :param width:
    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up
    """
    for _ in range(2):
        t.fd(length)
        t.lt(90)
        t.fd(width)
        t.lt(90)

def snowflake(length=8):
    """
    draws a 6-arms snowflake
    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up:
    """
    for _ in range(5):
        t.lt(60)
        t.fd(length)
    

def draw_sun(r=16):
    t.pencolor('yellow')
    t.fillcolor('yellow')
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.setheading(0)
    t.penup()

def draw_rain(size=16):
    """

    """
    t.down()
    x = t.xcor()
    y = t.ycor()
    draw_cloud()
    t.up()
    t.rt(90)
    t.fd(size/2)
    for _ in range(4):
        t.down()
        t.rt(30)
        t.fd(size)
        t.bk(size)
        t.rt(60)
        t.up()
        t.fd(size/2)
        t.lt(90)
    t.goto(x,y)
    t.setheading(0)
    t.penup()

def draw_cloud(r=16):
    """
    draws a pretty cloud as a combination of: 1 circle of radius r,
    2 circles of radius r/2 and a rectangle 2r x r
    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up, pencolor black
    """
    t.pencolor("blue")
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(r/2)
    draw_rectangle(2.2*r, r)
    t.forward(1.2*r)
    t.circle(r)
    t.forward(1.2*r)
    t.circle(r/3)
    t.end_fill()
    t.pencolor("black")
    
    
def draw_snow(size=8):
    """
    draws 3 snowflakes and a cloud
    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up
    """
    draw_cloud(2*size)
    t.up()
    t.backward(4*size)
    t.right(90)
    t.forward(size)
    t.left(90)
    snowflake(size)
    t.right(45)
    t.forward(2*size)
    t.left(45)
    snowflake(size)
    t.left(45)
    t.forward(2*size)
    t.right(45)
    snowflake(size)
    

if __name__ == "__main__":
    background()

