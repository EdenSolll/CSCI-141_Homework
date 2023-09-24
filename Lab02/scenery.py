import turtle as t

def pinetree():
    t.down()
    t.pencolor('green')
    t.bk(100)
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(30)
    t.rt(120)
    t.fd(60)
    t.rt(120)
    t.fd(60)
    t.rt(120)
    t.fd(30)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.bk(100)
    t.up()


def house():
    t.pencolor('cyan')
    t.down()
    t.fd(50)
    t.lt(90)
    t.fd(100)
    t.rt(45)
    t.fd(70)
    t.rt(90)
    t.fd(70)
    t.rt(45)
    t.fd(100)
    t.lt(90)
    t.fd(50)
    t.bk(150)
    t.fd(50)
    t.up()

def mapletree():
    t.down()
    t.pencolor('green')
    t.bk(100)
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.circle(25)
    t.up()


if __name__ == '__main__':
    # house_color = print(input('What color is the house? '))
    #
    pinetree()
    t.fd(100)
    house()
    t.fd(100)
    mapletree()
    t.done()

