import math
file = open("ex.in")
input = file.read()
lines = input.split("\n")

pos_h = (0,0)
pos_t = (0,0)

def print_grid():
    out = ""
    num_rows = 5
    num_cols = 6
    global pos_h
    global pos_t
    for row in range(num_rows):
        for col in range(num_cols):
            if(pos_h == (col, num_rows-1-row)):
                out = out + "H"
            elif(pos_t == (col,num_rows-1-row)):
                out = out + "T"
            else:
                out = out + "."
        out = out + "\n"
    print(out)


def move(dir, pos_h, pos_t):
    new_h = ()
    new_t = ()
    if(dir == "U"):
        new_h = (pos_h[0], pos_h[1]+1)
        new_t = (pos_h[0], pos_t[1]+1)
    elif(dir == "D"):
        new_h = (pos_h[0], pos_h[1]-1)
        new_t = (pos_h[0], pos_t[1]-1)
    elif(dir == "L"):
        new_h = (pos_h[0]-1, pos_h[1])
        new_t = (pos_t[0]-1, pos_h[1])
    else:
        new_h = (pos_h[0]+1, pos_h[1])
        new_t = (pos_t[0]+1, pos_h[1])

    x,y = new_h
    i,j = pos_t
    new_dist = math.sqrt((x-i)**2 + (y-j)**2)
    if(new_dist > math.sqrt(2)):
        return [new_h, new_t]
    else:
        return [new_h, pos_t] 


pos_set = set()
for line in lines:
    _dir,_dist = line.split(' ')
    dir, dist = _dir, int(_dist)
    for i in range(dist):
        print_grid()
        pos_h, pos_t = move(dir, pos_h, pos_t)
        pos_set.add(pos_t)
print_grid()
print(len(pos_set))