"""
Eden Grace CS021 
Professor Lima 
Lab03 Bowties.py

This is a program that uses recursion to draw bowties in a specified pattern.
This is done by using two functions. One which takes an input value of size, then draws a singluar bowtie-
returning to its starting position before ending. And a second function which uses the first bowtie function-
and itself to recursively draw bowties in the pattern. The recursive function in initally called in the main gate-
using user input values for the initial size of the bowtie and the depth the recursion should go to.
"""


import turtle as t

def bowtie(size):
    """
    Draws a bowtie shape using the turtle graphics library.

    Post-conditions: Turtle is pen-up, with black pen ink, facing east (default dirrection which I was told to set it to by Kedar)
    """
    t.down()
    t.lt(30)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.rt(120)
    t.fd(size*2)
    t.lt(120)
    t.fd(size)
    t.lt(120)
    t.fd(size)
    t.rt(120)
    t.up()
    t.fd(size/4)
    t.lt(90)
    t.down()
    t.fillcolor('red')
    t.begin_fill()
    t.circle(size/4)
    t.end_fill()
    t.up()
    t.lt(90)
    t.fd(size/4)
    t.pencolor('black')
    t.rt(90)



def recursive_drawing(depth, size):
    """
    Recurively draws bowties at decreasing sizes per a larger input depth valuue


    Post-conditions: Turtle is pen-up, with black pen ink, facing east
    """
    bowtie(size)
    if depth >= 1:
        t.up()
        t.lt(30)
        t.fd(size*2)
        recursive_drawing(depth-1, size/3)
        t.bk(size*2)
        t.rt(60)
        t.fd(size*2)
        recursive_drawing(depth-1, size/3)
        t.bk(size*2)
        t.rt(120)
        t.fd(size*2)
        recursive_drawing(depth-1, size/3)
        t.bk(size*2)
        t.rt(60)
        t.up()
        t.fd(size*2)
        recursive_drawing(depth-1, size/3)
        t.bk(size*2)
        t.rt(150)


if __name__ == '__main__':
    """
    Main gate function which prompts the user for input size and depth, then initiates the drawing.
    """

    inputsize = int(input('Enter starting bowtie size: '))
    inputdepth = int(input('Enter starting bowtie depth: '))
    recursive_drawing(inputdepth, inputsize)
    t.done()
