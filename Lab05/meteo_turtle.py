import meteo as m

def string_processor(string):
    for chr in string:
        




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
    if cmd == 'S':
        m.draw_sun()
    if cmd == 'C':
        m.draw_cloud()

def main():
    m.background()
    input()
    
if __name__ == '__main__':
    main()
