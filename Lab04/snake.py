"""
Eden Grace
CSCI-141 LAB04 Snakes
Professor Lima
Using the turtle import this program uses different methods of drawing a snake
including recusion, tail recursion, and iteration (while loop). 
"""
import turtle as t 
import random 

MAX_SEGMENTS = 500
BOUNDING_BOX = 200 
MAX_LENGTH = 20 
MAX_THICKNESS = 10
MAX_ANGLES = 30
COLOR_MAX = 255

def setup_window():
    """
    This function setsup the box boundaries and returns to the starting position 
    ready to begin using any of the drawing functions
    """
    t.up()
    t.bk(BOUNDING_BOX)
    t.down()
    t.rt(90)
    t.fd(BOUNDING_BOX)
    t.lt(90)
    t.fd(BOUNDING_BOX*2)
    t.lt(90)
    t.fd(BOUNDING_BOX*2)
    t.lt(90)
    t.fd(BOUNDING_BOX*2)
    t.lt(90)
    t.fd(BOUNDING_BOX)
    t.up()
    t.lt(90)
    t.fd(BOUNDING_BOX)
    t.down()


def draw_snake_rec(segments):
    """
    This function uses non tail end recursion to draw a snake while avoid the box boundaries
    """
    if segments == 0:
        return 0
    else:
        length = random.randint(1, MAX_LENGTH)
        t.colormode(COLOR_MAX)
        t.pencolor(random.randint(0, COLOR_MAX), random.randint(0, COLOR_MAX), random.randint(0, COLOR_MAX)) 
        t.width(random.randint(1, MAX_THICKNESS))
        t.lt(random.randint(-MAX_ANGLES, MAX_ANGLES))
        if t.xcor() >= BOUNDING_BOX - 25 or t.xcor() <= -(BOUNDING_BOX - 25) \
                or t.ycor() >= BOUNDING_BOX - 25 or t.ycor() <= -(BOUNDING_BOX - 25): 
            t.setheading(t.towards(0,0))
        t.fd(length)
        return draw_snake_rec(segments - 1) + length


def draw_snake_tail(segments, total):
    """
    This function uses tail end recursion to draw a snake while avoid the box boundaries 
    """
    if segments == 0:
        return int(total)
    else:
        length = random.randint(1, MAX_LENGTH)
        t.colormode(COLOR_MAX)
        t.pencolor(random.randint(0, COLOR_MAX), random.randint(0, COLOR_MAX), random.randint(0, COLOR_MAX)) 
        t.width(random.randint(1, MAX_THICKNESS))
        t.lt(random.randint(-MAX_ANGLES, MAX_ANGLES))
        if t.xcor() >= BOUNDING_BOX - 25 or t.xcor() <= -(BOUNDING_BOX - 25) \
                or t.ycor() >= BOUNDING_BOX - 25 or t.ycor() <= -(BOUNDING_BOX - 25): 
            t.setheading(t.towards(0,0))
        t.fd(length)
        total += length
        return draw_snake_tail(segments - 1, total)


def draw_snake_iter(segments):
    """
    This function uses interation via a while loop to draw a snake and avoid the box boundaries 
    """
    total = 0
    while segments >= 1:
        length = random.randint(1, MAX_LENGTH)
        t.colormode(COLOR_MAX)
        t.pencolor(random.randint(0, COLOR_MAX), random.randint(0, COLOR_MAX), random.randint(0, COLOR_MAX)) 
        t.width(random.randint(1, MAX_THICKNESS))
        t.lt(random.randint(-MAX_ANGLES, MAX_ANGLES))
        if t.xcor() >= BOUNDING_BOX - 25 or t.xcor() <= -(BOUNDING_BOX - 25) \
                or t.ycor() >= BOUNDING_BOX - 25 or t.ycor() <= -(BOUNDING_BOX - 25): 
            t.setheading(t.towards(0,0))
        t.fd(length)
        total += length
        segments -= 1 
    return total


def main():
    """
    This main function calls for the user to input a validated number of segments which are then passed to all three forms 
    of drawing the snake. The function will print the total value of length used by each function then resetting the canvas
    and waiting for the user to press enter before starting the next draw function.
    """
    segment_input = int(input('Enter number of input segments (0-500): '))
    if segment_input < 0 or segment_input > MAX_SEGMENTS:
        print('Error, input out of range')
        exit()    
    else:
        setup_window()
        print(f'Recursive snake’s length is {draw_snake_rec(segment_input)} units.')
        input('Hit enter to continue...')
        t.reset()
        setup_window()
        print(f'Tail Recursive snake’s length is {draw_snake_tail(segment_input, 0)} units.')
        input('Hit enter to continue...') 
        t.reset()
        setup_window()
        print(f'Iterative snake’s length is {draw_snake_iter(segment_input)} units.')
        print('Close the canvas when finished viewing')
        t.done()

if __name__ == '__main__':
    main()
