import turtle as t 
import random as r

def setup_window():
    t.bk(200)
    t.down()
    t.rt(90)
    t.fd(200)
    t.lt(90)
    t.fd(400)
    t.lt(90)
    t.fd(400)
    t.lt(90)
    t.fd(400)
    t.lt(90)
    t.fd(200)
    t.up()
    t.lt(90)
    t.fd(200)        

def draw_snake_iter(segments):
    total = 0 
    while segments >= 1:
        t.lt(30)
        t.fd(r.randint(1, 20))
        
if __name__ == '__main__':
    input = int(input('Enter number of input segments (0-500): '))
    if input < 0 or input > 500:
        print('Error, input out of range')
    else:
        setup_window()
        print(draw_snake_iter(input))
