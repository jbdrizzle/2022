import sys
import time
#f = open("out.txt", 'w')
#sys.stdout = f

coords = [line.split(" -> ") for line in open("p1.in").read().split("\n")]
#print(coords)
grid = {}
for path in coords:
    for i in range(len(path)-1):
        min_x = min(int(path[i+1].split(',')[0]), int(path[i].split(',')[0]))
        max_x = max(int(path[i+1].split(',')[0]), int(path[i].split(',')[0]))
        for x in range(min_x,max_x+1):
            min_y = min(int(path[i].split(',')[1]), int(path[i+1].split(',')[1]))
            max_y = max(int(path[i].split(',')[1]), int(path[i+1].split(',')[1]))
            for y in range(min_y,max_y+1):
                grid[(x,y)] = '#'

x_sorted = sorted(key[0] for key in grid.keys())
y_sorted = sorted(key[1] for key in grid.keys()) 

for x in range(max(x_sorted)+1, min(x_sorted)-2, -1):
    for y in range(0, max(y_sorted)+1):
        if((x,y) not in grid.keys()):
            grid[(x,y)] = '.'

for x in range(max(x_sorted)+1, min(x_sorted)-2, -1):
    for y in range(max(y_sorted)+1, max(y_sorted)+2):
        if((x,y) not in grid.keys()):
            grid[(x,y)] = '.'

for x in range(max(x_sorted)+1, min(x_sorted)-2, -1):
    for y in range(max(y_sorted)+2, max(y_sorted)+3):
        if((x,y) not in grid.keys()):
            grid[(x,y)] = '#'

x_sorted = sorted(key[0] for key in grid.keys())
y_sorted = sorted(key[1] for key in grid.keys()) 

def print_grid():
    out = ""

    for y in range(min(y_sorted), max(y_sorted)+1):
        for x in range(min(x_sorted), max(x_sorted)+1):
            out = out + grid[(x,y)]
        out = out + "\n"
    print(out)
#print_grid()

def move_a_spot(pos):
    x = pos[0]
    y = pos[1]
    if(grid[(x,y+1)] not in ('#','o')):
        return (x,y+1)
    elif(grid[(x-1,y+1)] not in ('#','o')):
        return (x-1,y+1)
    elif(grid[(x+1,y+1)] not in ('#','o')):
        return (x+1,y+1)
    else:
        return pos

x_min = min(x_sorted)
x_max = max(x_sorted)
y_max = max(y_sorted)
def drop_a_grain(start_pos):
    global x_min
    global x_max
    global x_sorted
    current_pos = start_pos
    prev_pos = (-1,-1)
    while(current_pos != prev_pos):
        prev_pos = current_pos
        current_pos = move_a_spot(current_pos)
        grid[prev_pos] = '.'
        if not (x_min < current_pos[0] < x_max):
            for j in range(0,y_max):
                grid[(x_min-1,j)] = '.'
                grid[(x_max+1,j)] = '.'
            grid[(x_min-1,y_max)] = '#'
            grid[(x_max+1,y_max)] = '#'
            x_min = x_min -1
            x_max = x_max+1
            x_sorted = sorted(key[0] for key in grid.keys())

        if(current_pos[1] == y_max):
            grid[current_pos] = 'o'
            break
        grid[current_pos] = 'o'
    return current_pos


#drop_a_grain((500,0))
i = 0
while drop_a_grain((500,0)) != (500,0):
    i = i + 1
    if(i%100 == 0):
        print(i)
        print_grid()
print(i+1)