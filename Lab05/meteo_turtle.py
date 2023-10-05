"""
    meteo_turtle.py
    assignment: lab 5
    language: python3
    author: Eden Grace
"""

import meteo as m
import turtle as t


def process_string(string):
    """
    Takes a string iterates through it searching for the end of each command.
    Errors out if an index error occours
    """
    i = 1
    while True:
        try:
            if len(string) == i + 1:
                commands(string)
                t.done()
                break
            if 65 <= ord(string[i]) <= 90 and ord(string[i]) != 71:
                commands(string[:i])
                string = string[i:]
                i = 1
            elif i >= 1:
                if ord(string[i]) == 71 and ord(string[i - 1]) <= 57:
                    commands(string[:i])
                    string = string[i:]
                    i = 1
            i = i + 1
        except IndexError:
            return None
            

def get_number(string):
    """
    Takes a command section and strips the numbers for it and returns 
    two numbers if the command is goto, otherwise returning just a single number
    """
    i = 0  # lastchar index
    r = 0  # comma location
    for ind in range(len(string)):
        if ord(string[ind]) == 44:
            r = ind
        if ord(string[ind]) >= 65 and ord(string[i]) <= 90 and ord(
                string[ind + 1]) <= 57:
            i = ind
    if string[0] == 'G' or string[1] == 'G':
        return string[i + 1:r], string[r + 1:]
    else:
        return string[i:]


def commands(cmd):
    """
    Takes the command from the string slicer and checks which commands need to be called
    then each command calls to either the meteo.py file where the command is stored or calls to the 
    get number function to get the required numbers for the command
    """
    if cmd[0] == 'G':
        x, y = get_number(cmd)
        t.up()
        t.goto(int(x), int(y))
    elif cmd[0] == 'S':
        m.draw_sun()
    elif cmd[0] == 'P':
        m.draw_sun()
        m.draw_cloud()
    elif cmd[0] == 'C':
        m.draw_cloud()
    elif cmd[0] == 'R':
        m.draw_rain()
    elif cmd[0] == 'W':
        m.draw_snow()
    elif cmd[0] == 'T':
        x = get_number(cmd)
        t.pencolor('white')
        t.fillcolor('white')
        t.begin_fill()
        m.draw_rectangle(36, 16)
        t.end_fill()
        t.pencolor('black')
        t.write(str(x)[1:] + 'F', font=('Arial', 9, 'bold'))
    elif cmd[0] == 'A':
        t.pencolor('red')
        t.down()
        x = get_number(cmd)
        t.circle(int(str(x)[1:]))
    if cmd[1] == 'G':
        x, y = get_number(cmd)
        t.up()
        t.goto(int(x), int(y))
    else:
        return None

def main():
    """
    Draws the background from meteo.py then asks user for the command string
    then sending it to the string processor function
    """
    m.background()
    t.speed(0)
    input_string = input('Enter your command strings')
    process_string(input_string)


if __name__ == '__main__':
    main()
