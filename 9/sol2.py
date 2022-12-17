import math
file = open("p1.in")
input = file.read()
lines = input.split("\n")

knots = []
for i in range(10):
    knots.append((0,0))

def print_grid():
    out = ""
    num_rows = 5
    num_cols = 6

    for row in range(num_rows):
        for col in range(num_cols):
            match = False
            if(knots[0] == (col, num_rows-1-row)):
                out = out + "H"
                match = True
            for i in range(1,10):
                if(knots[i] == (col,num_rows-1-row) and not match):
                    out = out + str(i)
                    match = True
            if(not match):
                out = out + "."
        out = out + "\n"
    print(out)

def print_grid2():
    out = ""
    num_rows = 21
    num_cols = 26

    for row in range(num_rows):
        for col in range(num_cols):
            match = False
            if(knots[0] == (col-11, num_rows-1-row-5)):
                out = out + "H"
                match = True
            for i in range(1,10):
                if(knots[i] == (col-11,num_rows-1-row-5) and not match):
                    out = out + str(i)
                    match = True
            if(not match):
                out = out + "."
        out = out + "\n"
    print(out)

def move_new(pos_h, dir):
    if(dir == "U"):
        new_h = (pos_h[0], pos_h[1]+1)
        dx=0
        dy=1
    elif(dir == "D"):
        new_h = (pos_h[0], pos_h[1]-1)
        dx=0
        dy=-1
    elif(dir == "L"):
        new_h = (pos_h[0]-1, pos_h[1])
        dx=-1
        dy=0
    elif(dir == "R"):
        dx=1
        dy=0
        new_h = (pos_h[0]+1, pos_h[1])
    return [new_h, dx, dy]

def move_tail_new(pos_h, pos_t, dx,dy):
    prev_h = (pos_h[0]-dx,pos_h[1]-dy)
    dist_to_prev = math.sqrt((prev_h[0]-pos_t[0])**2 + (prev_h[1]-pos_t[1])**2)
    
    if(dist_to_prev > 1):
        dist_to_new = math.sqrt((pos_h[0]-pos_t[0])**2 + (pos_h[1]-pos_t[1])**2)
        if(dist_to_new > math.sqrt(6)):
            new_t = prev_h
            return [new_t,dx,dy]
        elif(dist_to_new > 2):
            new_t = prev_h
            dx=new_t[0]-pos_t[0]
            dy=new_t[1]-pos_t[1]
            return [new_t, new_t[0]-pos_t[0], new_t[1]-pos_t[1]]
        elif(dist_to_new == 2):
            if(pos_t[0] == pos_h[0]):
                dx = 0
                dy = int((pos_h[1]-pos_t[1])/2)
                new_t = (pos_t[0], pos_t[1]+dy)
                return [new_t, dx, dy]
            else:
                dy = 0
                dx = int((pos_h[0]-pos_t[0])/2)
                new_t = (pos_t[0]+dx, pos_t[1])
                return [new_t, dx, dy]
        else:
            return [pos_t, 0, 0]

    elif(dist_to_prev == 1):
        dist_to_new = math.sqrt((pos_h[0]-pos_t[0])**2 + (pos_h[1]-pos_t[1])**2)
        if(dist_to_new == 2):
            new_t = (pos_t[0]+dx,pos_t[1]+dy)
            return [new_t, dx, dy]
        elif(dist_to_new > 2):
            new_t = (pos_t[0]+dx, pos_t[1]+dy)
            return [new_t, dx, dy]
        else:
            return [pos_t,0,0]

    else:
        return [pos_t,0,0]

pos_set = set()
for line in lines:
    _dir,_dist = line.split(' ')
    dir, dist = _dir, int(_dist)
    for i in range(dist):
        prev_k = knots[1]
        knots[0], dx, dy = move_new(knots[0], dir)
        for j in range(1,10):
            knots[j], dx, dy = move_tail_new(knots[j-1], knots[j], dx, dy)
        pos_set.add(knots[9])

print(len(pos_set))