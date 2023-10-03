import turtle as t

def draw_pentagon(size):
    t.up()
    t.fd(size/2)
    t.lt(135)
    t.down()
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(65)
    t.fd(size)
    t.lt(70)
    t.fd(size)
    t.lt(70)
    t.fd(size)
    t.lt(65)
    t.fd(size)

def main():
    draw_pentagon(200)
    t.done()

if __name__ == '__main__':
    main()
