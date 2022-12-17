from enum import Enum
file = open("p1.in")
input = file.read()
lines = input.split("\n")

reg_x = 1
clk = 1
sum = 0

class cpu_st_t(Enum):
    NOOP = 0
    WAIT_ADD  = 1
    ADD = 2
    IDLE = 3

if(lines[0].split()[0] == "noop"):
    cpu_st = cpu_st_t.NOOP
    next_st = cpu_st_t.NOOP
else:
    cpu_st = cpu_st_t.WAIT_ADD
    next_st = cpu_st_t.ADD
index = 0

pixels = []

while(1):
    line = lines[index]
    cmd = line.split()
    if(cmd == []):
        break
    op = cmd[0]
    if(op == "addx"):
        arg = int(cmd[1])
    else:
        arg = 0

    next_cmd = lines[index+1]
    if(next_cmd != ""):
        next_op = next_cmd.split()[0]
    else:
        next_op = ""

    print(clk, cpu_st, "x=",reg_x, next_cmd)

    if(abs(((clk-1)%40)-reg_x) <= 1):
        pixels.append('#')
    else:
        pixels.append('.')

    if(clk in (20,60,100,140,180,220)):
    #    print("adding ", (clk)*reg_x)
        sum = sum + (clk)*reg_x

    match cpu_st:
        case cpu_st_t.NOOP:
            if(next_op == "addx"):
                next_st = cpu_st_t.WAIT_ADD
            else:
                next_st = cpu_st_t.NOOP
            index = index + 1
        case cpu_st_t.WAIT_ADD:
            next_st = cpu_st_t.ADD
        case cpu_st_t.ADD:
            if(next_op == "noop"):
                next_st = cpu_st_t.NOOP
            else:
                next_st = cpu_st_t.WAIT_ADD
            reg_x = reg_x + arg
            index = index + 1



    clk = clk + 1
    cpu_st = next_st 


print(sum)

out = ""
for i in range(6):
    for j in range(40):
       out = out + pixels[i*40+j]
    out = out + "\n"

print(out) 
