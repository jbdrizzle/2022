import pprint
file = open("p1.in")
input = file.read()
lines = input.split("\n")

map = []

r_i = 0
start_pos = (0,0)
end_pos = (0,0)
for line in lines:
    row = []
    for i in range(len(line)):
        row.append(line[i])
        if(line[i] == 'S'):
            start_pos = (r_i, i)
            row[i] = '`'
        if(line[i] == 'E'):
            end_pos = (r_i,i)
            row[i] = '{'
    map.append(row)
    r_i = r_i + 1
r_max = len(map)-1
c_max = len(map[0])-1

def check_if_path_forward_exists(pos, coord_visited_set):
    r = pos[0]
    c = pos[1]
    ooo = ord(map[r][c])
    if(r < r_max and (r+1,c) not in coord_visited_set):
        if(ord(map[r+1][c]) - ooo <= 1):
            return True
    if (r > 0 and (r-1,c) not in coord_visited_set):
        if(ord(map[r-1][c]) - ooo <= 1):
            return True
    if(c < c_max and (r,c+1) not in coord_visited_set):
        if(ord(map[r][c+1]) - ooo <= 1):
            return True
    if(c > 0 and (r,c-1) not in coord_visited_set):
        if(ord(map[r][c-1]) - ooo <= 1):
            return True
    return False

path_lengths_set = set()
def check_pos(pos, prev, _len, coord_visited_set):
    global r_max
    global c_max
    global end_pos
    r = pos[0]
    c = pos[1]
    ooo = ord(map[r][c])
    forward_paths = []
    equal_paths = []
    
    up = -99
    down = -99
    left = -99
    right = -99

    dirs = {"up": (r-1,c),
            "down": (r+1,c),
            "left": (r,c-1),
            "right": (r,c+1)}
    dists = {"up": -99,
             "down": -99,
             "left": -99,
             "right": -99}

    if(pos == end_pos):
        print(_len)
        path_lengths_set.add(_len)
        return

    if(r < r_max and dirs["down"] not in coord_visited_set):
        dists["down"] = ord(map[r+1][c]) - ooo
    if (r > 0 and dirs["up"] not in coord_visited_set):
        dists["up"] = ord(map[r-1][c]) - ooo
    if(c < c_max and dirs["right"] not in coord_visited_set):
        dists["right"] = ord(map[r][c+1]) - ooo
    if(c > 0 and dirs["left"] not in coord_visited_set):
        dists["left"] = ord(map[r][c-1]) - ooo

    coord_visited_set.add(pos)
    for dir in dirs.keys():
        if dists[dir] > 1:
            dists.pop(dir)
    for dir in dirs.keys():
        if not check_if_path_forward_exists(dirs[dir], coord_visited_set):
            dists.pop(dir)
    #print(max(dists, key=dists.get))
    return (dirs[max(dists, key=dists.get)]) #, pos, _len+1, coord_visited_set.copy())
    #for path in forward_paths:
    #    check_pos(path, pos, _len+1, coord_visited_set.copy())
    
prev_pos = start_pos
current_pos = start_pos
coord_visited_set = set()

coord_visited_set.add(start_pos)

len = 0
while (current_pos != end_pos):
    copy = current_pos
    current_pos = check_pos(current_pos, prev_pos, len, coord_visited_set)
    print(current_pos)
    prev_pos = copy
    len = len + 1
print(current_pos, len)
