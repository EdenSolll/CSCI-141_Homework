import meteo as m


def fun(string):
    i = 0 
    r = 0 
    for char in string:
        if ord(string[i]) >= x and ord(string[i]) <= y:
                commands(string[r:i])
                r = i
        i = i + 1





def get_numbebr(string):
    i = 0
    b = 0
    for letter in string:
        if ord(letter) == 45 or ord(letter) >= 48 and ord(letter) <= 57:
            for letter in string[i:]:
                if ord(letter) == 45 or ord(letter) >= 48 and ord(letter) <= 57:
                    return string[i:b]
                else:
                    b += 1
        else:
            i += 1
def commands(cmd):
    if cmd[0] == 'S':
        m.draw_sun()
    if cmd[0] == 'P': 
       m.draw_sun() 
       m.draw_cloud()
    if cmd[0] == 'C':
        m.draw_cloud()
    if cmd[0] == 'R':
        m.draw_rain()
def main():
    m.background()
    input()
    
if __name__ == '__main__':
    main()
