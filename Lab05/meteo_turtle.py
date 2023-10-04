import meteo as m
import turtle as t

def fun(string):
    i = 1
    r = 0
    for _ in string:
        if ord(string[i]) >= 65 and ord(string[i]) <= 90 and ord(string[i]) != 71:
             commands(string[r:i])
             break
        i = i + 1

def get_number(string):
    i = 0 #lastchar index 
    r = 0 #comma location
    for ind in range(len(string)):
        if ord(string[ind]) == 44: 
            r = ind
        if ord(string[ind]) >= 65 and ord(string[i]) <= 90 and ord(string[ind+1]) <= 57:
            i = ind
    if string[0] == 'G' or string[1] == 'G':
        return string[i+1:r], string[r+1:]
    else:
        return string[i+1:]

def commands(cmd):
    if cmd[0] == 'S':
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
        t.write(str(x) + 'F', font=('Arial', 9, 'bold'))
    elif cmd[0] == 'A':
        x = get_number(cmd)
        t.pencolor('red')
        t.circle(x[0])
    if cmd[0] == 'G':
        x,y = get_number(cmd)
        t.up()
        t.goto(int(x),int(y))
        t.down()
    if cmd[1] == 'G':
        x,y = get_number(cmd)
        t.goto(int(x),int(y))
        t.up()


def main():
    m.background()
    s = "RG100,100SG20,200PG10,190T50G-200,-40WG-210,-50T70G20,-200A40" 
    fun(s)
    t.done()

if __name__ == '__main__':
    main()
