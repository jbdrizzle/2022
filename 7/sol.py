import pprint
file = open("p1.in")
input = file.read()
lines = input.split("$ ")[1:]
#print(lines)

path = []
tree = {}
tree["/"] = {}
def do_ls(path, contents):
    #print("doing ls: ", path)
    #print(contents)
    base_hash = tree
    for key in path:
        base_hash = base_hash[key]
    #tree[str(path)] = {}
    for item in contents:
        line = item.split(' ')
        if(line[0] == "dir"):
            base_hash[line[1]] = {}
        else:
            base_hash[line[1]] = str(line[0])

            
def do_cd(path, dir):
    #print("moving from", path, "to", dir)
    if(dir == ".."):
        path.pop()
    elif (dir == '/'):
        path.clear()
        path.append(dir)
    else:
        path.append(dir)


for line in lines:
    subblock = line.split("\n")
    cmd = subblock[0]
    #print(cmd)
    if cmd[0:2] == "ls":
        contents = line.split("\n")[1::]
        for item in contents:
            if(item == ''):
                contents.remove(item)
        #contents = contents[0:len(contents)-1]
        do_ls(path, contents)
    elif cmd[0:2] == "cd":
        do_cd(path, cmd[3:])
    else:
        print("Doing nothing...")

sub_dirs = []
small_dirs = []
def travel_tree(dir):
    #print(dir.keys())
    total_dir_size = 0
    for key in dir.keys():
        if(type(dir[key]) == type("")):
            #print("found file: ", key)
            total_dir_size = total_dir_size + int(dir[key])
        elif(type(dir[key]) == type({})):
            #print("found dir: ", key)
            total_dir_size = total_dir_size + travel_tree(dir[key])
#    print("total size of dir", dir, total_dir_size)
    if(total_dir_size <= 100000):
        small_dirs.append(total_dir_size)
    sub_dirs.append(total_dir_size)

    return total_dir_size

#pprint.pprint(tree)
travel_tree(tree["/"])
print(sum(small_dirs))

print(max(sub_dirs))
unused_space = 70000000 - max(sub_dirs)
print(unused_space)
tbd_space = 30000000 - unused_space
print(tbd_space)
possible_dirs = []
for dir in sub_dirs:
    if dir > tbd_space:
        possible_dirs.append(dir)
print(min(possible_dirs))