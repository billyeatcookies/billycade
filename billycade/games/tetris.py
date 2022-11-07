import time,os 

BS="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def bastr(s, b):
    res = ""
    while s:
        res+=BS[s%b]
        s//= b
        return res[::-1] or "0"

def t(a, b, c, d, e=0):
    d += c
    e = a | b << d
    if d < 0 | a & b << d:
        a = e = int(str(a | b << c).replace('\t', ''), d)
    b = 1 if time.time() % 2 else 3

    return a, b, d, e

board = 0
block = 3
position = 32
display=0

def update(offset):
    global board, block, position, display 
    try:
        txt = ""
        result = t(board, block, position, offset)
    
    
        board = result[0]
        block = result[1]
        position = result[2]
        display = result[3]

        display = "{0:b}".format(1<<30|display)
                                    
        for i in range(1,30):
            txt += "#" if (display[i] == "1") else "."
            if(i%5 == 0):
                txt+= "\n"
    except:
        pass 

    os.system('clear')
    print(txt)
update(0)
speed = 1000

while True:
    update(-5)
    time.sleep(1)
