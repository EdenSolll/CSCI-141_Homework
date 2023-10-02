"""
    meteo.py
    assignment: lab 4
    language: python3
    author: Eden Grace
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
    :pre-conditions: turtle faces east2, pen up
    :post-conditions: turtle faces east, pen up
    """
    t.fd(length/2)
    t.lt(90)
    t.down()
    t.fd(width/2)
    t.lt(90)
    t.fd(length)
    t.lt(90)
    t.fd(width)
    t.lt(90)
    t.lt(length)
    t.lt(90)
    t.fd(width/2)
    t.up()
    t.rt(90)
    t.bk(length/2)



def snowflake(length=8):
    """
    draws a 6-arms snowflake
    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up
    """
    t.down()
    for _ in range(5):
        t.fd(length)
        t.bk(length)
        t.lt(60)
    t.up()


def draw_sun(r=16):
    t.fillcolor('yellow')
    t.begin_fill() 
    t.circle(r)
    t.end_fill()

def draw_rain(size=16):

    pass # YOUR CODE AND DOCSTRING  GOES HERE
    
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
    t.circle(r/2)
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
