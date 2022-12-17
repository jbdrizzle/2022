file = open("p1_2.in")
input = file.read()
lines = input.split("\n\n")
elves = []
for line in lines:
    elves.append(line.split("\n"))
print (elves)
total_cals_arr = []
top3 = [0,0,0]

def assign_new_max(max_in):
    print ("called new max: ", max_in)
    top3[2] = top3[1]
    top3[1] = top3[0]
    top3[0] = max_in
    return top3[0]

max_cals = 0
for elf in elves:
    total_cals = 0
    for food in elf:
        total_cals = total_cals + int(food)
    if total_cals > max_cals:
        assign_new_max(total_cals)
        max_cals = total_cals
    total_cals_arr.append(total_cals)
    print(total_cals_arr)
print(max_cals)
top3 = sorted(total_cals_arr)
print(top3[-1] + top3[-2] + top3[-3])
