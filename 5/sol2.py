file_in = "p1.in"
file = open(file_in)
input = file.read()
lines = input.split("\n")
stacks = []
ops = []

if(file_in == "ex.in"):
    num_stacks = 3
    stacks = [[],[],[]]
else:
    num_stacks = 9
    stacks = [[],[],[],[],[],[],[],[],[]]

for line in lines:
    crates = ()
    tokens = ()
    if(line.find("[") != -1):
        #tokens = line.split(' ')
        for item in range(len(line)):
            if(int(item)%4 == 1):
                label = line[item]
                if(label != ' '):
                    stacks[int(item/4)].append(line[item])
                #print(line[item])
    else:
        tokens = line.split()
        if(len(tokens) > 0 and tokens[0] == "move"):
            ops.append([tokens[1], tokens[3], tokens[5]])
            #print(tokens)
print(stacks)
#print(len(ops))
#print(ops)

for i in range(len(ops)):
    num_crates = int(ops[i][0])
    src = int(ops[i][1])-1
    dest = int(ops[i][2])-1
    print(num_crates, src, dest)
    move_stack = []
    for j in range(num_crates):
        move_stack.append(stacks[src].pop(0))
    for j in range(num_crates):
        stacks[dest].insert(0,move_stack.pop())
    print(stacks)
end_string = ""
for stack in stacks:
    end_string = end_string + stack[0]
print(end_string)