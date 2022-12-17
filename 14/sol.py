import sys
import time
#f = open("out.txt", 'w')
#sys.stdout = f

coords = [line.split(" -> ") for line in open("ex.in").read().split("\n")]
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

for x in range(max(x_sorted), min(x_sorted)-2, -1):
    for y in range(0, max(y_sorted)+1):
        if((x,y) not in grid.keys()):
            grid[(x,y)] = '.'


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
y_max = max(y_sorted)
def drop_a_grain(start_pos):
    current_pos = start_pos
    prev_pos = (-1,-1)
    while(current_pos != prev_pos):
        prev_pos = current_pos
        current_pos = move_a_spot(current_pos)
        grid[prev_pos] = '.'
        
        if(current_pos[0] == x_min or current_pos[1] == y_max):
            current_pos = (-1,-1)
            break
        grid[current_pos] = 'o'
    return current_pos


#drop_a_grain((500,0))
i = 0
while drop_a_grain((500,0)) != (-1,-1):
    i = i + 1
    if(i%10 == 0):
        print(i)
    print_grid()
print(i)